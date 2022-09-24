from random import choice
from os import system, name


class Board:
    """
    class initialises the players (user and computer).
    Also has the print_score function that prints the score.
    """



    def __init__(self, user_name, user_score, computer_name, computer_score):
        global empty_board
        

        self.user_name = user_name
        self.user_score = user_score
        self.computer_name = computer_name
        self.computer_score = computer_score


    def print_score(self, player):
        """
        prints the score to the terminal.
        <name> score is <score>
        """
        if player == "user":
            print(f"{self.user_name.capitalize()} score is {self.user_score}\n")
        elif player == "computer":
            print(f"{self.computer_name.capitalize()} score is {self.computer_score}\n")

    def reset_board(self):
        """
        resets the playboard to empty state
        """
        empty_board = {
                        "A1": "| -",
                        "B1": "| - |",
                        "C1": "- |",
                        "A2": "| -",
                        "B2": "| - |",
                        "C2": "- |",
                        "A3": "| -",
                        "B3": "| - |",
                        "C3": "- |"}
        self.board_state = empty_board



def init_session():
    """
    Initialises the session and asks for the users name.
    Sets up computer and user class then  initialises the game.
    """

    print("Welcome to tic tac toe!\n")
    name_input = input("Please enter your name: ")
    while name_input == "":
        print("\nEmpty name input is not accepted!")
        name_input = input("Please enter your name: ")
    global board
    board = Board(name_input, 0, "computer", 0)
    init_game()


def init_game():
    """
    Initializes new game.
    """
    print("\nYou are X on the board.\n")
    board.reset_board()
    draw()
    handle_round()


def draw():
    """
    Draws the game board
    """
    temp_board_string = ""
    for k, v in board.board_state.items():

        if k == "A1":
            print("    A   B   C")
            temp_board_string += "1 "
            temp_board_string += f"{v} "
        elif k == "C1":
            temp_board_string += f"{v} \n"
            temp_board_string += "  ------------- \n2 "
        elif k == "C2":
            temp_board_string += f"{v} \n"
            temp_board_string += "  ------------- \n3 "
        else:
            temp_board_string += f"{v} "
    print(temp_board_string)


# 1 round counts as when both player and computer has made 1 move.
# Not a whole set.
def handle_round():
    """
    Handles each round after the player and computer selections.
    """
    handle_user_round()
    if check_if_game_is_over():
        draw()
        end_game(check_if_game_is_over())
        return
    handle_computer_round()
    draw()
    if check_if_game_is_over():
        end_game(check_if_game_is_over())
    else:
        handle_round()


def handle_user_round():
    """
    Handles the user selection and verifies that the selection has a valid
    value and checks if the selection is occupied.
    """
    try:
        user_input = input("Select placement for example A1: ").upper()
        if "X" in board.board_state[user_input] or "O" in board.board_state[user_input]:
            print(f"Please select a valid placement. {user_input}"
                  " is already occupied!")
            handle_user_round()
        board.board_state.update(
            {user_input: board.board_state[user_input].replace("-", "X")})

    except KeyError:
        if user_input == "":
            print("Please enter a placment again, you sent an empty command.")
        else:
            print(
                 "Please select a valid placement. "
                 f"{user_input} is not a valid input!")
        handle_user_round()


def handle_computer_round():
    """
    Handles the computer selection and checks if the selection is occupied.
    If it is, it will loop and select a new.
    """
    while True:
        temp_computer_key = choice(list(board.board_state.keys()))
        if "X" not in board.board_state[temp_computer_key] and \
           "O" not in board.board_state[temp_computer_key]:
            board.board_state.update({temp_computer_key:
                                      board.board_state[temp_computer_key]
                                      .replace("-", "O")})
            break


def check_if_game_is_over():
    """
    Will check if game has a winner or if the board is full.
    """
    if check_winner():
        return check_winner()
    elif check_if_board_full():
        return "draw"
    else:
        return False


def check_if_board_full():
    """
    Checks if the board is full
    """
    board_count = 0
    result = False
    for k, v in board.board_state.items():
        if "-" in v:
            break
        else:
            board_count += 1
    if board_count == 9:
        result = True
    return result


def check_winner():
    """
    Checks if there are any winners in the current board state
    """
    if "X" in board.board_state["A1"] and \
       "X" in board.board_state["A2"] and "X" in board.board_state["A3"]:
        return "win"
    elif "O" in board.board_state["A1"] and \
         "O" in board.board_state["A2"] and "O" in board.board_state["A3"]:
        return "loss"
    elif "X" in board.board_state["B1"] and \
         "X" in board.board_state["B2"] and "X" in board.board_state["B3"]:
        return "win"
    elif "O" in board.board_state["B1"] and \
         "O" in board.board_state["B2"] and "O" in board.board_state["B3"]:
        return "loss"
    elif "X" in board.board_state["C1"] and \
         "X" in board.board_state["C2"] and "X" in board.board_state["C3"]:
        return "win"
    elif "O" in board.board_state["C1"] and \
         "O" in board.board_state["C2"] and "O" in board.board_state["C3"]:
        return "loss"
    elif "X" in board.board_state["A1"] and \
         "X" in board.board_state["B1"] and "X" in board.board_state["C1"]:
        return "win"
    elif "O" in board.board_state["A1"] and \
         "O" in board.board_state["B1"] and "O" in board.board_state["C1"]:
        return "loss"
    elif "X" in board.board_state["A2"] and \
         "X" in board.board_state["B2"] and "X" in board.board_state["C2"]:
        return "win"
    elif "O" in board.board_state["A2"] and \
         "O" in board.board_state["B2"] and "O" in board.board_state["C2"]:
        return "loss"
    elif "X" in board.board_state["A3"] and \
         "X" in board.board_state["B3"] and "X" in board.board_state["C3"]:
        return "win"
    elif "O" in board.board_state["A3"] and \
         "O" in board.board_state["B3"] and "O" in board.board_state["C3"]:
        return "loss"
    elif "X" in board.board_state["A1"] and \
         "X" in board.board_state["B2"] and "X" in board.board_state["C3"]:
        return "win"
    elif "O" in board.board_state["A1"] and \
         "O" in board.board_state["B2"] and "O" in board.board_state["C3"]:
        return "loss"
    elif "X" in board.board_state["C1"] and \
         "X" in board.board_state["B2"] and "X" in board.board_state["A3"]:
        return "win"
    elif "O" in board.board_state["C1"] and \
         "O" in board.board_state["B2"] and "O" in board.board_state["A3"]:
        return "loss"


def end_game(message):
    """
    Handles the game ending, and adds score to the winning player,
    or if draw, no score is added
    """

    print(f"\nThe game ends in a {message}!")
    if message == "win":
        board.user_score += 1
    if message == "loss":
        board.computer_score += 1

    board.print_score("user")
    board.print_score("computer")

    play_again_input = input(
        "If you want to go for another round, please type Y: ").upper()
    if play_again_input == "Y":
        cls()
        init_game()


def cls():
    """
    Checks if the terminal is based on Windows or another OS.
    Then uses the right clear terminal command.
    """
    system('cls' if name == 'nt' else 'clear')


init_session()

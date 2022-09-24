from random import choice
from os import system, name as os_name


class Session:
    """
    a class repressenting a session of tic tac toe
    """
    def __init__(self, player_name):
        self.user = Player(player_name)
        self.computer = Player("computer")
        self.board_state = {}
        self.init_board()

    def init_board(self):
        """
        reset playboard
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


class Player:
    """
    a class representing the player
    """
    def __init__(self, name):
        self.name = name
        self.score = 0

    def print_score(self):
        """
        prints the score to the terminal.
        <name> score is <score>
        """
        print(self.name.capitalize() +
              f" score is {self.score}\n")


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
    global session
    session = Session(name_input)
    init_game()


def init_game():
    """
    Initializes new game.
    """
    print("\nYou are X on the board.\n")
    draw()
    handle_round()


def draw():
    """
    Draws the game board
    """
    temp_board_string = ""
    for k, v in session.board_state.items():

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
        if "X" in session.board_state[user_input] or \
           "O" in session.board_state[user_input]:
            print(f"Please select a valid placement. {user_input}"
                  " is already occupied!")
            handle_user_round()
        session.board_state.update(
            {user_input: session.board_state[user_input].replace("-", "X")})

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
        temp_computer_key = choice(list(session.board_state.keys()))
        if "X" not in session.board_state[temp_computer_key] and \
           "O" not in session.board_state[temp_computer_key]:
            session.board_state.update({temp_computer_key:
                                       session.board_state[temp_computer_key]
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
    for k, v in session.board_state.items():
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
    if "X" in session.board_state["A1"] and \
       "X" in session.board_state["A2"] and "X" in session.board_state["A3"]:
        return "win"
    elif "O" in session.board_state["A1"] and \
         "O" in session.board_state["A2"] and "O" in session.board_state["A3"]:
        return "loss"
    elif "X" in session.board_state["B1"] and \
         "X" in session.board_state["B2"] and "X" in session.board_state["B3"]:
        return "win"
    elif "O" in session.board_state["B1"] and \
         "O" in session.board_state["B2"] and "O" in session.board_state["B3"]:
        return "loss"
    elif "X" in session.board_state["C1"] and \
         "X" in session.board_state["C2"] and "X" in session.board_state["C3"]:
        return "win"
    elif "O" in session.board_state["C1"] and \
         "O" in session.board_state["C2"] and "O" in session.board_state["C3"]:
        return "loss"
    elif "X" in session.board_state["A1"] and \
         "X" in session.board_state["B1"] and "X" in session.board_state["C1"]:
        return "win"
    elif "O" in session.board_state["A1"] and \
         "O" in session.board_state["B1"] and "O" in session.board_state["C1"]:
        return "loss"
    elif "X" in session.board_state["A2"] and \
         "X" in session.board_state["B2"] and "X" in session.board_state["C2"]:
        return "win"
    elif "O" in session.board_state["A2"] and \
         "O" in session.board_state["B2"] and "O" in session.board_state["C2"]:
        return "loss"
    elif "X" in session.board_state["A3"] and \
         "X" in session.board_state["B3"] and "X" in session.board_state["C3"]:
        return "win"
    elif "O" in session.board_state["A3"] and \
         "O" in session.board_state["B3"] and "O" in session.board_state["C3"]:
        return "loss"
    elif "X" in session.board_state["A1"] and \
         "X" in session.board_state["B2"] and "X" in session.board_state["C3"]:
        return "win"
    elif "O" in session.board_state["A1"] and \
         "O" in session.board_state["B2"] and "O" in session.board_state["C3"]:
        return "loss"
    elif "X" in session.board_state["C1"] and \
         "X" in session.board_state["B2"] and "X" in session.board_state["A3"]:
        return "win"
    elif "O" in session.board_state["C1"] and \
         "O" in session.board_state["B2"] and "O" in session.board_state["A3"]:
        return "loss"


def end_game(message):
    """
    Handles the game ending, and adds score to the winning player,
    or if draw, no score is added
    """

    print(f"\nThe game ends in a {message}!")
    if message == "win":
        session.user.score += 1
    if message == "loss":
        session.computer.score += 1

    session.user.print_score()
    session.computer.print_score()

    play_again_input = input(
        "If you want to go for another round, please type Y: ").upper()
    if play_again_input == "Y":
        cls()
        session.init_board()
        init_game()


def cls():
    """
    Checks if the terminal is based on Windows or another OS.
    Then uses the right clear terminal command.
    """
    system('cls' if os_name == 'nt' else 'clear')


init_session()

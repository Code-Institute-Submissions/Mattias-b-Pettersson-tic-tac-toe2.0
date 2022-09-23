import random

def init_game():
    """
    Initializes the game.
    """
    print("Welcome to tic tac toe!")
    print("You are X on the board.")

    global board_state
    board_state = {
        "A1": "| -",
        "B1": "| - |",
        "C1": "- |",
        "A2": "| -",
        "B2": "| - |",
        "C2": "- |",
        "A3": "| -",
        "B3": "| - |",
        "C3": "- |"}
    draw()
  
    handle_round()


def draw():
    """
    Draws the game board
    """
    board = ""
    for k, v in board_state.items():

        if k == "A1":
            print("    A   B   C")
            board += "1 "
            board += f"{v} "
        elif k == "C1":
            board += f"{v} \n"
            board += "  ------------- \n2 "
        elif k == "C2":
            board += f"{v} \n"
            board += "  ------------- \n3 "
        else:
            board += f"{v} "
    print(board)  


def handle_round():
    """
    Handles each round after the player and computer selections.
    """
    handle_user_round()
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
        user_input = input("Select placement: ").upper()
        if "X" in board_state[user_input] or "O" in board_state[user_input]:
            print(f"Please select a valid placement. {user_input}"\
                " is already occupied!")
            handle_user_round()
            
        board_state.update({user_input: board_state[user_input].replace("-", "X")})

    except KeyError:
        print(f"Please select a valid placement. {user_input} is not a valid input!")
        handle_user_round()


def handle_computer_round():
    """
    Handles the computer selection and checks if the selection is occupied. If it is, it will loop and select a new.
    """
    while True:
        temp_computer_key = random.choice(list(board_state.keys()))
        if "X" or "O" not in board_state[temp_computer_key]:
            board_state.update({temp_computer_key: board_state[temp_computer_key].replace("-", "O")})
            break


def check_if_game_is_over():
    """
    Will check if game is over by either the board is full or the game has a winner.
    """
    #check_winner() 

    if check_if_board_full():
        return "draw"
    else:
        return False


def check_if_board_full():
    """
    Checks if the board is full
    """
    board_count = 0
    result = False
    for k, v in board_state.items():
        if "-" in v:
            break
        else:
            board_count += 1
    if board_count == 9:
        result = True
    return result


def check_winner():
    print("hej hej")


def end_game(message):
    print(f"The game ends in a {message}")

init_game()
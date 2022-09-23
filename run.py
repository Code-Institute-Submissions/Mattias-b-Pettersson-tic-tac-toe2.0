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
    handle_user_round()
    #handle_computer_round()
    draw()
    # if check_if_game_is_over():
        # end_game()
    # else:
        # handle_round()

def handle_user_round():
    try:
        user_input = input("Select placement: ")
        if "X" or "O" in board_state[user_input]:
            handle_user_round_retry(user_input)

        board_state.update({user_input: board_state[user_input].replace("-", "X")})

def init_game():
    print("Welcome to tic tac toe!")

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

init_game()
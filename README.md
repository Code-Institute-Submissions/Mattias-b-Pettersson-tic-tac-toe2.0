![Multiple screens image](assets\readme-images\multiple-screens.png)

# Tic Tac Toe
Tic Tac Toe is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users can try to beat the computer by getting three circles in a row against the computer.
Here is the live version of the [project](https://tic-tac-toe-matte.herokuapp.com/).

# How to play

Tic Tac Toe is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner

You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe).

On this website, you enters your name in the beginning of the game and a playboard is generated. You can then choose your placement and then the computer, your oponent, makes a move. Then this is repeated til the game is over and the score is stored and displayed, then you can choose to go for another round.

# Features

## Existing Features

- play multiple rounds.

- Play against the computer.

- Accepts user input.

- Maintains scores.


  ![score count image](assets\readme-images\score-count.png)

- Input validation and error-checking.

  ![error testing image](assets\readme-images\invalid-input.png)
  - you cannot provide an empty input.
  - You cannot cannot place your marker outside the size of the grid.
  - You cannot place your marker on a square that is already occupied.
  - You cannot provide an invalid input such as "cat"

- Data maintained in class instances.

## Future Features

- Allow the player to choose who begins the round.
- Allow the player to choose that every other player starts.
- Allow for 2 players, and not only one against the computer.

#  Data Model

I decided to use a session class as my model. From there it creates 1 instance of the board to hold the state of the board. And it also creates two more classes, one for the player and one for the computer.
The session class stores the board, the position of current marks. The player class stores one name and score.
The 2 classes also has methods to help play the game. A print score method and a initialize board method.

# Testing

I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs: placed on a occupied square, given a input that is outside the playboard, given a random input as for example "cat".
- Tested in my local terminal and the Code Institute Heroku terminal.
Bugs

## Solved Bugs

- When I wrote the project, I forgot that the game could be over before both players had made a placement, so as the last square was filled, the computer tried to fill a empty square but none where left. This led to an infinite loop and the game broke. i fixed this by checking if the game was over before the computer made a move, and also one after.

## Remaining Bugs

- No bugs remaining.

# Validator Testing

[PEP8](http://pep8online.com/). No errors are returned now but alot of "line to long" errors were fixed.

# Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
Steps for deployment:
- Fork or clone this repository 
- Create a new Heroku app 
- Set the buildbacks to Python and NodeJS in that order.
- You must add a Config Var to Heroku the settings. The key is PORT and the value is 8000
- Link the Heroku app to the repository
- Click on Deploy.

# Credits

- Code Institute for the deployment terminal
- Code Institute for the deplyment steps above.
- [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe) for the details of the Battleships game
- Poke on stack overflow for the cls function. [Link.](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)


# Breakout
Your goal is to implement two-player chess.

Gameplay will consist of the two players taking turns making moves by entering their move in algebraic notation (see `https://en.wikipedia.org/wiki/Algebraic_notation_(chess)`); the player with the white pieces will always make the first move of the game.
Moves must obey the rules of chess (see `https://en.wikipedia.org/wiki/Rules_of_chess`), and all of the rules must be implemented.
Only legal moves will be carried out on the board; illegal moves will be disregarded, prompting the offending player to enter a legal move.

Next to the board, on each player's respective side, there should be a list of the pieces that player has captured from his opponent.
If you're ambitious enough, you can also implement a time control system (with or without increment) that will display each player's remaining time in real-time next to the board.

Unicode characters for rendering the chess pieces are given below in `KQRBNP` order.
- `♔♕♖♗♘♙`
- `♚♛♜♝♞♟` 
In order to render the board properly, make sure to read the documentation on displaying foreground and background colors using `blessed`.
- `https://blessed.readthedocs.io/en/latest/colors.html`

# Requirements
## Piece
+ `type` attribute
  - returns a string corresponding to the type of piece this is (one of `K`, `Q`, `R`, `B`, `N`, or, `P`).
+ `move()` method
  - moves the piece to the corresponding square

## Square
+ `location` attribute
  - returns the coordinates, in terms of the board's coordinate system, of this square
+ `piece` attribute
  - is of type `None` or `Piece` depending on whether this square is occupied by a piece
+ `__contains__()` method
  - implements the `_ in _` operation
  - returns a boolean based on whether this square contains the given piece

## Board
Contains the current state of the board, composed of Square.
Displays captured pieces (and, possibly, player times) next to it.

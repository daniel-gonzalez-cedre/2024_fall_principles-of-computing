# Breakout
Your goal is to produce a single-player, real-time implementation of the classic Atari game Breakout.

`https://youtu.be/AMUv8KvVt08?t=25`

Gameplay consists of a paddle which the player moves side-to-side to bounce a ball.
When the ball comes into contact with the paddle, the ball bounces off at an angle determined by the contact point.
When the ball comes into contact with a brick, it bounces off at a right-angle and destroys the brick.

Bricks come in three colors: green, yellow, and red (though you can feel free to implement more).
Each destroyed brick grants points based on its color.

| green | yellow |  red  |
| ----- | ------ | ----- |
| 1 pt  | 2 pts  | 5 pts |

A scoreboard at the top of the screen keeps track of the player's current score along with their chosen three-character name (default player name is `aaa` if none is chosen).

The game ends in a loss if the ball falls below the bottom edge of the screen.
The game ends in a victory if all of the bricks are cleared.

# Requirements
## Menu
1. New Game
  - displays a new screen and begins a new game
2. Choose Name
  - displays a new screen allowing the user to set their name
3. Leaderboard
  - displays a list of the top 5 best players of all time along with their highest scores

+ `move()` method
   - moves the selector up or down according to the player's input
+ `select()` method
   - activates the menu option that is currently selected
+ `selected` attribute
   - returns information identifying which menu option the selector is on

## Ball
+ `location` attribute
  - returns the coordinates of the paddle's center of mass
+ `move()` method
  - moves the ball by one unit according to the ball's velocity and trajectory
+ `respawn()` method
  - spawns the ball in the center of the screen

## Paddle
+ `location` attribute
  - returns the coordinates of the paddle's center of mass
+ `bounding_box` attribute
  - returns the coordinates of the four corners of the paddle's bounding box
+ `move()` method
  - moves the paddle one unit in the direction (either left or right) the player selects
+ `respawn()` method
  - spawns the paddle at the bottom of the screen, vertically centered

## Brick
+ `location` attribute
  - returns the coordinates of the brick's center of mass
+ `bounding_box` attribute
  - returns the coordinates of the four corners of the brick's bounding box

## Scoreboard
1. Displays at the top of the screen above the playable area.
2. Displays the current score at the top left.
3. Displays the player's name at the top right.

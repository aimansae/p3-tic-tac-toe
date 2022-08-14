# TIC TAC TOE Game - Python

## Introduction

Tic Tac Toe game is the third project challenge with Code Institute in order to acquire the Full Stack Developer diploma. The game is created using Python, as required.

Tic-tac-toe is a game where two players take turns in drawing either an ' O' or an ' X' in one square of a grid consisting of nine squares, against the computer.
The first player who gets 3 same symbols in a row (horizontally, vertically or diagonally) wins!

Please find the live progect [here:](https://p3-tic-tac-toe.herokuapp.com/) 

***foto  amiresponsive

## Table Of Contents
+ [UX](#ux "UX")
  + [User Stories](#userstories "User Stories")
    + [As a player:](#first-time-user "As a player:")
+ [Features](#features "Features")  
  + [Introduction](#Introduction "Introduction")
  + [Instructions](#Instructions "Instructions") 
   + [Start Game](#Start-Game "Start Game")  







## UX:
### User Stories
#### As a player:

- I want to play a game with clear and easy instructions
- I want to be able to see my scores
- I want to be able to play the game again or quit easily    

## Features:

### Introduction

Once the program runs, the user is welcomed to the game and they are asked them to insert their Name. This will be used through the game for fidelization purposes.
The "welcome to the game" statement has a sys.stdout.flush() method applied for a better visual effect.

![Introduction](images/introduction.screenshot.png) 

### Instructions
After the validated name is inserted, a small explaination of the rules is shown , as per screenshot below:
**foto 

### Start Game
In the next step the user is asked to type "S" to start playing. Thanks to the validation, the terminal wil accept any "S" format, uppercase or lower, if the elemeny typed is different that "S" they will get error message stating to tye "S" again.

**foto

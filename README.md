# Chess Bot

This is the github repository for the chess bot we will be making in the Harper Society of Engineers. Currently this is just a frame for what the repository will look like and I will be updating this more and more once I learn what we need to install and such.

The plan is for this to be coded in python but if that is not possible we can use a different language.

Might need YOLO from ultralytics for image recognision but idk.



## Psuedocode

#### Main Loop

start loop
get move from user (either via input in command line or picture from camera)
send move to chess board (verify that this is a valid move, otherwise get another move)
check if game over, if game over end loop else
get move back from stockfish
translate stockfish move to positions on the 3d printer (3d printer is 220mm by 220mm)
move the 3d printer to make a move
check if game over, if game over end loop else continue to next iteration


#### Move piece logic

get positions (start and end)
get if the move is a capture (so we know we have to get rid of that piece)
if capture:
  move hand to end pos
  pick up piece
  move piece off board (idk how yet)
move the hand to the start piece
pick up piece
move hand to end pos
put down piece
return to origin (or just stay idk yet)

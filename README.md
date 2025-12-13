# Chess Bot

This is the main code for the logic behind the chess bot made from an old/broken 3d printer for the Harper Society of Engineers.

I updated this with everything anyone should need to write code if you're bored or just want to contribute in some way. If anyone has questions just contact me. 


## Plan

In case anyone wants to work on this here is the plan for what we need and what we have. 

Currently we only have 3 files/classes and they can be renamed if needed to make their purpose more clear.

Chess Logic is what I mainly started. It uses the python-chess library to communicate with Stockfish. If you want to see how this works you can read the docs or look through my code. The purpose of this class is to handle all chess functions. The primary communication it will have with other classes is by using UCI strings. UCI strings is as simple as something like "a2g4". This simply says that it will move the piece from location a2 and put it onto the square g4. This makes it simple to translate to our bot. This translation will be its own class.

This second class I have labeled in the file printer_commands. This class has only one job, translate from G code commands or a x, y postion on the board in mm to UCI. To understand G code you can do a quick google search, basically it gives a command like G90, and then followed by coordinates in the order X Y Z F, where F is the speed at which the arm moves (right now it is hard codded at 3000 since that seems to work the best). This also should have the function of translating from UCI to G code aswell.

The third one I made is labeled printer_comm. This class is made to be able to comminicate with the printer itself. I haven't done much research in this one yet since I haven't connected to the printer in a while but the code I have made there should work, at least maybe. This uses the library called pyserial. The only job for this one is to send a G code command to the printer. This needs lots of work since we need a way to make sure multiple commands aren't sent at the same time, we need to make sure the right commands are sent. 

Any other class/file can be added with no issue, it don't really matter just make sure names make sense. Also try and make unit tests for files since that will make sure that everything works correctly and give us practice making them. 

#### Other code

If you don't want to work on the python code for this, we do still need the arduino code to be able to control the electro magnet, we also need some sort of code that will take this python code and communicate with the arduino code. I haven't looked into this at all so good luck. 



## How to make everything work

First you gotta clone this repo.

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and Python version control. We use [ruff](https://github.com/astral-sh/ruff) for linting and formatting.

### 1. Install `uv`
If you haven't already, install `uv` (the ultra-fast Python package installer).

### 2. Initialize project
Run the following command to install the correct Python version and all dependencies automatically:
```bash
uv sync
```

This creates a virtual environment in .venv. You do not need to manually activate it if you use uv run commands, but you can activate it with source .venv/bin/activate (Mac/Linux) or .venv\Scripts\activate (Windows).

### 3. Create Branch For Feature

First sync from main to get all code up to date:
```bash
git checkout main
git pull origin main
```

Then make a new branch (create a branch and work on one feature, basically like one class or something like that, make multiple commits to save ur history in case u need to go back on something):
```bash
git checkout -b feature/your-feature-name
```

Before pushing any code, you must run the linter and formatter. We use ruff for both. This just makes it look good and follow naming convention standard since python is a lot more strict than c++ or other languages.

To Check for Errors (Linting):
```bash
uv run ruff check
```
To Auto-Format Your Code:
```bash
uv run ruff format
```

Lastly you push to origin and open a pull request:
```bash
git push -u origin feature/your-feature-name
```

Go to GitHub and open a Pull Request against main. Add a description of your changes. This then will need to be reviewed to make sure there are no merge conflicts which I will do, it might notify me about it but either way just lmk and I can do it. 

Going thru all this might seem like a lot of work but this is how any company does github workflow and the same for any open source projects. This is all command line commands for git and github but since I know some of y'all use either github desktop or something else you will have to look it up. the only one you gotta look up is branches, both making a new one and switching between them. Also once you merge you can look up how to delete old ones. 







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

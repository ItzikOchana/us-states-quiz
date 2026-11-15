# U.S. States Quiz

A guessing game built with Python's `turtle` module and `pandas`.
Type the name of a U.S. state and, if you are right, it appears on the map in the right place.

## How it works
- Guess the 50 states one by one. Each correct guess adds a point to the scoreboard.
- Type `exit` (or press Cancel) to quit. The states you missed are saved to `states_to_learn.csv`.
- Guess all 50 to win.

State names and their map coordinates are in `50_states.csv`.

## Run
```
pip install -r requirements.txt
python main.py
```

Requires Python 3 with Tkinter (included in the standard Python installers).

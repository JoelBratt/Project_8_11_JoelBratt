"""
scoreboard.py
Joel Bratt
handles File I/o and JSON data to track player score across sessions
7/8/2026
"""
import json
import os 

SCORE_FILE = 'scores.json'

def load_scores():
    """Reads the score.json file doesn't exist, it returns a dictionary."""

    default_scores = {"Player": 0, "CPU": 0, "Ties": 0}
    
    if os.path.exists(SCORE_FILE):
        try:
            """opens and reads the json"""
            with open(SCORE_FILE, 'r') as file:
                loaded_scores = json.load(file)
                if isinstance(loaded_scores, dict):
                    default_scores.update(loaded_scores)
        except (json.JSONDecodeError, OSError):
            """if broken or empty ignores it and returns the normal scores"""
            pass 
            
    return default_scores
    
def save_scores(scores):
    """Writes the scores to the json"""
    with open(SCORE_FILE, 'w') as file:
        json.dump(scores, file, indent=4)

def display_scoreboard(scores):
    """Prints the current standings to the console."""
    print('=== SCOREBOARD ===')
    print(f'Player: {scores['Player']} | CPU: {scores['CPU']} | Ties: {scores['Ties']}')
    print('===================\n')
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
    if os.path.exists(SCORE_FILE):
        """open and read the file"""
        with open(SCORE_FILE, 'r') as file:
            return json.load(file)
    else:
        return {"Plauer":0, "CPU":0, "Ties":0}
    
def save_scores(scores):
    """Writes the scores to the json"""
    with open(SCORE_FILE, 'w') as file:
        json.dump(scores, file, indent=4)

def display_scoreboard(scores):
    """Prints the current standings to the console."""
    print('=== SCOREBOARD ===')
    print(f'Player: {scores['Player']} | CPU: {scores['CPU']} | Ties: {scores['Ties']}')
    print('===================\n')
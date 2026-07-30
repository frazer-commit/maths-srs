import pandas as pd
import json

with open("settings.json") as f:
    config = json.load(f)

DECK_PATH = config["deckPath"]
deck = pd.read_csv(DECK_PATH)

REGISTRY = {}

def register(question):
    REGISTRY[question.__name__] = question.write
    
    if question.__name__ not in deck["name"].values:
        deck.loc[len(deck)] = {"name": question.__name__,
                               "dependencies": [q.__name__ for q in question.dependencies]
                              }

    return question

from . import arithmetic


deck.to_csv(DECK_PATH, index=False)

if __name__ == "__main__":
    print(REGISTRY)

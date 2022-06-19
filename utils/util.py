import json

from os import path, getcwd
from datetime import  date

class Data:
    def __init__(self):

        self.json_obj = None
        self.open_file()

    def open_file(self):
        with open(path.join(getcwd() + "/utils/data.json"), "r") as file:
            self.json_obj = json.load(file)

    def add_score(self, score):
        if len(self.json_obj["score"]) <= 5:
            self.json_obj['score'].append(score)
            self.json_obj['date'].append(f"{date.today()}")


        for score_json_index, score_json in enumerate(self.json_obj['score']):
            if score > score_json and len(self.json_obj["score"]) > 5:
                self.json_obj["score"].pop(score_json_index)
                self.json_obj["date"].pop(score_json_index)

        self.save_file()

    def save_file(self):
        with open(path.join(getcwd() + "/utils/data.json"), "w") as save:
            json.dump(self.json_obj, save, indent=4)

    def reset(self):
        with open(path.join(getcwd() + "/utils/data.json"), "w"):
            self.json_obj = {"score": [0, 0, 0, 0, 0], "date": ["yyyy/mm/dd", "yyyy/mm/dd", "yyyy/mm/dd", "yyyy/mm/dd", "yyyy/mm/dd"]}

            self.save_file()

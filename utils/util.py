import json

from os import path, getcwd
from datetime import  date

class Data:
    def __init__(self):

        self.json_obj = None
        self.open_file()
        self.organize_file()

    def open_file(self):
        with open(path.join(getcwd() + "/utils/data.json"), "r") as file:
            self.json_obj = json.load(file)

    def add_score(self, score):
        self.json_obj['score'].append(score)
        self.json_obj['date'].append(f"{date.today()}")

        self.organize_file()
        self.save_file()

    def save_file(self):
        with open(path.join(getcwd() + "/utils/data.json"), "w") as save:
            json.dump(self.json_obj, save, indent=4)

    def organize_file(self):
        for i in range(len(self.json_obj["score"])):
            for j in range(i):
                if self.json_obj["score"][j] > self.json_obj["score"][j+1]:
                    temp_score = self.json_obj["score"][j]
                    self.json_obj["score"][j] = self.json_obj["score"][j+1]
                    self.json_obj["score"][j+1] = temp_score

                    temp_date = self.json_obj["date"][j]
                    self.json_obj["date"][j] = self.json_obj["date"][j+1]
                    self.json_obj["date"][j+1] = temp_date

        self.json_obj["score"] = list(reversed(self.json_obj["score"]))
        self.json_obj["date"] = list(reversed(self.json_obj["date"]))

    def reset(self):
        with open(path.join(getcwd() + "/utils/data.json"), "w"):
            self.json_obj = {"score": [0, 0, 0, 0, 0], "date": ["yyyy/mm/dd", "yyyy/mm/dd", "yyyy/mm/dd", "yyyy/mm/dd", "yyyy/mm/dd"]}

            self.save_file()

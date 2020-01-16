import uuid
import os
import json

class Model:

    def __init__(self, controller):
        self.controller = controller
    

    def initNewFile(self):
        cfg = self.controller.config
        self.filename = os.path.join(cfg["resultsFolder"], f"{uuid.uuid4()}.json")

        with open(self.filename, "x") as fp:
            d = dict()
            json.dump(d, fp)
            
            
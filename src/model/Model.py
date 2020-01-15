import uuid
import os

class Model:

    def __init__(self, controller):
        self.controller = controller
        self.initResultFile()
    
    def initResultFile(self):
        cfg = self.controller.config
        self.filename = os.path.join(cfg["resultsFolder"], f"{uuid.uuid4()}.json")
        # Create result file
        with open(self.filename, 'w'):
            pass
            
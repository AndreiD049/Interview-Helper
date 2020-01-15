import json
import os

class Validator:
    """ 
       File validator
    """
    def __init__(self, val_type):
        self.validator = val_type

    def validate(self, *args, **kwargs):
        return self.validator.run(*args, **kwargs)

class TypingTestValidator:

    def run(self, file):
        with open(file, 'r') as fp:
            try:
                d = json.load(fp)
            except json.JSONDecodeError:
                return False
            if "expected" not in d:
                return False
            return True

class ErrorCheckingValidator:

    def run(self, file):
        with open(file, 'r') as fp:
            try:
                d = json.load(fp)
            except json.JSONDecodeError:
                return False
            if "image" not in d:
                return False
            if not os.path.isfile(d["image"]):
                return False
            if "question" not in d:
                return False
            if "answer" not in d:
                return False
            if "options" not in d:
                return False
            return True


ValidatorTyping = Validator(TypingTestValidator())
ValidatorErrorChecking = Validator(ErrorCheckingValidator())
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
            # test image tag
            if "image" not in d:
                return False
            elif not os.path.isfile(d["image"]):
                return False
            elif type(d["image"]) != str:
                return False
            # test question tag
            if "question" not in d:
                return False
            elif len(d["question"]) == 0:
                return False
            elif type(d["question"]) != str:
                return False
            # test answers tag
            if "answers" not in d:
                return False
            elif len(d["answers"]) == 0:
                return False
            elif type(d["answers"]) != list:
                return False
            # test options tag
            if "options" not in d:
                return False
            elif len(d["options"]) < 2:
                return False
            elif type(d["options"]) != list:
                return False
            return True


ValidatorTyping = Validator(TypingTestValidator())
ValidatorErrorChecking = Validator(ErrorCheckingValidator())
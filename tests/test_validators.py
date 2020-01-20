import unittest
import os
import source.validators as v

class TestValidators(unittest.TestCase):

    def test_typing(self):
        self.assertTrue(True)
    
    def test_is_instance(self):
        self.assertIsInstance(v.ValidatorTyping, v.Validator)

    def test_typing_validator(self):
        self.assertTrue(v.ValidatorTyping.validate(os.path.join(os.path.split(__file__)[0], "assets", "typing_correct.json")))
        self.assertFalse(v.ValidatorTyping.validate(os.path.join(os.path.split(__file__)[0], "assets", "typing_incorrect.json")))

    def test_error_checking(self):
        self.assertTrue(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_correct.json")), "Test correct file")
        self.assertFalse(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_invalid_path.json")), "Test invalid path")
        self.assertFalse(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_incorrect_type.json")), "Test invalid type of question")
        self.assertFalse(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_answers_type.json")), "Test invalid answers type")
        self.assertFalse(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_missing answers.json")), "Test missing answer")
        self.assertFalse(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_options missing.json")), "Test missing options")
        self.assertFalse(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_options type.json")), "Test checking options type")
        self.assertTrue(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_correct options length.json")), "Test checking valid options length")
        self.assertFalse(v.ValidatorErrorChecking.validate(os.path.join(os.path.split(__file__)[0], "assets", "error_checking_incorrect options length.json")), "Test checking invalid options length")

if __name__ == "__main__":
    unittest.main()
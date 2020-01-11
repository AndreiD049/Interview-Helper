import difflib
import time


class TypingTest:

    def __init__(self, expected):
        self.expected = expected
        self.timeStart = time.time()
        self.timeEnd = 0.0
        self.typedText = ""
        self.typingSpeed = 0        # chars per minute

    def getInput(self):
        print(f"{'='*20}\n{self.expected}\n{'='*20}")
        print("Please print the above text: ", end="")
        self.resetTimeStart()
        self.typedText = input()
        self.chars = len(self.typedText)
        self.timeEnd = time.time()

    def resetTimeStart(self):
        self.timeStart = time.time()

    def calculate(self):
        print(f"{self.typingSpeed:.2f}")

    def calculateCorrectness(self):
        diff = difflib.ndiff(self.expected, self.typedText)
        s = ""
        brace = False
        for x in diff:
            if x[0] == " ":
                if brace:
                    s += "]" + x[2]
                    brace = False
                else:
                    s += x[2]
            if x[0] == "-":
                if brace: 
                    s+= x[2]
                else: 
                    s += "[" + x[2]
                    brace = True
        if brace: s += "]"
        print(s)

    def calculateSpeed(self):
        self.typingSpeed = self.chars / (self.timeEnd - self.timeStart) * 60
        

    def __repr__(self):
        return "Expected text:\n" + self.expected + "\nTime start: " + time.strftime("%H:%M:%S", time.localtime(self.timeStart)) + \
               "\nTime End: " + time.strftime("%H:%M:%S", time.localtime(self.timeEnd))


if __name__ == "__main__":
    t = TypingTest("Hello world")
    t.getInput()
    print(t)
    t.calculateCorrectness()
from datastretch.core import Task


class ProcessingTask1(Task):

    def __init__(self):
        # do your init-stuff here
        super().__init__()

    def run(self):
        print("I am processing class 1!")
        self.data = "Data of ProcessingTask1"
        return self.data



class ProcessingTask2(Task):

    def __init__(self):
        # do your init-stuff here
        super().__init__()

    def run(self):
        print("I am processing class 2!")
        self.data = "Data of ProcessingTask2"
        return self.data

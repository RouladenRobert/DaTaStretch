from datastretch.core import Task


class Output(Task):

    def __init__(self):
        # do your init-stuff here
        super().__init__()

    def run(self):
        print("Output: I have received:")
        print(self.processingtask1_data)
        print(self.processingtask2_data)

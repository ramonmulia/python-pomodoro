import threading
from breakTime import BreakEnum
from eventHook import EventHook


class Pomodoro(threading.Thread):
    cicle = 0
    checkmark = 0
    count = 0

    def __init__(self, time, breaktime):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.onFinishSection = EventHook()

        self.breaktype = BreakEnum.SHORT
        self.time = time

    def updateTurn(self):
        self.checkmark = self.checkmark + 1
        auxcheckmark = self.checkmark
        if self.checkmark == 4:
            self.checkmark = 0
            self.cicle = self.cicle + 1

            if self.cicle < 4:
                self.breaktype = BreakEnum.SHORT
            else:
                self.breaktype = BreakEnum.LONG

        self.onFinishSection.fire(auxcheckmark, self.cicle, self.breaktype)

    def run(self):
        print("Running..")
        self.count = self.time
        while self.count > 0 and not self.event.is_set():
            print(self.count)
            self.count -= 1
            self.event.wait(1)

        self.updateTurn()

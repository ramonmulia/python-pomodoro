from enum import Enum
import threading


class BreakEnum(Enum):
    SHORT = 1
    LONG = 2


class BreakTime(threading.Thread):
    def __init__(self, short, long):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.short = short
        self.long = long

    def __getTimeFromEnum(self, breakType):
        if breakType == BreakEnum.SHORT:
            return self.short

        return self.long

    def run(self, breakType):
        print("Running {} seconds of {} break".format(
            self.__getTimeFromEnum(breakType), breakType.name))

        count = 0
        breakTime = self.__getTimeFromEnum(breakType)

        while count < breakTime and not self.event.is_set():
            print('.'*(count+1))

            count += 1
            self.event.wait(1)

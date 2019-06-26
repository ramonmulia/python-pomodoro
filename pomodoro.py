import threading
from breakTime import BreakEnum
from eventHook import EventHook


class Pomodoro(threading.Thread):
    __cicle = 1
    __checkmark = 1
    __time = 10  # seconds
    __max_cicle_to_long_break = 0

    def __init__(self, time, max_checkmark):
        threading.Thread.__init__(self)

        self.__max_checkmark = max_checkmark
        self.__event = threading.Event()
        self.onFinishSection = EventHook()

        self.__time = time

    def updateTurn(self):
        auxcheckmark = self.__checkmark
        auxcicle = self.__cicle

        if self.__checkmark == self.__max_checkmark:
            self.__checkmark = 1
            self.__cicle = self.__cicle + 1
            breaktype = BreakEnum.LONG
        else:
            breaktype = BreakEnum.SHORT
            self.__checkmark = self.__checkmark + 1

        self.onFinishSection.fire(auxcheckmark, auxcicle, breaktype)

    def run(self):
        print('\nPomodoro {}/{} Cicle: {}  \n'.format(self.__checkmark,
                                                    self.__max_checkmark, self.__cicle))
        count = self.__time
        while count > 0 and not self.__event.is_set():
            print(count)
            count -= 1
            self.__event.wait(1)

        self.updateTurn()

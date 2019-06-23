from pomodoro import Pomodoro
from breakTime import BreakTime, BreakEnum
import time

btime = BreakTime(3, 15)
pomodoro = Pomodoro(2, btime)


def startBreak(checkmark, cicle, breakType):
    print(checkmark, cicle, breakType)
    if breakType == BreakEnum.SHORT:
        time.sleep(btime.short)
    else:
        time.sleep(btime.long)

    pomodoro.run()


pomodoro.onFinishSection += startBreak

pomodoro.run()

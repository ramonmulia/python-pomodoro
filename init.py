from pomodoro import Pomodoro
from breakTime import BreakTime, BreakEnum
import time

total_checkmark_to_long_break = 5

btime = BreakTime(3, 15)
pomodoro = Pomodoro(2, total_checkmark_to_long_break)


def startBreak(checkmark, cicle, breakType):
    print('\n--- Time to rest! ---\n')
    btime.run(breakType)
    pomodoro.run()


pomodoro.onFinishSection += startBreak

pomodoro.run()

from enum import Enum


class BreakEnum(Enum):
    SHORT = 1
    LONG = 2


class BreakTime:
    def __init__(self, short, long):
        self.short = short
        self.long = long

    

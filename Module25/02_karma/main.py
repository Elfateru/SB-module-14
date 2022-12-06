from random import randint, choice


class KillError(Exception):
    def __str__(self):
        return 'KillError\n'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError\n'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError\n'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError\n'


class DepressonError(Exception):
    def __str__(self):
        return 'DepressionError\n'


def one_day():
    if randint(1, 10) == 1:
        dice = choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
        if dice == 'KillError':
            return KillError()
        elif dice == 'DrunkError':
            return DrunkError()
        elif dice == 'CarCrashError':
            return CarCrashError()
        elif dice == 'GluttonyError':
            return GluttonyError()
        elif dice == 'DepressionError':
            return DepressonError()
    else:
        return randint(1, 7)


karma = 0
day = 0
while karma < 500:
    day += 1
    res = one_day()
    try:
        karma += res
    except:
        with open('karma.log', 'a', encoding='utf-8') as text:
            text.write(str(day) + ' день ' + res.__str__())

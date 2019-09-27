import random

from colorama import init, Fore

init(autoreset=False)


class Colored(object):
    lasted_randint = None

    @staticmethod
    def red(s):
        return Fore.LIGHTRED_EX + s + Fore.RESET

    @staticmethod
    def green(s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET

    @staticmethod
    def yellow(s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET

    @staticmethod
    def white(s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET

    @staticmethod
    def blue(s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET

    @staticmethod
    def magenta(s):
        return Fore.LIGHTMAGENTA_EX + s + Fore.RESET

    @staticmethod
    def cyan(s):
        return Fore.LIGHTCYAN_EX + s + Fore.RESET

    @staticmethod
    def black(s):
        return Fore.LIGHTBLACK_EX + s + Fore.RESET

    @classmethod
    def random(cls, s):
        randint = random.randint(1, 7)
        if randint == 1:
            result = cls.red(s)
        elif randint == 2:
            result = cls.green(s)
        elif randint == 3:
            result = cls.yellow(s)
        elif randint == 4:
            result = cls.white(s)
        elif randint == 5:
            result = cls.blue(s)
        elif randint == 6:
            result = cls.magenta(s)
        elif randint == 7:
            result = cls.cyan(s)
        else:
            result = cls.black(s)
        if cls.lasted_randint and cls.lasted_randint == randint:
            return cls.random(s)
        cls.lasted_randint = randint
        print(cls.lasted_randint)
        return result


color = Colored()

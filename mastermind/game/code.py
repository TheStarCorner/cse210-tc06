import random
from game.guess import Guess

class Code:
    def __init__(self):
        self._code = random.randint(1000, 9999)
    def is_correct_guess(self, guess):
        return guess.get_guess().get_guess() == self._code
    def check_guess(self, guess):
        string = ""
        string += self._check_thousand(guess.get_guess())
        string += self._check_hundred(guess.get_guess())
        string += self._check_ten(guess.get_guess())
        string += self._check_one(guess.get_guess())
        return string
    def print(self):
        print(self._code)

    def _check_thousand(self, guess):
        a = self._get_thousandth(guess.get_guess()) #a is the number in the thousandths place of guess
        if a == self._get_thousandth(self._code): #if the two thousandth places are the same
            return '\x1b[0;30;42m' + 'X' + '\x1b[0m'
        if a == self._get_hundredth(self._code): #if the thousandth place of guess is equal to the hundreth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        if a == self._get_tenth(self._code): #if the thousandth place of guess is equal to the tenth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        if a == self._get_oneth(self._code): #if the thousandth place of guess is equal to the oneth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        return '\x1b[0;30;41m' + '*' + '\x1b[0m' #if the thousandth place of guess is not equal to anything in the code
    def _check_hundred(self, guess):
        a = self._get_hundredth(guess.get_guess()) #a is the number in the hundredth place of guess
        if a == self._get_hundredth(self._code): #if the two hundredth places are equal
            return '\x1b[0;30;42m' + 'X' + '\x1b[0m'
        if a == self._get_thousandth(self._code): #if the hundreth place in guess is equal to the thousandth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        if a == self._get_tenth(self._code): #if the hundredth place of guess is equal to the tenth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        if a == self._get_oneth(self._code): #if the hundredth place of guess is equal to the oneth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        return '\x1b[0;30;41m' + '*' + '\x1b[0m' #if the hundredth place of guess is not equal to anything in the code
    def _check_ten(self, guess):
        a = self._get_tenth(guess.get_guess()) #a is the number in the tenth place of guess
        if a == self._get_tenth(self._code): #if the two tenth places are equal
            return '\x1b[0;30;42m' + 'X' + '\x1b[0m'
        if a == self._get_thousandth(self._code): #if the tenth place in guess is equal to the thousandth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        if a == self._get_hundredth(self._code): #if the tenth place in guess is equal to the hundredth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        if a == self._get_oneth(self._code): #if the tenth place of guess is equal to the oneth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        return '\x1b[0;30;41m' + '*' + '\x1b[0m' #if the tenth place of guess is not equal to anything in the code
    def _check_one(self, guess):
        a = self._get_oneth(guess.get_guess()) #a is the number in the oneth place of guess
        if a == self._get_oneth(self._code): #if the two tenth places are equal
            return '\x1b[0;30;42m' + 'X' + '\x1b[0m'
        if a == self._get_thousandth(self._code): #if the oneth place in guess is equal to the thousandth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        if a == self._get_hundredth(self._code): #if the oneth place in guess is equal to the hundredth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        if a == self._get_tenth(self._code): #if the oneth place in guess is equal to the tenth place of code
            return '\x1b[0;30;43m' + 'O' + '\x1b[0m'
        return '\x1b[0;30;41m' + '*' + '\x1b[0m' #if the tenth place of guess is not equal to anything in the code
    
    def _get_thousandth(self, num):
        #get the thousandth
        return int(num / 1000)
    def _get_hundredth(self, num):
        return int(num / 100) % 10
    def _get_tenth(self, num):
        return int(num / 10) % 10
    def _get_oneth(self, num):
        return int(num % 10)
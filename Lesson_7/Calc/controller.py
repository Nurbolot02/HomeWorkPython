from Lesson_7.Calc.input_data import init_data
from Lesson_7.Calc.prog import sumNumbers
from Lesson_7.Calc.out import view


def start():
    init_data.init()
    sumAB = sumNumbers(init_data.userInputA, init_data.userInputB)
    view.printResult(init_data.userInputA, init_data.userInputB, sumAB)

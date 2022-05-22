from Lesson_7.Calc.input_data import init_data
from Lesson_7.Calc.prog import mathOperation
from Lesson_7.Calc.out import view


def start():
    init_data.init()
    result = mathOperation.do(init_data.userInput)
    view.printResult(init_data.userInput, result)


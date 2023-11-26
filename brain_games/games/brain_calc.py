import random


RULES = 'What is the result of the expression?'


def generate_question_and_answer():
    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)
    math_operators = ('+', '-', '*')
    math_operator = random.choice(math_operators)
    question = f'{number1} {math_operator} {number2}'
    if math_operator == '+':
        answer = number1 + number2
    elif math_operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return question, str(answer)

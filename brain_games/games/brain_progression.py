import random


RULES = 'What number is missing in the progression?'


def generate_question_and_answer():
    start = random.randint(1, 100)
    difference = random.randint(1, 5)
    length = random.randint(5, 7)
    hiden_index = random.randint(0, length - 1)
    progression = [
        str(start + difference * (i + 1))
        for i in range(length)
    ]
    answer = progression[hiden_index]
    progression[hiden_index] = ".."
    question = " ".join(progression)
    return question, answer

#!/usr/bin/env python3


import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    even_or_not()


def even_or_not():
    name = prompt.string('May I have you name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = 0
    while correct_answer < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        write_answer = prompt.string("Your answer: ")
        if (write_answer == "yes" and number % 2 == 0) or (write_answer == "no" and number % 2 != 0):
            print("Correct!")
            correct_answer += 1
	if correct_answer == 3:
	    print(f"Congratulations, {name}!")
        else:
            print(f"'{write_answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
	    return


if __name__ == '__main__':
    main()

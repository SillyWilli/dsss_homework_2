import random


def rndmInt(min, max):
    """
    Returns a random integer between two given values.

    Input:
        min (int): low boundary
        max (int): high boundary

    Output:
        int: random integer between min and max
    """
    return random.randint(min, max)


def rndmOperator():
    """
    Returns a random math operator

    Input:
        --

    Output:
        str: one of the following operators: +, -, *
    """
    return random.choice(['+', '-', '*'])


def operation(n1, n2, o):
    """
    Performs the operation o with the two numbers n1 and n2 and returns the solution s and the merged operation mo

    Input:
        n1 (int): first number
        n2 (int): second number
        o (str): operator

    Output:
        s (int): solution of the operation
        mo (str): merged operation
    """
    mo = f"{n1} {o} {n2}"
    if o == '-': s = n1 - n2
    elif o == '+': s = n1 + n2
    else: s = n1 * n2
    return mo, s

def math_quiz():
    """
    Executes a math quiz with random math problems with numrounds rounds. Every round one problem has to be solved. 
    The user gets one pont if the answer is correct. At the end the solution is displayed.

    Input:
        --

    Output:
        --
    """
    numpoints = 0
    numrounds = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(numrounds):
        # Numbers and operator for the calculation
        n1 = rndmInt(1, 10); n2 = rndmInt(1, 5); o = rndmOperator()

        # Generate and print the equation
        PROBLEM, ANSWER = operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        # only integeer values are accepted as answer
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except ValueError:
            print("Your solution has to be an integer.")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

        # Plus one point for correct answer
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            numpoints += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {numpoints}/{numrounds}")

if __name__ == "__main__":
    math_quiz()

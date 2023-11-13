import random
import math


def get_random_integer(min, max):
    """
    Return a random integer between given input values (min and max).
    
    Parameters
    ----------
    min: integer 
        The smallest random number that can be returned
        
    max: integer
        The largest random number that can be returned
        
    Returns
    -------
    integer
        A random value produced by the function random.randint()
       
    """
    try: 
        return random.randint(min, max)
    except ValueError: 
        print("Function 'get_random_integer()': input(s) not an integer")


def get_random_math_symbol():
    """
    Return a random mathematical operation symbol.
    
    Parameters
    ----------
    None
        
    Returns
    -------
    string
        A random element from a list of mathematical operation symbols.
       
    """
    return random.choice(['+', '-', '*'])


def plus_minus_multiplication(n1, n2, o):
    """
    Return a integer value after executing a defined mathematical operation on two given 
    values.
    The following symbols/operations are accepted:
    '+': addition
    '-': subtraction
    '*': multiplication
    
    Parameters
    ----------
    n1: integer
        first value 
    n2: integer
        second value
    o: 
        mathematical operation symbol
        
    Returns
    -------
    p: string
        prints the mathematical equation
    a: integer
        An value resulted from the execution of a defined mathematical operation on two 
        input integers
    """
       
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = math.ceil(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # how many questions in a quiz game  
    for _ in range(t_q):
        n1 = get_random_integer(1, 10); n2 = get_random_integer(1, 5); o = get_random_math_symbol()

        PROBLEM, ANSWER = plus_minus_multiplication(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()

import random, sys
random.seed(658)  # Ensures reproducibility
sys.setrecursionlimit(1000000)

def foo(counter=0, history=None):
    """Generates random numbers until we get a 50"""
    if history is None:
        history = []

    # Track how many calls we've made
    counter += 1

    random_number = random.randint(1, 100)
    history.append(random_number)

    if random_number == 50:
        print(f"Blank 1 (counter when first return executes): {counter}")

        if len(history) >= 2:
            print(f"Blank 2 (random_number one call before 50): {history[-2]}")
        if len(history) >= 4:
            print(f"Blank 3 (random_number three calls before 50): {history[-4]}")

        return
    
    foo(counter, history)

foo()
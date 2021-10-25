from random import randint

def gen_random(amount, minimal, maximum):
    for _ in range(amount):
        yield randint(minimal, maximum)

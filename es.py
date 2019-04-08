import math
import random
import numpy as np


file_name = "model5.txt"

N = 101


def model_function(i, a, b, c):
    return a*(i * i - b * math.cos(c* 3.14 * i))


def init_population():
    #return random.randint(-10, 10)
    return np.random.uniform(-10, 10), np.random.uniform(-10, 10), np.random.uniform(-10, 10)

def mean_square_error(values_expected, values_obtained):
    E = 0
    for i in range(0, len(values_expected)):
        E = E + (values_expected - values_obtained) ** 2
    E = E / len(values_obtained)
    return E


def evaluate(a, b, c):
    return True

def alter(params):


def select(params):
    best = 0


def procedure_ea():
    t = 0
    #termination_condition = False
    params = init_population()
    best = None
    termination_condition = evaluate(params)
    while not termination_condition:
        t = t + 1
        best = select(params)
        alter(params)
        termination_condition = evaluate(best)


procedure_ea()



import math


file_name = "model5.txt"

N = 101


def model_function(i, a, b, c):
    return a*(i * i - b * math.cos(c* 3.14 * i))


def init_population():


def mean_square_error(values_expected, values_obtained):
    E = 0
    for i in range(0, len(values_expected)):
        E = E + (values_expected - values_obtained) ** 2
    E = E / len(values_obtained)
    return E


def procedure_ea():
    t = 0
    termination_condition = False
    init_population()



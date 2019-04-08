import math


file_name = "model5.txt"

N = 101


def model_function(i, a, b, c):
    return a*(i * i - b * math.cos(c* 3.14 * i))


def init_population():



def procedure_ea():
    t = 0
    termination_condition = False
    init_population()



import random


def get_random_num():
    all_num = 30
    num = 9
    result = random.sample(range(1,all_num),num)
    return result
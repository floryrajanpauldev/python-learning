
# Lesson: Function Return Values

import math


def slices_needed(guests):
    return guests * 2


def pizzas_needed(slices):
    return math.ceil(slices / 8)


slices = slices_needed(10)
pizzas = pizzas_needed(slices)

print(pizzas)

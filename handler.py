
import re
from sys import prefix
from estimation import Complexity

def count_func(prediction:  dict, key: str):
    count = 0
    for i in prediction:
        if i['tagName'] == key and i['probability'] > 0.97:
            count += 1
    return count

def count_funct(prediction:  dict, key: str):
    count = 0
    for i in prediction:
        if i['tagName'] == key and i['probability'] > 0.85:
            count += 1
    return count

def find_complexity(usecase):
    if usecase < 4:
        return Complexity.SIMPLE
    elif usecase < 7:
        return Complexity.AVERAGE
    else:
        return Complexity.COMPLEX        
    
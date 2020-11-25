from random import randint

def random_item (list):
    length = len(list)
    index = randint(0, length -1)

    return list[index]

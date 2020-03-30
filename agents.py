from random import randrange

"""Using reservoir sampling (alghoritm) to retrieve a random user-agent from the text file - without loading the whole file into memory."""


def get_random_line(file, default=None):

    line = default
    for i, dummy_line in enumerate(file, start=1):
        if randrange(i) == 0:  # random int [0..i)
            line = dummy_line
    return line

with open('user_agents.txt') as f:
    agent = get_random_line(f)
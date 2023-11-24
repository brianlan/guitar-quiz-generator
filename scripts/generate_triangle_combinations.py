import argparse
import itertools
import random
import numpy as np

class Triangle:
    STATES = ['xoo', 'oxo', 'oox', 'xxo', 'xox', 'oxx']

def generate_states(n):
    return list(itertools.product(Triangle.STATES, repeat=n))

def main(args):
    all_states = generate_states(args.number_of_triangles)
    if args.shuffle:
        random.shuffle(all_states)

    if args.head:
        all_states = all_states[:args.head]

    for state in all_states:
        print(' '.join(state * args.repeat))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate all possible states combinations of triangles')
    parser.add_argument('--number-of-triangles', type=int, help='Number of triangles')
    parser.add_argument('--shuffle', action='store_true', help='Shuffle the states')
    parser.add_argument('--head', type=int, help='Number of states to print')
    parser.add_argument('--repeat', type=int, help='Repeat the states')
    main(parser.parse_args())
import argparse
import sched
import time
import random
import signal
import sys
from easydict import EasyDict as edict

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-up", type=int, default=10, help="time up in seconds for each quiz")
    parser.add_argument("--flat", action="store_true", default=False)
    return edict({k: v for k, v in parser.parse_args()._get_kwargs()})


args = parse_arguments()


def generate_output():
    note_pool = ["1", "2", "3", "4", "5", "6", "7"]
    if args.flat:
        note_pool += ["b2", "b3", "b5", "b6", "b7"]
    while True:
        # finger = random.choice([1, 2, 4])
        string = random.randint(2, 5)
        fret = random.randint(3, 12)
        number1 = random.choice(note_pool)
        direction = random.choice(['up', 'down'])
        number2 = random.choice(note_pool)
        if number1 != number2:
            break
    print(f"{number1} {direction} {number2}")
        # print(f"[{string},{fret}] : {number1} {direction} {number2}")

def sigterm_handler(signum, frame):
    print("Received SIGTERM signal. Terminating the program gracefully.")
    sys.exit(0)

def main():
    signal.signal(signal.SIGTERM, sigterm_handler)

    scheduler = sched.scheduler(time.time, time.sleep)

    def schedule_next_run():
        scheduler.enter(args.time_up, 1, generate_output)
        scheduler.enter(args.time_up, 2, schedule_next_run)

    schedule_next_run()

    scheduler.run()

if __name__ == '__main__':
    main()


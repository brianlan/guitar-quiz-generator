import argparse
import sched
import time
import random
import signal
import sys

def generate_output():
    while True:
        # finger = random.choice([1, 2, 4])
        string = random.randint(2, 5)
        fret = random.randint(3, 12)
        number1 = random.randint(1, 7)
        direction = random.choice(['up', 'down'])
        number2 = random.randint(1, 7)
        if number1 != number2:
            break
    print(f"{number1} {direction} {number2}")
        # print(f"[{string},{fret}] : {number1} {direction} {number2}")

def sigterm_handler(signum, frame):
    print("Received SIGTERM signal. Terminating the program gracefully.")
    sys.exit(0)

def main(args):
    signal.signal(signal.SIGTERM, sigterm_handler)

    scheduler = sched.scheduler(time.time, time.sleep)

    def schedule_next_run():
        scheduler.enter(args.time_up, 1, generate_output)
        scheduler.enter(args.time_up, 2, schedule_next_run)

    schedule_next_run()

    scheduler.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-up", type=int, default=10, help="time up in seconds for each quiz")
    main(parser.parse_args())

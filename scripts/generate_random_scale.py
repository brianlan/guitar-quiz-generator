import argparse
from collections import defaultdict
from pathlib import Path
import time

import pandas as pd
import numpy as np
from loguru import logger


directions = ["UP", "DOWN"]
scales = ["Major", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Minor", "Locrian", "Harmonic Minor", "Melodic Minor"]
fingers = [1, 2, 4]

def main(args):
    logger.info("Generating random scale")
    i = 0
    scales_practiced = []
    while True:
        try:
            direction = directions[i % 2]
            scale = np.random.choice(scales)
            finger = np.random.choice(fingers)
            logger.info(f"{direction:<4} F{finger} {scale}")
            time.sleep(args.sleep_time)
            i += 1
            scales_practiced.append((direction, scale, finger))
        except KeyboardInterrupt:
            logger.info("Exiting")
            stats = pd.DataFrame(scales_practiced, columns=["direction", "scale", "finger"])
            summary = stats.groupby(["scale", "finger", "direction"]).size()
            logger.info(f"Stats - total scales practiced: {i + 1}\n{summary}")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--sleep-time', type=int, default=10)
    main(parser.parse_args())

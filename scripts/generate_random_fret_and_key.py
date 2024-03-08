import argparse
from pathlib import Path

import numpy as np
from loguru import logger


def main(args):
    keys = ["C", "D", "E", "F", "G", "A", "B", "Bb", "Eb", "Ab", "Db", "Gb"]
    frets = list(range(1, 13))
    random_keys = np.random.choice(keys, 6, replace=False)
    logger.info(f"random_keys: {random_keys}")
    random_frets = np.random.choice(frets, 6, replace=False)
    logger.info(f"random_frets: {random_frets}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    main(parser.parse_args())

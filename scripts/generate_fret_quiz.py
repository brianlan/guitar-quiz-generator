import argparse
from pathlib import Path

from loguru import logger


parser = argparse.ArgumentParser()
parser.add_argument("--output-path", type=Path, default=Path("fret_quiz.txt"))
parser.add_argument("--scale-display-method", type=str, default="number", choices=["number", "mode_scale"])
parser.add_argument("--display-answers", action="store_true", default=False)


finger_types = [1, 2, 4]
root_types = [6, 5, 4]
modal_scales = ["Major", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]

answers = {
    6: {
        1: ["C", "D", "E", "F", "G", "A", "B"],
        2: ["B", "C", "D", "E", "F", "G", "A"],
        4: ["A", "B", "C", "D", "E", "F", "G"]
    },
    5: {
        1: ["G", "A", "B", "C", "D", "E", "F"],
        2: ["F", "G", "A", "B", "C", "D", "E"],
        4: ["E", "F", "G", "A", "B", "C", "D"]
    },
    4: {
        1: ["D", "E", "F", "G", "A", "B", "C"],
        2: ["C", "D", "E", "F", "G", "A", "B"],
        4: ["B", "C", "D", "E", "F", "G", "A"],
    },
}
def main(args):
    quiz = []
    for finger in finger_types:
        for root in root_types:
            for scale in modal_scales:
                scale_number = modal_scales.index(scale) + 1
                if args.scale_display_method == "number":
                    q = f"{scale_number}-R{root}F{finger}"
                else:
                    q = f"{scale}-R{root}F{finger}"
                if args.display_answers:
                    q += f" {answers[root][finger][scale_number - 1]}"
                quiz.append(q)
    
    # shuffle the quiz
    import random
    random.shuffle(quiz)

    # write the quiz
    with open(args.output_path, "w") as f:
        for q in quiz:
            f.write(f"{q}\n")


if __name__ == "__main__":
    main(parser.parse_args())

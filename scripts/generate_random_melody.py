import argparse
import random
from typing import List, Tuple
from pathlib import Path

from loguru import logger

from guitar.base_structure import Note, Pitch, Duration, NoteEvent, RestEvent, Chord, Interval, ScaleType, Scale


def main(args):
    # random_melody = generate_random_melody(4, 120)
    # for event in random_melody:
    #     print(event)
    
    melody, chords = generate_music()
    print("Melody:")
    for event in melody:
        print(event)

    print("\nChords:")
    for chord in chords:
        print(chord)



class MusicGenerator:
    def __init__(self, measures: int, beats_per_measure: int):
        self.measures = measures
        self.beats_per_measure = beats_per_measure

    def generate_melody(self, scale_notes: list[Note]) -> list[NoteEvent | RestEvent]:
        melody = []
        for _ in range(self.measures * self.beats_per_measure):
            if random.random() < 0.8:  # 80% chance of generating a note
                note = random.choice(scale_notes)
                duration = random.choice(list(Duration))
                melody.append(NoteEvent(note, duration))
            else:  # 20% chance of generating a rest
                duration = random.choice(list(Duration))
                melody.append(RestEvent(duration))
        return melody

    def generate_chords(self, scale_notes: list[Note]) -> list[Chord]:
        chords = []
        for _ in range(self.measures):
            root_note = random.choice(scale_notes)
            intervals = random.sample([Interval.MAJOR_THIRD, Interval.MINOR_THIRD, Interval.PERFECT_FIFTH], 2)
            duration = Duration.WHOLE_NOTE
            inversion = random.randint(0, 1)  # 0 or 1 inversion
            chord = Chord(root_note, intervals, duration, inversion)
            chords.append(chord)
        return chords

def generate_music(measures: int = 4, beats_per_measure: int = 4) -> Tuple[list[NoteEvent | RestEvent], list[Chord]]:
    # Pick a random key and scale
    root_note = Note(random.choice(list(Pitch)), random.randint(3, 5))
    scale_type = random.choice(list(ScaleType))
    scale = Scale(root_note, scale_type)
    scale_notes = scale.get_notes()

    # Generate melody and chords
    generator = MusicGenerator(measures, beats_per_measure)
    melody = generator.generate_melody(scale_notes)
    chords = generator.generate_chords(scale_notes)

    return melody, chords




# def generate_random_melody(num_measures: int = 4, tempo: int = 120) -> List[NoteEvent | RestEvent]:
#     melody: List[NoteEvent | RestEvent] = []
#     current_duration = 0

#     while current_duration < num_measures * 4:  # Assuming 4/4 time signature
#         if current_duration % 4 == 0:
#             # Ensure a note event at the beginning of each measure
#             note = generate_random_note()
#             duration = random.choice([Duration.WHOLE_NOTE, Duration.HALF_NOTE, Duration.QUARTER_NOTE])
#             melody.append(NoteEvent(note, duration))
#         else:
#             # Randomly choose between a note event and a rest event
#             if random.random() < 0.8:  # 80% chance of a note event
#                 note = generate_random_note()
#                 duration = random.choice([Duration.HALF_NOTE, Duration.QUARTER_NOTE, Duration.EIGHTH_NOTE])
#                 melody.append(NoteEvent(note, duration))
#             else:  # 20% chance of a rest event
#                 duration = random.choice([Duration.HALF_NOTE, Duration.QUARTER_NOTE, Duration.EIGHTH_NOTE])
#                 melody.append(RestEvent(duration))

#         current_duration += duration.value

#     return melody


# def generate_random_note() -> Note:
#     pitch = random.choice(list(Pitch))
#     octave = random.randint(3, 5)  # Limit octave range for a more pleasant melody
#     return Note(pitch, octave)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    main(parser.parse_args())

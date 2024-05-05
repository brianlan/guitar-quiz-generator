from dataclasses import dataclass
from typing import Tuple, List
from enum import Enum


class Pitch(Enum):
    C = 0
    C_SHARP = 1
    D_FLAT = 1
    D = 2
    D_SHARP = 3
    E_FLAT = 3
    E = 4
    E_SHARP = 5
    F = 5
    F_SHARP = 6
    G_FLAT = 6
    G = 7
    G_SHARP = 8
    A_FLAT = 8
    A = 9
    A_SHARP = 10
    B_FLAT = 10
    B = 11


class Interval(Enum):
    UNISON = 0
    MINOR_SECOND = 1
    MAJOR_SECOND = 2
    MINOR_THIRD = 3
    MAJOR_THIRD = 4
    PERFECT_FOURTH = 5
    DIMINISHED_FIFTH = 6
    PERFECT_FIFTH = 7
    MINOR_SIXTH = 8
    MAJOR_SIXTH = 9
    MINOR_SEVENTH = 10
    MAJOR_SEVENTH = 11
    OCTAVE = 12
    MAJOR_NINTH = 14
    PERFECT_ELEVENTH = 17
    MAJOR_THIRTEENTH = 21


class Duration(Enum):
    WHOLE_NOTE = 4.0
    HALF_NOTE = 2.0
    QUARTER_NOTE = 1.0
    EIGHTH_NOTE = 0.5
    SIXTEENTH_NOTE = 0.25


@dataclass
class Note:
    pitch: Pitch
    octave: int

    def __repr__(self) -> str:
        return f"{self.pitch.name}{self.octave}"


@dataclass
class NoteEvent:
    note: Note
    duration: Duration

    def __repr__(self):
        return f"{self.note}({self.duration.name})"


@dataclass
class RestEvent:
    duration: Duration

    def __repr__(self):
        return f"Rest({self.duration.name})"


class Chord:
    def __init__(self, root_note: Note, intervals: list[Interval], duration: float, inversion: int = 0):
        self.root_note = root_note
        self.intervals = intervals
        self.duration = duration

        max_inversion = len(intervals)
        if inversion < 0 or inversion > max_inversion:
            raise ValueError(f"Invalid inversion value. Must be between 0 and {max_inversion}.")
        self.inversion = inversion

    def __repr__(self):
        chord_name = f"{self.root_note} {'-'.join([i.name for i in self.intervals])}"
        if self.inversion > 0:
            chord_name += f" (inversion {self.inversion})"
        return chord_name

    def get_notes(self) -> list[Note]:
        notes = []
        for interval in self.intervals:
            pitch = (self.root_note.pitch.value + interval.value) % 12
            octave = self.root_note.octave + (self.root_note.pitch.value + interval.value) // 12
            notes.append(Note(Pitch(pitch), octave))

        # Adjust octaves for inverted notes
        for i in range(len(notes)):
            if i < self.inversion:
                notes[i] = Note(notes[i].pitch, notes[i].octave + 1)

        inverted_notes = notes[self.inversion :] + notes[: self.inversion]

        return inverted_notes


class ScaleType(Enum):
    MAJOR = [
        Interval.UNISON,
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.PERFECT_FOURTH,
        Interval.PERFECT_FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH,
    ]
    NATURAL_MINOR = [
        Interval.UNISON,
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.PERFECT_FOURTH,
        Interval.PERFECT_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH,
    ]
    HARMONIC_MINOR = [
        Interval.UNISON,
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.PERFECT_FOURTH,
        Interval.PERFECT_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SEVENTH,
    ]
    MELODIC_MINOR_ASCENDING = [
        Interval.UNISON,
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.PERFECT_FOURTH,
        Interval.PERFECT_FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH,
    ]
    MELODIC_MINOR_DESCENDING = [
        Interval.UNISON,
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.PERFECT_FOURTH,
        Interval.PERFECT_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH,
    ]


class Scale:
    def __init__(self, root_note: Note, scale_type: ScaleType):
        self.root_note = root_note
        self.scale_type = scale_type

    def __repr__(self):
        return f"{self.root_note} {self.scale_type.name}"

    def get_notes(self) -> list[Note]:
        notes = [self.root_note]
        for interval in self.scale_type.value[1:]:
            pitch_value = (self.root_note.pitch.value + interval.value) % 12
            pitch = Pitch(pitch_value)
            octave = self.root_note.octave + (self.root_note.pitch.value + interval.value) // 12
            notes.append(Note(pitch, octave))
        return notes

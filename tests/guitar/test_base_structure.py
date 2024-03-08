from guitar.base_structure import Chord, Note, Pitch, Interval, Scale, ScaleType, RestEvent, Duration

import pytest


def test_chord_creation():
    c_major_chord = Chord(Note(Pitch.C, 4), [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH], 1.0)
    assert c_major_chord.root_note == Note(Pitch.C, 4)
    assert c_major_chord.intervals == [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH]
    assert c_major_chord.duration == 1.0
    assert c_major_chord.inversion == 0


def test_chord_str_representation():
    c_major_chord = Chord(Note(Pitch.C, 4), [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH], 1.0)
    assert str(c_major_chord) == "C4 UNISON-MAJOR_THIRD-PERFECT_FIFTH"

    c_major_first_inversion = Chord(
        Note(Pitch.C, 4), [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH], 1.0, inversion=1
    )
    assert str(c_major_first_inversion) == "C4 UNISON-MAJOR_THIRD-PERFECT_FIFTH (inversion 1)"


def test_chord_get_notes():
    c_major_chord = Chord(Note(Pitch.C, 4), [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH], 1.0)
    assert c_major_chord.get_notes() == [Note(Pitch.C, 4), Note(Pitch.E, 4), Note(Pitch.G, 4)]

    c_major_first_inversion = Chord(
        Note(Pitch.C, 4), [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH], 1.0, inversion=1
    )
    assert c_major_first_inversion.get_notes() == [Note(Pitch.E, 4), Note(Pitch.G, 4), Note(Pitch.C, 5)]


def test_chord_get_notes_seven_chord():
    c_major_seven_chord = Chord(
        Note(Pitch.C, 4), [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH], 1.0
    )
    assert c_major_seven_chord.get_notes() == [Note(Pitch.C, 4), Note(Pitch.E, 4), Note(Pitch.G, 4), Note(Pitch.B, 4)]

    c_major_seven_first_inversion = Chord(
        Note(Pitch.C, 4),
        [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH],
        1.0,
        inversion=1,
    )
    assert c_major_seven_first_inversion.get_notes() == [
        Note(Pitch.E, 4),
        Note(Pitch.G, 4),
        Note(Pitch.B, 4),
        Note(Pitch.C, 5),
    ]

    c_major_seven_second_inversion = Chord(
        Note(Pitch.C, 4),
        [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH],
        1.0,
        inversion=2,
    )
    assert c_major_seven_second_inversion.get_notes() == [
        Note(Pitch.G, 4),
        Note(Pitch.B, 4),
        Note(Pitch.C, 5),
        Note(Pitch.E, 5),
    ]

    c_major_seven_third_inversion = Chord(
        Note(Pitch.C, 4),
        [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH],
        1.0,
        inversion=3,
    )
    assert c_major_seven_third_inversion.get_notes() == [
        Note(Pitch.B, 4),
        Note(Pitch.C, 5),
        Note(Pitch.E, 5),
        Note(Pitch.G, 5),
    ]


def test_chord_get_notes_nine_chord():
    c_major_nine_chord = Chord(
        Note(Pitch.C, 4),
        [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH, Interval.MAJOR_NINTH],
        1.0,
    )
    assert c_major_nine_chord.get_notes() == [
        Note(Pitch.C, 4),
        Note(Pitch.E, 4),
        Note(Pitch.G, 4),
        Note(Pitch.B, 4),
        Note(Pitch.D, 5),
    ]

    c_major_nine_first_inversion = Chord(
        Note(Pitch.C, 4),
        [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH, Interval.MAJOR_NINTH],
        1.0,
        inversion=1,
    )
    assert c_major_nine_first_inversion.get_notes() == [
        Note(Pitch.E, 4),
        Note(Pitch.G, 4),
        Note(Pitch.B, 4),
        Note(Pitch.D, 5),
        Note(Pitch.C, 5),
    ]

    c_major_nine_second_inversion = Chord(
        Note(Pitch.C, 4),
        [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH, Interval.MAJOR_NINTH],
        1.0,
        inversion=2,
    )
    assert c_major_nine_second_inversion.get_notes() == [
        Note(Pitch.G, 4),
        Note(Pitch.B, 4),
        Note(Pitch.D, 5),
        Note(Pitch.C, 5),
        Note(Pitch.E, 5),
    ]

    c_major_nine_third_inversion = Chord(
        Note(Pitch.C, 4),
        [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH, Interval.MAJOR_NINTH],
        1.0,
        inversion=3,
    )
    assert c_major_nine_third_inversion.get_notes() == [
        Note(Pitch.B, 4),
        Note(Pitch.D, 5),
        Note(Pitch.C, 5),
        Note(Pitch.E, 5),
        Note(Pitch.G, 5),
    ]

    c_major_nine_fourth_inversion = Chord(
        Note(Pitch.C, 4),
        [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH, Interval.MAJOR_SEVENTH, Interval.MAJOR_NINTH],
        1.0,
        inversion=4,
    )
    assert c_major_nine_fourth_inversion.get_notes() == [
        Note(Pitch.D, 5),
        Note(Pitch.C, 5),
        Note(Pitch.E, 5),
        Note(Pitch.G, 5),
        Note(Pitch.B, 5),
    ]


def test_chord_get_notes_thirteenth_chord():
    c_major_thirteenth_chord = Chord(
        Note(Pitch.C, 4),
        [
            Interval.UNISON,
            Interval.MAJOR_THIRD,
            Interval.PERFECT_FIFTH,
            Interval.MAJOR_SEVENTH,
            Interval.MAJOR_NINTH,
            Interval.PERFECT_ELEVENTH,
            Interval.MAJOR_THIRTEENTH,
        ],
        1.0,
    )
    assert c_major_thirteenth_chord.get_notes() == [
        Note(Pitch.C, 4),
        Note(Pitch.E, 4),
        Note(Pitch.G, 4),
        Note(Pitch.B, 4),
        Note(Pitch.D, 5),
        Note(Pitch.F, 5),
        Note(Pitch.A, 5),
    ]

    c_major_thirteenth_first_inversion = Chord(
        Note(Pitch.C, 4),
        [
            Interval.UNISON,
            Interval.MAJOR_THIRD,
            Interval.PERFECT_FIFTH,
            Interval.MAJOR_SEVENTH,
            Interval.MAJOR_NINTH,
            Interval.PERFECT_ELEVENTH,
            Interval.MAJOR_THIRTEENTH,
        ],
        1.0,
        inversion=1,
    )
    assert c_major_thirteenth_first_inversion.get_notes() == [
        Note(Pitch.E, 4),
        Note(Pitch.G, 4),
        Note(Pitch.B, 4),
        Note(Pitch.D, 5),
        Note(Pitch.F, 5),
        Note(Pitch.A, 5),
        Note(Pitch.C, 5),
    ]

    c_major_thirteenth_second_inversion = Chord(
        Note(Pitch.C, 4),
        [
            Interval.UNISON,
            Interval.MAJOR_THIRD,
            Interval.PERFECT_FIFTH,
            Interval.MAJOR_SEVENTH,
            Interval.MAJOR_NINTH,
            Interval.PERFECT_ELEVENTH,
            Interval.MAJOR_THIRTEENTH,
        ],
        1.0,
        inversion=2,
    )
    assert c_major_thirteenth_second_inversion.get_notes() == [
        Note(Pitch.G, 4),
        Note(Pitch.B, 4),
        Note(Pitch.D, 5),
        Note(Pitch.F, 5),
        Note(Pitch.A, 5),
        Note(Pitch.C, 5),
        Note(Pitch.E, 5),
    ]

    c_major_thirteenth_third_inversion = Chord(
        Note(Pitch.C, 4),
        [
            Interval.UNISON,
            Interval.MAJOR_THIRD,
            Interval.PERFECT_FIFTH,
            Interval.MAJOR_SEVENTH,
            Interval.MAJOR_NINTH,
            Interval.PERFECT_ELEVENTH,
            Interval.MAJOR_THIRTEENTH,
        ],
        1.0,
        inversion=3,
    )
    assert c_major_thirteenth_third_inversion.get_notes() == [
        Note(Pitch.B, 4),
        Note(Pitch.D, 5),
        Note(Pitch.F, 5),
        Note(Pitch.A, 5),
        Note(Pitch.C, 5),
        Note(Pitch.E, 5),
        Note(Pitch.G, 5),
    ]


def test_chord_get_notes_sus4_chord():
    c_sus4_chord = Chord(Note(Pitch.C, 4), [Interval.UNISON, Interval.PERFECT_FOURTH, Interval.PERFECT_FIFTH], 1.0)
    assert c_sus4_chord.get_notes() == [Note(Pitch.C, 4), Note(Pitch.F, 4), Note(Pitch.G, 4)]

    c_sus4_first_inversion = Chord(
        Note(Pitch.C, 4), [Interval.UNISON, Interval.PERFECT_FOURTH, Interval.PERFECT_FIFTH], 1.0, inversion=1
    )
    assert c_sus4_first_inversion.get_notes() == [Note(Pitch.F, 4), Note(Pitch.G, 4), Note(Pitch.C, 5)]

    c_sus4_second_inversion = Chord(
        Note(Pitch.C, 4), [Interval.UNISON, Interval.PERFECT_FOURTH, Interval.PERFECT_FIFTH], 1.0, inversion=2
    )
    assert c_sus4_second_inversion.get_notes() == [Note(Pitch.G, 4), Note(Pitch.C, 5), Note(Pitch.F, 5)]


def test_chord_invalid_inversion():
    with pytest.raises(ValueError):
        Chord(Note(Pitch.C, 4), [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH], 1.0, inversion=-1)

    with pytest.raises(ValueError):
        Chord(Note(Pitch.C, 4), [Interval.UNISON, Interval.MAJOR_THIRD, Interval.PERFECT_FIFTH], 1.0, inversion=4)

def test_rest_event_creation():
    quarter_rest = RestEvent(Duration.QUARTER_NOTE)
    assert quarter_rest.duration == Duration.QUARTER_NOTE

def test_rest_event_repr():
    quarter_rest = RestEvent(Duration.QUARTER_NOTE)
    assert repr(quarter_rest) == "Rest(QUARTER_NOTE)"

def test_scale_creation():
    c_major_scale = Scale(Note(Pitch.C, 4), ScaleType.MAJOR)
    assert c_major_scale.root_note == Note(Pitch.C, 4)
    assert c_major_scale.scale_type == ScaleType.MAJOR

def test_scale_repr():
    c_major_scale = Scale(Note(Pitch.C, 4), ScaleType.MAJOR)
    assert repr(c_major_scale) == "C4 MAJOR"

def test_scale_get_notes():
    c_major_scale = Scale(Note(Pitch.C, 4), ScaleType.MAJOR)
    notes = c_major_scale.get_notes()
    expected_notes = [
        Note(Pitch.C, 4),
        Note(Pitch.D, 4),
        Note(Pitch.E, 4),
        Note(Pitch.F, 4),
        Note(Pitch.G, 4),
        Note(Pitch.A, 4),
        Note(Pitch.B, 4)
    ]
    assert notes == expected_notes

def test_scale_get_notes_different_octaves():
    c_major_scale = Scale(Note(Pitch.G, 4), ScaleType.MAJOR)
    notes = c_major_scale.get_notes()
    expected_notes = [
        Note(Pitch.G, 4),
        Note(Pitch.A, 4),
        Note(Pitch.B, 4),
        Note(Pitch.C, 5),
        Note(Pitch.D, 5),
        Note(Pitch.E, 5),
        Note(Pitch.F_SHARP, 5)
    ]
    assert notes == expected_notes


def test_scale_get_notes_natural_minor():
    a_natural_minor_scale = Scale(Note(Pitch.A, 4), ScaleType.NATURAL_MINOR)
    notes = a_natural_minor_scale.get_notes()
    expected_notes = [
        Note(Pitch.A, 4),
        Note(Pitch.B, 4),
        Note(Pitch.C, 5),
        Note(Pitch.D, 5),
        Note(Pitch.E, 5),
        Note(Pitch.F, 5),
        Note(Pitch.G, 5)
    ]
    assert notes == expected_notes

def test_scale_get_notes_harmonic_minor():
    a_harmonic_minor_scale = Scale(Note(Pitch.A, 4), ScaleType.HARMONIC_MINOR)
    notes = a_harmonic_minor_scale.get_notes()
    expected_notes = [
        Note(Pitch.A, 4),
        Note(Pitch.B, 4),
        Note(Pitch.C, 5),
        Note(Pitch.D, 5),
        Note(Pitch.E, 5),
        Note(Pitch.F, 5),
        Note(Pitch.G_SHARP, 5)
    ]
    assert notes == expected_notes

def test_scale_get_notes_harmonic_minor_different_octaves():
    f_sharp_harmonic_minor_scale = Scale(Note(Pitch.F_SHARP, 4), ScaleType.HARMONIC_MINOR)
    notes = f_sharp_harmonic_minor_scale.get_notes()
    expected_notes = [
        Note(Pitch.F_SHARP, 4),
        Note(Pitch.G_SHARP, 4),
        Note(Pitch.A, 4),
        Note(Pitch.B, 4),
        Note(Pitch.C_SHARP, 5),
        Note(Pitch.D, 5),
        Note(Pitch.E_SHARP, 5)
    ]
    assert notes == expected_notes

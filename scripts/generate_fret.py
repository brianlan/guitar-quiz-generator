# Define the open string notes for a standard-tuned 6-string guitar
open_strings = ['E', 'A', 'D', 'G', 'B', 'E']

# Reverse the order of the open strings
open_strings.reverse()

# Define the number of frets on the guitar neck
num_frets = 16  # You can adjust this number based on your requirements

# Initialize the fretboard as a list of lists
fretboard = [[] for _ in range(6)]

# Define the order of notes
note_order = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
# note_order = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

# Populate the fretboard with notes for each fret
for string_num, open_note in enumerate(open_strings):
    current_note = open_note
    for _ in range(num_frets):
        fretboard[string_num].append(current_note)
        
        # Get the index of the current note in the note order
        note_index = note_order.index(current_note)
        
        # Move to the next note in the note order (cycling back to 'A' after 'G#')
        current_note = note_order[(note_index + 1) % len(note_order)]

# Print the fretboard
for string_notes in fretboard:
    print(string_notes)

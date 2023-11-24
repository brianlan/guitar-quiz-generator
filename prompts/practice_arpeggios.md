I want you to generate a all in one html file with javascript that implements a tool for me to practice and memorize arpeggios in guitar. Below are the requirements.

- All we play is on a 6 by 6 grid indicating the fret of the guitar. 
- we have some predefined chrod type with corresponding arpeggios
- an arpeggio always starts with root note 1 and ends with 1 of either a higher octave or a lower octave, for example: [1, b3, b5, b7, 1] when playing upwards, and [1, b7, b5, b3, 1] when playing downwards.
- this is the order of notes: [1, b2, 3, b3, 4, b5, 5, b6, 6, b7, 7, 1, ...], and the next note is always one position right to the previous note on fret, or we say the distance between a note and its adjacent note is 0.5.
- there're 6 strings (or rows of the grid) on the fret, the distance between grid[5][j] and grid[4][j] is 2.5, the distance between grid[4][j] and grid[3][j] is 2.5, the distance between grid[3][j] and grid[2][j] is 2.5, the distance between grid[2][j] and grid[1][j] is 2, and the distance between grid[1][j] and grid[0][j] is 2.5.
- For example, the distance between 1 and 3 is 2. If 1 is at grid[5][1], 3 could possibly be at grid[4][0](move 1 string higher means +2.5, move left means -0.5 ) and grid[5][5](move 4 position to the right means 0.5 * 4 = 2).
- Each test round, 
  1. you clear the existing grid
  2. create a quiz for the user by:
     2.1 randomly select a chord type
     2.2 randomly select a direction (either upward or downward)
     2.3 randomly select a position in this grid as the starting point, i.e. root note of a chord.
  3. next the user will try to complete (by mouse click on button) the rest of the arpeggio. 
  4. For example, you randomly selected grid[5][2] as the root note 1, then the user should click grid[4][1], grid[4][4], grid[3][3] and grid[3][4] in order (representing 3, 5, 7, 1 repectively).
  5. No matter the user did it right or wrong, move to the next round by repeating all the step of a round.

Here are some predefined arpeggios for your reference:
```
chord_types = {
    'major 7': ['1', '3', '5', '7', '1'],
    'minor 7': ['1', 'b3', '5', 'b7', '1'],
    'dominant 7': ['1', '3', '5', 'b7', '1'],
    'half diminished 7': ['1', 'b3', 'b5', 'b7', '1'],
}
```

---
After you randomly selected a starting position, you should derive the rest of the notes' position in the grid according to the chord type and the direction. A sequence of notes (exactly 5) is considered a quiz. You then need to show the first note of the quiz as "1" on the button grid, and then let the user to complete rest of them by clicking, if the position is correct, you show the note on the clicked button, otherwise, let the user know it's wrong.


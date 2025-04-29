I want to create a web app that help people to practice music intervals on guitar. The app should include the following features:
1. show buttons that represents a guitar fretboard: 6 rows and 12 columns (denoting 6 strings and 12 frets).
2. the program randomly select two positions on the fretboard, and for one of them, we render it as yellow, and for the other, we render it as green. The absolute distance between the yellow and the green mustn't be more than 5 frets.
3. Calculate the absolute interval between the two positions by the following rules:
  a. if yellow is the lower note on the fretboard, the absolute interval is the interval from yellow to green; if the yellow is the higher note on the fretboard, then the absolute interval should be the interval from the green to yellow. 
  b. if the two positions are in the same row, the distance (in the unit of semitones) is the fret difference between the two positions.
  c. if the two positions are in the same fret but in different rows, the interval between each adjacent strings are: 6->5: 5 semitones; 5->4: 5 semitones; 4->3: 5 semitones; 3->2: 4 semitones; 2->1: 5 semitones;
  d. the final interval should be calculated based on the string difference and fret difference between the two positions.
  e. let me provide an example for you. Let's define the top left position of the fretboard to be (0, 0). Given the yellow locates at (0, 2) and the green locates at (2, 3), the interval between green and yellow should be b6 (i.e. minor 6th). Let me explain why: 
    i. the interval between (2, 3) and (1, 3) is a positive major 3rd (4 semitones)
    ii. the interval between (1, 3) and (0, 3) is a positive perfect 4th (5 semitones)
    iii. the interval between (0, 3) and (0, 2) is a negative minor 2nd (-1 semitones)
    iv. put these intervals together, we get a minor 6th (4 + 5 - 1 = 8 semitones, which is a minor 6th)
4. There're three modes for the user to choose:
  A. The user is asked to type-in what the absolute interval between these two positions. We use 1, b2, 2, b3, 3, 4, b5, 5, b6, 6, b7 and 7 to represent intervals and they are really denoting unison/octave, minor 2nd, major 2nd, minor 3rd, major 3rd, perfect 4th, diminished 5th, perfect 5th, minor 6th, major 6th, minor 7th and major 7th. Users should type a single key on the keyboard to answer the question, with numbers 1~7 represents 1~7 and 'q' for b2, 'w' for b3, 'r' for b5, 't' for b6 and 'y' for b7.
  B. The yellow cell is randomly choosing from notes {1, b2, 2, b3, 3, 4, b5, 5, b6, 6, b7, and 7}. The user is asked to type-in what note is the green cell then. For example, if the yellow cell is b3 and the green cell is perfect 4th higher than the yellow cell (i.e. absolute interval is perfect 4th), the user should type-in b6, because b3 + 5 semitones is b6. 
  C. Similar to Mode B, but the only difference is that we fix the yellow cell's note to be Do (1), and the user is asked to type-in what the green cell's note is. For example, if the green cell is a major 3rd (i.e. absolute interval) higher than the yellow cell, the user should type-in 3; if the green cell is a perfect 4th (i.e. absolute interval) lower than the yellow cell, the user should type-in 5.
5. No matter user choose the mode A, B or C in Step 4., the program listen to the key press event that the user type-in.
6. The program should check if the user is correct or not. After the answer judging, the program records the result (success or failed) and generates another question for the user.

Now, please generate the whole code for me. Thanks.

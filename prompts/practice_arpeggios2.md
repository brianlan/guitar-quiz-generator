I want you to generate an all-in-one html file with javascript that implements a tool for me to practice and memorize arpeggios in guitar. Below are the requirements.

- All we play is on a 6 by 6 grid indicating the fret of the guitar. 
- we have some predefined chordTypes and arpeggios
- an arpeggio always starts with root note 1 and ends with 1 of either a higher octave or a lower octave, for example: [1, b3, b5, b7, 1] when playing upwards, and [1, b7, b5, b3, 1] when playing downwards.
- Each test round, 
  1. you clear the existing grid
  2. create a quiz for the user by:
     2.1 randomly select a chordTypes
     2.2 randomly select an arpeggios using the same type of chordTypes
     2.3 randomly choose a direction (either upward or downward), if upward, just follow the order defined in arpeggio selected in step2.2, and if downward, the order should be reversed.
     2.4 if there's null in the arpeggio selected in step2.2, we mustn't make null the starting note.
  3. You show the first note of the quiz as "1" on the button grid
  4. next the user will try to complete (by mouse click on button) the rest of the arpeggio. If the position is correct, you show the note on the clicked button, otherwise, let the user know it's wrong.

Here is the basic code structure and predefined chordTypes, arpeggios for your reference:
```
<!DOCTYPE html>
<html>
<head>
    <title>Guitar Arpeggio Practice Tool</title>
    <style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;
        }
        button {
          width: 50px;
          height: 50px;
        }
    </style>
</head>
<body>
    <h1>Guitar Arpeggio Practice Tool</h1>
    <table id="grid"></table>
    <button onclick="startNewRound()">Start New Round</button>
    <script>
        const chordTypes = {
            'major 7': ['1', '3', '5', '7', '1'],
            'minor 7': ['1', 'b3', '5', 'b7', '1'],
            'dominant 7': ['1', '3', '5', 'b7', '1'],
            'half diminished 7': ['1', 'b3', 'b5', 'b7', '1'],
        };

        const arpeggios = {
            'major 7': [
                [[5, 0], [5, 4], [4, 2], [3, 1], [3, 2]], // R6F1
                [[5, 2], [4, 1], [4, 4], [3, 3], [3, 4]], // R6F2
                [[5, 3], [4, 2], [3, 0], [3, 4], [2, 0]], // R6F4
                [[4, 0], [4, 4], [3, 2], [2, 1], [2, 2]], // R5F1
                [[4, 2], [3, 1], [3, 4], [2, 3], [2, 4]], // R5F2
                [[4, 3], [3, 2], [2, 0], [2, 4], [1, 1]], // R5F4
                [[3, 0], [3, 4], [2, 2], [1, 2], [1, 3]], // R4F1
                [[3, 2], [2, 1], [2, 4], [1, 4], [0, 0]], // R4F2
                [[3, 3], [2, 2], [1, 1], [0, 0], [0, 1]], // R4F4
                [[2, 0], [1, 0], [1, 3], [0, 2], [0, 3]], // R3F1
                [[2, 2], [1, 2], [0, 0], [0, 4], [0, 5]], // R3F2 or R3F3
                [[1, 0], [1, 4], [0, 2],  null ,  null ], // R2F1
                [[1, 2], [0, 1], [0, 4],  null ,  null ], // R2F2 or R2F3
                [ null , [5, 2], [4, 0], [4, 4], [3, 0]], // R4F1 (down only)
                [ null , [5, 0], [5, 3], [4, 2], [4, 3]], // R5F4 or R5F3 (down only)
                [ null ,  null , [5, 0], [5, 4], [4, 0]], // R5F1 (down only)
            ],
            'minor 7': [
                [[5, 0], [5, 3], [4, 2], [3, 0], [3, 2]], // R6F1
                [[5, 2], [4, 0], [4, 4], [3, 2], [3, 4]], // R6F2
                [[5, 3], [4, 1], [3, 0], [3, 3], [2, 0]], // R6F4
                [[4, 0], [4, 3], [3, 2], [2, 0], [2, 2]], // R5F1
                [[4, 2], [3, 0], [3, 4], [2, 2], [2, 4]], // R5F2
                [[4, 3], [3, 1], [2, 0], [2, 3], [1, 1]], // R5F4
            ],
            'dominant 7': [
                [[5, 0], [5, 4], [4, 2], [3, 0], [3, 2]], // R6F1
                [[5, 2], [4, 1], [4, 4], [3, 2], [3, 4]], // R6F2
                [[5, 3], [4, 2], [3, 0], [3, 3], [2, 0]], // R6F4
                [[4, 0], [4, 4], [3, 2], [2, 0], [2, 2]], // R5F1
                [[4, 2], [3, 1], [3, 4], [2, 2], [2, 4]], // R5F2
            ],
            'half diminished 7': [
                [[5, 0], [5, 3], [4, 1], [3, 0], [3, 2]], // R6F1
                [[5, 2], [4, 0], [4, 3], [3, 2], [3, 4]], // R6F2
                [[5, 4], [4, 2], [3, 0], [3, 4], [2, 1]], // R6F4
                [[4, 0], [4, 3], [3, 1], [2, 0], [2, 2]], // R5F1
                [[4, 2], [3, 0], [3, 3], [2, 2], [2, 4]], // R5F2
            ],
        };

        let grid = [...Array(6)].map(() => Array(6).fill(''));
        let currentQuiz = [];
        let quizIndex = 0;

        const table = document.getElementById('grid');
        for (let i = 0; i < 6; i++) {
            const row = table.insertRow();
            for (let j = 0; j < 6; j++) {
                const cell = row.insertCell();
                const button = document.createElement('button');
                button.id = `cell-${i}-${j}`;
                button.addEventListener('click', () => handleButtonClick(i, j));
                cell.appendChild(button);
            }
        }

        function generateQuiz(chord, rootNote) {

        }

        function handleButtonClick(i, j) {

        }

        function startNewRound() {

        }
    </script>
</body>
</html>
```


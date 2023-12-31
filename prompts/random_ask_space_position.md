You are an expert on software engineering and programming.
Now I need you to guide me to modify code I have (provided below, written in Javascript/CSS/Html).

The requirements are simple:
1. modify function `startQuiz` to ask the user the position with " " as well but with small probability
2. modify function `checkAnswer` accordingly: it considered correct if user typed on the space button.
3. any other places you think also need to be modified as well.

Please generate the code I can run directly without my additional modification.

"""
<!DOCTYPE html>
<html>
<head>
    <title>Guitar Quiz</title>
    <style>
        #quiz-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 5px; /* Adjust the gap size here. */
            padding: 20px;
            width: 400px;
        }
        .quiz-cell {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .quiz-button {
            width: 60px; /* Adjust the button width here. */
            height: 60px; /* Adjust the button height here. */
            padding: 0;
            margin: 0;
            font-size: 0.8em; /* Adjust the button font size here. */
        }
        .quiz-time {
            font-size: 0.7em;
        }
    </style>
</head>
<body>
    <select id="form-select">
        <!-- The user can select a form here -->
    </select>
    <button id="load-form">Load Form</button>
    <div id="quiz-grid"></div>
    <button id="start-quiz">Start Quiz</button>

    <script>
        // Define the guitar forms
        const guitarFormNames = ["E", "F", "G", "A", "B", "C", "D"]
        const guitarForms = [
            [
                ["3", "4", " ", "5", " "],
                ["7", "1", " ", "2", " "],
                ["5", " ", "6", " ", " "],
                ["2", " ", "3", "4", " "],
                ["6", " ", "7", "1", " "],
                ["3", "4", " ", "5", " "]
            ],
            [
                ["4", " ", "5", " ", "6"],
                [" ", " ", "2", " ", "3"],
                [" ", "6", " ", "7", "1"],
                [" ", "3", "4", " ", "5"],
                [" ", "7", "1", " ", "2"],
                ["4", " ", "5", " ", "6"]
            ],
            [
                ["5", " ", "6", " ", "7"],
                [" ", " ", "3", "4", " "],
                [" ", "7", "1", " ", "2"],
                ["4", " ", "5", " ", "6"],
                ["1", " ", "2", " ", "3"],
                ["5", " ", "6", " ", "7"]
            ],
            [
                ["6", " ", "7", "1", " "],
                ["3", "4", " ", " ", "5"],
                ["1", " ", "2", " ", " "],
                ["5", " ", "6", " ", "7"],
                ["2", " ", "3", "4", " "],
                ["6", " ", "7", "1", " "]
            ],
            [
                ["7", " ", "1", "2", " "],
                [" ", "5", " ", "6", " "],
                ["2", " ", "3", "4", " "],
                ["6", " ", "7", "1", " "],
                ["3", "4", " ", "5", " "],
                ["7", "1", " ", "2", " "]
            ],
            [
                ["1", " ", "2", " ", "3"],
                [" ", " ", "6", " ", "7"],
                [" ", "3", "4", " ", "5"],
                [" ", "7", "1", " ", "2"],
                ["4", " ", "5", " ", "6"],
                ["1", " ", "2", " ", "3"]
            ],
            [
                ["2", " ", "3", "4", " "],
                [" ", " ", "7", "1", " "],
                ["4", " ", "5", " ", "6"],
                ["1", " ", "2", " ", "3"],
                ["5", " ", "6", " ", "7"],
                ["2", " ", "3", "4", " "]
            ]
        ];

        let guitarForm = guitarForms[0]; // Start with the first form

        const formSelect = document.getElementById('form-select');
        const loadFormButton = document.getElementById('load-form');
        const grid = document.getElementById('quiz-grid');
        const startQuizButton = document.getElementById('start-quiz');
        
        let randomString = null;
        let randomFret = null;
        let startTime = null;
        let buttons = [];
        let times = [];

        let waitingForAnswer = false;
        document.addEventListener('keydown', function(event) {
            if (waitingForAnswer) {
                checkAnswer(randomString, randomFret, event.key.toUpperCase());
            }
        });
        

        // Populate the form select dropdown
        for (let i = 0; i < guitarForms.length; i++) {
            const option = document.createElement('option');
            option.value = i;
            option.text = `${i+1}.   ${guitarFormNames[i]} Form`;
            formSelect.add(option);
        }

        loadFormButton.onclick = loadForm;

        startQuizButton.onclick = startQuiz;

        function loadForm() {
          // Clear the grid
          grid.innerHTML = '';

          // Reset the buttons and times
          buttons = [];
          times = [];

          // Load the selected form
          guitarForm = guitarForms[formSelect.value];

          for (let i = 0; i < 6; i++) {
              const row = [];
              const timesRow = [];
              for (let j = 0; j < 5; j++) {
                  const cell = document.createElement('div');
                  cell.className = 'quiz-cell';
                  const btn = document.createElement('button');
                  btn.className = 'quiz-button';
                  btn.innerText = "";
                  btn.style.backgroundColor = "buttonface";
                  btn.onclick = () => checkAnswer(i, j);
                  cell.appendChild(btn);
                  row.push(btn);

                  const timeCell = document.createElement('div');
                  timeCell.className = 'quiz-time';
                  timeCell.innerText = '-';
                  cell.appendChild(timeCell);
                  timesRow.push({cell: timeCell, total: 0, count: 0});
                  
                  grid.appendChild(cell);
              }
              buttons.push(row);
              times.push(timesRow);
          }
        }

        function startQuiz() {
            while (true) {
                randomString = Math.floor(Math.random() * 6);
                randomFret = Math.floor(Math.random() * 5);

                if (guitarForm[randomString][randomFret] !== "") {
                    buttons[randomString][randomFret].innerText = "?";
                    // buttons[randomString][randomFret].style.color = "white";
                    buttons[randomString][randomFret].style.backgroundColor = "orange";
                    break;
                }
            }

            startTime = Date.now();
            waitingForAnswer = true;
        }

        function checkAnswer(string, fret, answer) {
            if (!waitingForAnswer) {
                alert('Please start the quiz first');
                return;
            }
            
            if (string === randomString && fret === randomFret) {
                const userAnswer = answer;
                if (userAnswer === guitarForm[string][fret]) {
                    buttons[string][fret].innerText = "";
                    buttons[randomString][randomFret].style.backgroundColor = "buttonface";
                    const endTime = Date.now();
                    const timeTaken = endTime - startTime;
                    times[string][fret].total += timeTaken;
                    times[string][fret].count++;
                    times[string][fret].cell.innerText = (times[string][fret].total / times[string][fret].count / 1000).toFixed(2) + 's';

                    waitingForAnswer = false;
                    startQuiz();
                } else {
                    alert('Wrong answer. Try again.');
                }
            } else {
                alert('Please answer the highlighted position');
            }
            
            // Update the average time for the cell
            if (times[string][fret].count > 0) {
              times[string][fret].cell.innerText = (times[string][fret].total / times[string][fret].count / 1000).toFixed(2) + 's';
            } else {
              times[string][fret].cell.innerText = '-';
            }
        }

        // Load the initial form
        loadForm();
    </script>
</body>
</html>
"""
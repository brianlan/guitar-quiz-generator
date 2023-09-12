import tkinter as tk
from tkinter import messagebox, simpledialog
from random import randint

# Define the guitar form
guitar_form = [
    ["1", "", "2", "", "3"],
    ["", "", "6", "", "7"],
    ["", "3", "4", "", "5"],
    ["", "7", "1", "", "2"],
    ["4", "", "5", "", "6"],
    ["1", "", "2", "", "3"]
]

class GuitarQuiz(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Guitar Quiz")
        self.geometry("600x600")

        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack()

        self.buttons = []
        for i in range(6):
            row = []
            for j in range(5):
                btn = tk.Button(self.grid_frame, text="_" if guitar_form[i][j] != "" else " ", command=lambda i=i, j=j: self.check_answer(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

        self.quiz_button = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        self.quiz_button.pack()

        self.random_string = None
        self.random_fret = None

    def start_quiz(self):
        while True:
            self.random_string = randint(0, 5)
            self.random_fret = randint(0, 4)

            if guitar_form[self.random_string][self.random_fret] != "":
                self.buttons[self.random_string][self.random_fret].config(text="?")
                break


    def check_answer(self, string, fret):
        if self.random_string is None or self.random_fret is None:
            messagebox.showinfo("Information", "Please start the quiz first")
        elif string == self.random_string and fret == self.random_fret:
            user_answer = simpledialog.askstring("Input", "What's the note?")
            if user_answer == guitar_form[string][fret]:
                self.buttons[string][fret].config(text="_" if guitar_form[string][fret] != "" else " ")
                self.start_quiz()
            else:
                messagebox.showinfo("Unfortunately", "Wrong answer. Try again.")
        else:
            messagebox.showinfo("Information", "Please answer the highlighted position")

if __name__ == "__main__":
    app = GuitarQuiz()
    app.mainloop()
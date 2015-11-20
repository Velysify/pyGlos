"""#!/usr/bin/env python"""
import tkinter as tk
import random
import sys
class Word_list(object):
    def __init__(self):
        self.word_list = {}
        self.fill_list()
        self.word = ""

    def fill_list(self):
        with open('ordlista.txt','r') as f:
            for line in f:
                split_line = line.split("=")
                try:
                    self.word_list[split_line[0].strip()] = split_line[1].strip()
                except IndexError:
                    print (split_line[0])
                    
    def new_word(self):
        self.word = random.choice(list(self.word_list.keys()))
        description = self.word_list.get(self.word)
        app.update_word(description)

    def check_answer(self):
        answer = app.answer.get()
        true_answer = answer.strip()
        if self.word.lower() == true_answer.lower():
            app.score_answer(True)
        else:
            app.score_answer(False)  
    
class Application (tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.score = 0
        self.negative = 0
        self.createWidgets()
        self.answer

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.columnconfigure(0, weight = 1)
        top.columnconfigure(1, weight = 1)
        self.answer = tk.Entry(self)
        tk.Label(self, text = "Svar: ").grid(row = 1, column = 0)
        self.answer.grid(row = 1, column = 1)
        self.new_word_button = tk.Button(self, text = "Nytt ord", command = wd.new_word)
        self.check_answer_button = tk.Button(self, text = "Kolla svar", command = wd.check_answer)
        self.word = tk.Label(self, text = "   ")
        self.check_answer_button.grid(row = 3, column = 2)
        self.word.grid(row = 0, column = 1)
        self.correct = tk.Label(self, text = self.score, bg = 'green')
        self.tries = tk.Label(self, text = self.negative, bg = 'red')
        self.correct.grid(row = 2, column = 0)
        self.tries.grid(row = 2, column = 1)
        self.new_word_button.grid(row = 3, column = 3)

    def update_word(self, description):
        self.answer.delete(0, 'end')
        self.word.grid_forget()
        self.word = tk.Label(self, text = "Beskrivning: ").grid(row = 0, column = 0)
        self.word = tk.Label(self, text = description)
        self.word.grid(row = 0, column = 1)

    def score_answer(self, correct):
        if correct:
            self.score += 1
            self.correct.grid_forget()
            self.correct = tk.Label(self, text = self.score, bg = 'green')
            self.correct.grid(row = 2, column = 0)
            wd.new_word()

        else:
            self.negative += 1
            self.tries.grid_forget()
            self.tries = tk.Label(self, text = self.negative, bg = 'red')
            self.tries.grid(row = 2, column = 1)
            self.answer.delete(0, 'end')
    
wd = Word_list() 
app = Application()
app.master.title('Glosförhör')
app.mainloop()

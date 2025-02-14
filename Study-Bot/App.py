from tkinter import *
import knowledge as informatiom
import random

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('Study Bot')
        self.root.geometry('650x410+300+150')
        self.root.configure(bg='azure')
        self.learning = informatiom.Learn
        self.x = random.randint(0, len(self.learning)-1)
        questions, answers, self.score, self.total = list(self.learning.keys()), list(self.learning.values()), 0, 0

        self.text = Text(self.root, bd=5, height=5, width=25, font='ariel 32 bold')
        self.text.place(x=20, y=120)

        self.label = Label(self.root, text=questions[self.x], font='ariel, 25 bold', width=20,bd=5, bg='dimgray', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text="0%", font='ariel, 25 bold', bg='dimgray', width=5, fg='black')
        self.label2.pack(side='top', fill=BOTH)
        self.label2.place(x=544, y = 50)

        def reset():
            self.total += 1        
            x = self.text.get("1.0", END)
            if str((x)[0:len(x)-1]) == str(answers[self.x]):
                self.score += 1
                
            self.label.after(0, self.label.destroy())
            self.x = random.randint(0, len(self.learning)-1)
            self.label = Label(self.root, text=questions[self.x], font='ariel, 25 bold', width=20,bd=5, bg='dimgray', fg='black')
            self.label.pack(side='top', fill=BOTH)
            
            self.text.delete("1.0", END)

            self.label2.destroy
            self.label2 = Label(self.root, text=f"{int(self.score/self.total*100)}%", font='ariel, 25 bold', bg='dimgray', width=5, fg='black')
            self.label2.pack(side='top', fill=BOTH)
            self.label2.place(x=544, y = 50)

        self.button = Button(self.root, text='✓', font='sarif 20 bold italic', width=5, bd=5, bg='silver', fg='black', command=reset)
        self.button.place(x=275, y=54)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

main()

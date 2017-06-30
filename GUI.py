from Tkinter import *
import sys
import os

class TextOut(Text()):

    def write(self, s):
        self.insert(self.CURRENT, s)

    def flush(self):
        pass


if __name__ == '__main__':
    root = Tk()
    text = TextOut(root)
    sys.stdout = text
    text.pack(expand=True, fill=root.BOTH)
    root.mainloop()

root = Tk()

frame = Frame(root)
frame.pack()

e = Entry(root)
e.pack(side=TOP)

e.delete(0, END)
e.insert(0, "Insert Twitter username here.")

root.button = Button(
    frame, text="QUIT", fg="red", command=frame.quit
)

root.button.pack(side=BOTTOM)

'''self.hi_there = Button(frame, text="Hello", command=self.say_hi)
   self.hi_there.pack(side=LEFT)'''

text = Text(root)
text.pack()
text.insert(END, output)

root.mainloop()

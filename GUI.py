import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):

        #Attempted to make a background throughout the app
        # bg = tk.PhotoImage('/Users/CrisForno/Documents/wallpapers/suit_logo_OSX.png')
        # self.bg_label = tk.Label(self, image=bg)
        # self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.twitterHandle = tk.Entry(self, fg='#00aced')
        self.twitterHandle.grid()

        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Misspelled Twitter')
app.mainloop()

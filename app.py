import tkinter as tk
import problem27_module as p27

class Home(tk.Tk):
    def __init__(self, *kwargs, **args):
        tk.Tk.__init__(self, *kwargs, **args)
        
        container = tk.Frame(self, width=300, height=300)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        
        # Adding Buttons
        
        self.frames = {}
        
    def showframe(self, frm):
        frame = self.frames[frm]
        frame.tkraise()


app = Home()
app.mainloop()

# p27.solve()
import tkinter as tk

class EulerProjectApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)
        
        self.resizable(0, 0)
        
        self.title('EulerProject - Beta(0.1)')


app = EulerProjectApp()
app.mainloop()
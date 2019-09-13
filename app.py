import tkinter as tk
import problem27_module as p27

# Installing image utility
from PIL import Image, ImageTk
import Pmw
class Home(tk.Tk):
    def __init__(self, *kwargs, **args):
        tk.Tk.__init__(self, *kwargs, **args)
        
        self.title('EulerProject')
        
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.logoimg = Image.open("./images/icon.jpg")
        self.renderimg = ImageTk.PhotoImage(self.logoimg)
        logo = tk.Label(self, image=self.renderimg, text="EulerProject")
        logo.pack(side=tk.TOP, padx=40)
        
        # Contains all the controlls required to navigate projects
        controlframe = tk.Frame(self)
        controlframe.pack(side=tk.TOP, pady=(10, 30))
        
        self.frames = {}
        
        # Adding controlls to controlframe
        projectlist = tk.Listbox(controlframe, width=20, height=3)
        projectlist_scroller = tk.Scrollbar(controlframe, command=projectlist.yview)
        projectlist.config(yscrollcommand=projectlist_scroller.set)
        projectlist.pack(side=tk.LEFT)
        projectlist_scroller.pack(side=tk.RIGHT, fill=tk.Y)
        
        
        
        for i in range(10):
            projectlist.insert(tk.END, i)
        
        self.frames = {}
        
    def showframe(self, frm):
        frame = self.frames[frm]
        frame.tkraise()


app = Home()
app.mainloop()

# p27.solve()
import tkinter as tk
import problem27_module as p27

# Installing image utility
from PIL import Image, ImageTk
import Pmw # Python MegaWidget module

class Home(tk.Tk): 
    def __init__(self, *kwargs, **args):
        tk.Tk.__init__(self, *kwargs, **args)
        
        self.title('EulerProject')
        
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.frames = {}
        
        for F in (MainPage, project_solution):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.frames[MainPage].populatelist(list(self.frames.keys()))
        
        self.showframe(MainPage)
        
    def showframe(self, frm):
        print ('Showing Frame')
        # removing all frames from grid
        for f in self.frames.values():
            f.grid_remove()
        frame = self.frames[frm]
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

class MainPage(tk.Frame):
    selectedframe = None
    frames = {}
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.logoimg = Image.open("./images/icon.jpg")
        self.renderimg = ImageTk.PhotoImage(self.logoimg)
        logo = tk.Label(self, image=self.renderimg, text="EulerProject")
        logo.pack(side=tk.TOP, padx=40, pady=(10, 0))
        
        # Contains all the controlls required to navigate projects
        controlframe = tk.Frame(self)
        controlframe.pack(side=tk.TOP, pady=(10, 30))
        
        combobox = Pmw.ComboBox(controlframe, label_text='Projects', labelpos='wn',
                        listbox_width=24, dropdown=1,
                        selectioncommand=self.choseEntery,
                        scrolledlist_items=self.frames)
        combobox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=8)
        if len(self.frames) > 0:
            combobox.selectitem(self.frames[0])
        
        goBtn = tk.Button(controlframe, text='GO', command= lambda: controller.showframe(project_solution))
        goBtn.pack(side=tk.TOP, fill=tk.BOTH)
        
    def choseEntery(self, entry):
        print('selected %s' % entry)
        self.selectedframe = entry
        
    def populatelist(self, frames):
        self.frames = frames

class project_solution(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        solve_btn = tk.Button(self, text='Solve', command=self.solve)
        solve_btn.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    
    def solve(self):
        pass

app = Home()
app.mainloop()

# p27.solve()
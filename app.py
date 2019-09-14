import tkinter as tk
import problem27_module as p27

# Installing image utility
from PIL import Image, ImageTk
import Pmw # Python MegaWidget module

global_frames = None

class Home(tk.Tk): 
    def __init__(self, *kwargs, **args):
        tk.Tk.__init__(self, *kwargs, **args)
        
        self.title('EulerProject')
        
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.frames = {}
        global global_frames
        global_frames = {'Project-27': project_solution1,'Project-24': project_solution2}
        
        main = MainPage(container, self)
        self.frames[MainPage] = main
        main.grid(row=0, column=0, sticky='nsew')
        
        for F in global_frames.values():
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.showframe(MainPage)
        
    def showframe(self, frm):
        # removing all frames from grid
        for f in self.frames.values():
            f.grid_remove()
        frame = self.frames[frm]
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

class MainPage(tk.Frame):
    selectedframe = None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.logoimg = Image.open("./images/icon.jpg")
        self.renderimg = ImageTk.PhotoImage(self.logoimg)
        logo = tk.Label(self, image=self.renderimg, text="EulerProject")
        logo.pack(side=tk.TOP, padx=40, pady=(10, 0))
        
        tk.Label(self, text="EulerProject", font=('Arial', 18)).pack(side=tk.TOP)
        
        # Contains all the controlls required to navigate projects
        controlframe = tk.Frame(self)
        controlframe.pack(side=tk.TOP, pady=(10, 30))
        
        combobox = Pmw.ComboBox(controlframe, label_text='Projects', labelpos='wn',
                        listbox_width=24, dropdown=1,
                        selectioncommand=self.choseEntery,
                        scrolledlist_items=global_frames.keys())
        combobox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=8)
        combobox.selectitem(list(global_frames.keys())[0])
        
        goBtn = tk.Button(controlframe, text='GO', command= lambda: controller.showframe(global_frames[self.selectedframe]))
        goBtn.pack(side=tk.TOP, fill=tk.BOTH)
        
    def choseEntery(self, entry):
        print('selected %s' % entry)
        self.selectedframe = entry

class project_solution1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        solve_btn = tk.Button(self, text='Solve', command=self.solve)
        solve_btn.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    
    def solve(self):
        pass

class project_solution2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        lbl = tk.Label(self, text='Project-27')
        lbl.pack(side=tk.TOP)
        
        solve_btn = tk.Button(self, text='Solve', command=self.solve)
        solve_btn.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    
    def solve(self):
        pass

app = Home()
app.mainloop()

# p27.solve()
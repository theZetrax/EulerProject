import tkinter as tk
import problem27_module as p27
import problem24_module as p24

# Installing image utility
from PIL import Image, ImageTk
import Pmw # Python MegaWidget module

global_frames = None
global_problemsolutions = None

class Home(tk.Tk): 
    def __init__(self, *kwargs, **args):
        tk.Tk.__init__(self, *kwargs, **args)
        self.resizable(0, 0)
        
        self.title('EulerProject')
        
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.frames = {}
        global global_frames
        global global_problemsolutions
        global_frames = {'Solutions': project_solution,}
        global_problemsolutions = {'Project-27': p27,'Project-24': p24}
        
        main = MainPage(container, self)
        self.frames[MainPage] = main
        main.grid(row=0, column=0, sticky='nsew')
        
        for F in global_frames.values():
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.showframe(MainPage)
        
    def showframe(self, frm):
        if frm is MainPage:
            self.geometry('')
        else:
            self.geometry('500x400')
        
        # removing all frames from grid
        for f in self.frames.values():
            f.grid_remove()
        frame = self.frames[frm]
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()
    
    def showsolution(self, solution):
        self.showframe(project_solution)
        project_solution.selected_solution = solution
        
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
                        selectioncommand=self.chooseEntery,
                        scrolledlist_items=global_problemsolutions.keys())
        combobox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=8)
        combobox.selectitem(list(global_problemsolutions.keys())[0])
        self.chooseEntery(list(global_problemsolutions.keys())[0])
        
        goBtn = tk.Button(controlframe, text='GO', command= lambda: controller.showsolution(global_problemsolutions[self.selectedframe]))
        goBtn.pack(side=tk.TOP, fill=tk.BOTH)
        
    def chooseEntery(self, entry):
        print('selected %s' % entry)
        self.selectedframe = entry

class project_solution(tk.Frame):
    selected_solution = None
    output = None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        solution_container = tk.Frame(self)
        solution_container.pack(side=tk.TOP, fill=tk.X, pady=(8, 0))
        
        text = tk.Text(solution_container, height=19, width=56)
        scroll = tk.Scrollbar(solution_container, command=text.yview)
        text_lbl = tk.Label(solution_container, text='Solution')
        text.configure(yscrollcommand=scroll.set)
        text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
        text.tag_configure('big', font=('Verdana', 24, 'bold'))
        text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))
        text.tag_configure('groove', relief=tk.GROOVE, borderwidth=2)
        text_lbl.pack(side=tk.TOP)
        text.pack(side=tk.LEFT, padx=10, pady=10)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        solve_btn = tk.Button(self, text='Solve', command= lambda: text.insert(tk.END, self.solve() + '\n'))
        solve_btn.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
    
    def solve(self):
        self.output = self.selected_solution.solve()
        return "Problem Definition\n" + self.selected_solution.problem_definition + "\nSolution: " + self.output

app = Home()
app.mainloop()
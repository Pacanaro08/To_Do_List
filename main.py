from tkinter import *

class Window:
    def __init__(self, master=None):
        self.master = master
        self.build()

    def build(self):
        self.font = ("Verdana", "11")

        self.header_font = ("Verdana", "16", "bold")
    
        self.main_window = Frame(self.master)
        self.main_window.pack(fill="both", expand=True)

        self.header = Frame(self.main_window)
        self.header.pack()

        self.input_container = Frame(self.main_window)
        self.input_container["padx"] = 20
        self.input_container["pady"] = 10
        self.input_container.pack()

        self.header_msg = Label(self.header, text="To-Do List")
        self.header_msg["font"] = self.header_font
        self.header_msg.pack()

        self.entry_msg = Label(self.input_container, text="Task:")
        self.entry_msg["font"] = self.font
        self.entry_msg.pack(side=LEFT)

        self.task = Entry(self.input_container)
        self.task.pack(side=LEFT)

        self.task.bind("<Return>", lambda event: self.addTask())

        self.add_task = Button(self.input_container, text="Enter")
        self.add_task["command"] = self.addTask
        self.add_task.pack(side=LEFT)

        self.list_handler_canvas = Canvas(self.main_window)
        self.list_handler_canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.main_window, orient="vertical", command=self.list_handler_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.list_handler_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.list_handler = Frame(self.list_handler_canvas)

        self.canvas_window = self.list_handler_canvas.create_window((0, 0), window=self.list_handler, anchor="nw")

        self.list_handler.bind("<Configure>", self.on_frame_configure)
        self.list_handler_canvas.bind("<Configure>", self.frame_width)
    
    def frame_width(self, event):
        canvas_width = event.width
        self.list_handler_canvas.itemconfig(self.canvas_window, width=canvas_width)

    def on_frame_configure(self, event):
        self.list_handler_canvas.configure(scrollregion=self.list_handler_canvas.bbox("all"))

    def addTask(self):
        task = self.task.get()
        
        if task:
            task_frame = Frame(self.list_handler)
            task_frame.pack(fill="x", anchor="w", pady=2)

            task_checkbutton = Checkbutton(task_frame)
            task_checkbutton.pack(side="left")

            task_label = Label(task_frame, text=task, wraplength=300, justify="left", anchor="w")
            task_label.pack(side="left", fill="x", expand=True, padx=3)
        
            self.task.delete(0, END)

root = Tk()
root.title("To Do List Helper")
root.geometry("400x550+50+50")
root.attributes("-topmost", 1)
root.resizable(False, False)
Window(root)
root.mainloop()
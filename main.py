# https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956

from tkinter import *

class Janela:
    def __init__(self, master=None):
        self.font = ("Verdana", "11")

        self.header_font = ("Verdana", "16", "bold")

        self.header = Frame(master)
        self.header.pack()

        self.input_container = Frame(master)
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

        self.add_task = Button(self.input_container, text="BUTAO")
        self.add_task["padx"] = 20
        self.add_task["command"] = self.addTask
        self.add_task.pack(side=LEFT)
    
    def addTask(self):
        ...

root = Tk()
root.title("To Do List Helper")
root.geometry("300x400+50+50")
root.attributes("-topmost", 1)
Janela(root)
root.mainloop()
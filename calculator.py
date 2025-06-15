import os
import platform
import time
from termcolor import colored
import tkinter as tk

def clear_screen():
    system_name = platform.system().lower()
    if system_name == 'windows':
        os.system('cls')  
    else:
        os.system('clear')  

clear_screen()

header = '''
 ______     __  __     __     ______     _____     __       
/\  ___\   /\ \/ /    /\ \   /\  == \   /\  __-.  /\ \      
\ \___  \  \ \  _"-.  \ \ \  \ \  __<   \ \ \/\ \ \ \ \     
 \/\_____\  \ \_\ \_\  \ \_\  \ \_____\  \ \____-  \ \_\    
  \/_____/   \/_/\/_/   \/_/   \/_____/   \/____/   \/_/    
                                                               
'''


print(colored(header, 'blue'))


time.sleep(5)


clear_screen()


toilet = '''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠒⠒⠀⠀⠒⠂⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⣐⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠀⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠐⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⠄⠂⠠⢀⡀⠀⠀⠀⠀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⡄⠀⠀⠀⠀⢀⠠⠐⠒⠐⠄
⢠⠁⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡤⡀⠁⠉⠀⠀⠀⠀⠀⠈
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠰⠀⠀⠀⠀⠀⠀⠀⢨
⠘⠄⠤⠀⠀⠀⠀⠀⠀⡆⠀⠀⢀⣼⣿⣿⠿⠿⠛⠻⠛⠛⠛⠙⠛⠛⠋⠩⠝⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⢘⣿⡶⣶⠲⢶⣴⣦⡄⠁
⠀⠀⠇⠀⠀⠀⠠⠔⢈⠁⠁⠀⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⡹⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⣿⣝⡾⣑⢎⡷⣏⡇⠀
⠀⠀⠏⠛⠓⠻⠷⠿⢿⠀⠀⠀⣿⣿⠇⠀⠀⠀⠀⣀⣠⣄⣤⣄⣀⣀⣀⠀⠸⣽⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣽⡾⣝⣳⢎⡿⡥⠂⠀
⠀⠀⢰⠀⠀⠀⠀⠀⢘⠀⠀⠀⢿⣿⢰⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⣿⡽⣯⡽⢾⣹⡓⠀⠀
⠀⠀⢸⠀⠀⠀⠀⠀⠨⠀⡀⢠⡘⣿⠸⣿⣿⡟⣋⢿⣿⡿⠙⣿⣿⡿⣽⢻⣿⡿⢽⣷⡇⠀⠀⠀⠀⠀⠀⢠⣿⣟⣷⡻⣝⣧⢹⠀⠀
⠀⠀⠘⡀⠀⠀⠀⠀⠀⡄⠙⠀⣿⣿⠀⠈⠛⠂⠡⠾⠟⠁⠀⡨⠟⠓⣖⣋⡁⣤⣿⢿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣞⣷⡻⣽⡺⡥⠀⠀
⠀⠀⠀⡄⠀⠀⠀⠀⠀⡇⠀⠀⢹⣯⡦⣤⣦⣤⡄⣃⠀⠀⠀⢴⣛⣶⢏⣾⣿⣿⣿⣻⠁⠀⠀⠀⠀⠀⠀⣸⣿⢾⣳⣟⡷⡽⡁⠀⠀
⠀⠀⠀⠇⠀⠀⠀⠀⠀⢡⢸⣡⡍⢳⣿⣳⣭⡷⡤⠝⣤⣁⣀⣺⣿⢻⢾⣭⣿⣿⡿⠃⠀⠀⠀⠰⣭⣱⢀⣿⣿⣻⡽⣾⣝⣷⠁⠀⠀
⠀⠀⠀⢰⠀⠀⢀⢀⠀⢈⡆⠁⠀⠀⠸⣷⣻⢿⣿⣶⣼⣿⣿⣿⣯⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠉⠀⣼⣿⡷⣿⣽⣳⢯⠸⠀⠀⠀
⠀⠀⠀⠈⡄⠀⠀⢢⠳⡠⢼⠀⠀⠀⠀⢿⣶⣂⢿⣿⣏⢙⠈⠙⢻⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣽⡷⣯⣟⠯⡆⠀⠀⠀
⠀⠀⠀⠀⠰⠀⠀⠀⡑⢝⢦⣇⠀⠀⠀⠘⣿⣿⣦⡹⢿⣶⣶⣶⢿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣟⣾⣿⣻⣞⢷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠇⠀⠶⡈⡎⣷⡾⣷⡀⠀⠀⣿⣿⣿⣿⣆⠈⣀⣈⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⡿⣷⣿⡎⡆⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠈⠮⠵⠵⠎⠵⠛⠛⠛⠛⠻⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⠶⠶⠶⠾⠿⠿⠿⠿⠿⠿⠽⣿⣟⢗⠜⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⢀⠀⣀⣀⣀⣀⡈⠎⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠀⠀⠉⠉⠉⠀⠀⠀⠀⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠂⠐⠀⠈⠀⠉⠉⠉⠉⠀⠀⠀⠀⠐⢰⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢄⡰⢠⢒⡰⢂⡖⣐⠺⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⢄⢢⡱⣘⢦⡜⣣⢮⡵⣫⡼⣧⢹⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢱⡰⢶⡖⣦⢤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣄⣤⣔⣦⣳⢦⣟⣮⣷⣻⣽⣞⣿⡽⣯⣿⣟⣿⠫⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢇⠢⡙⢤⠛⣼⢳⣻⢮⣝⡯⣽⣹⢮⡽⣭⣛⢮⣗⡻⣞⡽⣯⣻⠷⣯⢷⣻⢾⣽⣛⣷⣻⣞⢧⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡵⣹⢦⣛⢦⣏⣷⣻⢮⡽⣶⣛⣮⢗⡷⣫⣟⡼⣝⣧⠿⣵⢯⡿⣭⢿⣭⣟⡾⣽⡞⣷⢏⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣟⣯⣟⡿⣞⡷⣯⢿⡽⣞⣳⣭⢿⣹⣗⡾⣝⡾⣞⣻⡽⣾⡽⢯⣷⣛⡾⣽⣳⢿⢙⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠪⠿⣽⣯⢿⡽⣯⢿⣽⣳⢯⣟⡷⡾⣝⣻⡼⣯⢷⣻⣗⣿⣻⢾⣽⣻⠷⡫⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠩⢟⢿⣽⣟⣾⣽⣟⣾⣽⡿⣽⣷⣻⣽⣯⣷⣻⣾⡽⡛⠎⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠉⠉⠉⠙⠛⠛⡙⢩⠩⣅⠫⢖⡭⣿⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠣⡐⢍⠎⡼⣻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠱⡈⢎⡱⣝⣏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⢑⠢⣑⢮⢿⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠌⡒⡡⢞⣯⢯⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⢢⠁⢧⡙⣮⣟⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠍⢦⡙⣮⢿⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⡘⢦⣙⣾⣋⠁⠀  ,⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
print(colored(toilet, 'magenta'))

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)


def clear():
    entry.delete(0, tk.END)


def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "error your dumbass just put something invalid in ")


def memory_add():
    global memory
    try:
        memory += float(entry.get())
    except ValueError:
        pass


def memory_subtract():
    global memory
    try:
        memory -= float(entry.get())
    except ValueError:
        pass


def memory_recall():
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(memory))


def exponent():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + '**')

# Function to handle trigonometric functions
def trig_function(func):
    try:
        value = float(entry.get())
        if func == 'sin':
            result = math.sin(math.radians(value))
        elif func == 'cos':
            result = math.cos(math.radians(value))
        elif func == 'tan':
            result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

memory = 0


root = tk.Tk()
root.title("ghost's skbidi calculator ")


entry = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 14), justify="right")
entry.grid(row=0, column=0, columnspan=5)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sqrt', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('^', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('M+', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('M-', 5, 3), ('MR', 5, 4)
]


for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=clear)
    elif text == "sqrt":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=sqrt)
    elif text == "^":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=exponent)
    elif text == "M+":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=memory_add)
    elif text == "M-":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=memory_subtract)
    elif text == "MR":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=memory_recall)
    elif text in ['sin', 'cos', 'tan']:
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=lambda t=text: trig_function(t))
    else:
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Run the Tkinter event loop
root.mainloop()

#import from library tk=graphical interface and ttk for widgets
import tkinter as tk
from tkinter import ttk
darkmode = False
# function for everytime a button is clicked (takes text of clicked button as import and retrieves current text from result entry)
def execute_button_click(button_clicked_text):
    current_text = result_var.get()

    if button_clicked_text == "=":
        try:
            # replaces custom symbols with python operators
            expression = current_text.replace("÷", "/").replace("x", "*")
            #evaluated using eval function
            result = eval(expression)
            #Check is the result is a whole number
            if result.is_integer():
                result = int(result)
            result_var.set(result)
        # if there are errors if the program can't calculate
        except Exception as e:
            result_var.set("Error")
    elif button_clicked_text == "C":
        result_var.set("")
    elif button_clicked_text == "%":
        try:
            current_number = float(current_text)
            result_var.set(current_number/100)
        except ValueError:
            result_var.set("Error")
    elif button_clicked_text == "+-":
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")
    elif button_clicked_text == "⌫":
        result_var.set(current_text[:-1])
    else:
        result_var.set(current_text + button_clicked_text)

def change_mode():
    global darkmode
    darkmode = not darkmode
    if darkmode:
        root.configure(bg = "#252525") #Background for root window
        style.configure("TEntry", fieldbackground="#303030", foreground = "white") #darker field, white text
        #result_entry.configure(foreground = "white") #darker entry, white text
        #button background, foreground-button text color, relief-flat appearance, borderwidth is none
        style.configure("TButton", background = "#303030", foreground = "white", font = ("Helvetica", 16), width = 10, height = 4, relief = "flat", borderwidth = 0)
        #Hover and click colors/effects
        style.map("TButton", background = [("active", "#606060"), ("pressed", "#202020")], foreground = [("active", "white"), ("pressed", "white")])
        darkmode_button.configure(background="#505050", foreground="white")
    else:
        root.configure(bg="white")
        style.configure("TEntry", fieldbackground="white", foreground = "black") #back to og
        #result_entry.configure(foreground = "black")
        style.configure("TButton", background = "lightgrey", foreground = "black", font = ("Helvetica", 16), width = 10, height = 4, relief = "raised", borderwidth = 1)
        style.map("TButton", background = [("active", "grey"), ("pressed", "darkgrey")], foreground = [("active", "black"), ("pressed", "black")])
        darkmode_button.configure(background="lightgrey", foreground="black")

def connect_keyboard(event):
    char = event.char
    if char in "0123456789.+-*/%":
        execute_button_click(char)
    elif char == "\r":
        execute_button_click("=")
    elif char == "\x08":
        execute_button_click("⌫")
#Create the main window
root = tk.Tk()
#Label above window
root.title("Calculator")
#Entry widget to display the result with larger font size
result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_var, font = ("Helvetica", 24), justify = "right")
result_entry.grid(row=0, column=0, columnspan=4,sticky="nsew")
#button text row column
buttons = [("C", 1, 0), ("+-", 1, 1), ("%", 1, 2), ("÷", 1, 3),
           ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
           ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
           ("1", 4, 0), ("2", 4, 1), ("3", 4 , 2), ("+", 4 ,3),
           ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3),
           ("⌫",6,0,4)
]
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font = ("Helvetica",16), width = 10, height = 4)
#create buttons
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text = button_text, command = lambda text = button_text: execute_button_click(text), style = "TButton")
    button.grid(row=row, column=col, columnspan=colspan, sticky = "nsew", ipadx=10, ipady=4, padx=5, pady=5)
darkmode_button = ttk.Button(root, text="Dark Mode", command = change_mode, style = "TButton")
darkmode_button.grid(row=7, column=0, columnspan = 4, sticky = "nsew", padx = 5, pady = 5)
#Configure row and column weights so that they expand proportionally
for i in range(8):
    root.grid_rowconfigure(i, weight = 1)
for i in range(4):
    root.grid_columnconfigure(i, weight = 1)
#Set window size to 9:16
width = 500
height = 700
root.geometry(f"{width}x{height}")
#Make window nonresizeable
root.resizable(False, False)
#enable keyboard
#enter connects to equals
root.bind("<Key>", connect_keyboard)
root.bind("<Return>", lambda event: execute_button_click("="))
#backspace connects to clear
root.bind("<BackSpace>", lambda event: execute_button_click("⌫"))
root.bind("<Delete>", lambda event: execute_button_click("C"))
#run main loop
root.mainloop()
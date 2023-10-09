import tkinter as tk
from tkinter import ttk
import subprocess


def run_translation_model():
    ## Using subprocess module to run translate.py script
    try:
        subprocess.run(["python", "translate.py"], check=True)
    except subprocess.CalledProcessError:
        result_label.config(text="Translation failed")
    else:
        result_label.config(text="Translation successful")


## Creating the main window for teh GUI
root = tk.Tk()
root.title("Speech Translation Model")

## Creating  a button to run the translation.py script
## Limited to a single button GUI for now for simplicity
translate_button = ttk.Button(
    root, text="Run Translation Model", command=run_translation_model
)
translate_button.pack(pady=100, padx=100)

## Creating a label to display the model result
result_label = ttk.Label(root, text="")
result_label.pack()

## Run the GUI main loop
root.mainloop()

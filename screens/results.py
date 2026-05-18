import tkinter as tk
from styles import *

def setup_results(frame, show_home):

    label_results_title = tk.Label(frame, text="Results", font=HEADING_FONT)
    label_results_title.pack(pady=10)

    listbox_results = tk.Listbox(frame, width=80, height=20)
    listbox_results.pack(pady=10)

    tk.Button(frame, text="← Back to Home", width=BUTTON_WIDTH, command=show_home).pack(pady=10)

    return label_results_title, listbox_results
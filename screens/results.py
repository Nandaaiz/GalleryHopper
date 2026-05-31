import tkinter as tk
from styles import *

def setup_results(frame, show_home):

    tk.Label(frame, text="", font=HEADING_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=0)

    label_results_title = tk.Label(frame, text="Results", font=HEADING_FONT, bg=COLOR_BG, fg=COLOR_TEXT)
    label_results_title.pack(pady=20)

    # scrollable results area
    canvas = tk.Canvas(frame, bg=COLOR_BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=40)
    scrollbar.pack(side="right", fill="y")

    tk.Button(frame, text="← Back to Home", command=show_home,
              bg=COLOR_BG, fg=COLOR_GRAY, relief="flat", font=SMALL_FONT,
              cursor="hand2").pack(pady=10)

    return label_results_title, scroll_frame
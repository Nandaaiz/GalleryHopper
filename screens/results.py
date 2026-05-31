import tkinter as tk
from styles import *

def setup_results(frame, show_home):

    # header
    header = tk.Frame(frame, bg=COLOR_BG)
    header.pack(fill="x", padx=40, pady=(20, 0))

    label_results_title = tk.Label(header, text="Results", font=HEADING_FONT, bg=COLOR_BG, fg=COLOR_TEXT)
    label_results_title.place(relx=0.5, rely=0.5, anchor="center")
    label_results_title.pack(expand=True)

    back_btn = tk.Canvas(header, width=120, height=32, bg=COLOR_BG, highlightthickness=0)
    rect = back_btn.create_rectangle(0, 0, 120, 32, fill=COLOR_WHITE, outline=COLOR_BORDER)
    back_btn.create_text(60, 16, text="← Back", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_home())
    back_btn.bind("<Enter>", lambda e: back_btn.itemconfig(rect, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    back_btn.bind("<Leave>", lambda e: back_btn.itemconfig(rect, fill=COLOR_WHITE, outline=COLOR_BORDER))
    back_btn.pack(side="right")

    tk.Frame(frame, height=1, bg=COLOR_BORDER).pack(fill="x", padx=40, pady=12)

    # scrollable results area
    canvas = tk.Canvas(frame, bg=COLOR_BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((400, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=40)
    scrollbar.pack(side="right", fill="y")

    return label_results_title, scroll_frame
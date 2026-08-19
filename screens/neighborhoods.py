import tkinter as tk
from styles import *

def setup_neighborhoods(frame, neighborhoods, show_results, show_home, city="New York"):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Choose a Neighborhood", font=HEADING_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=30)

    canvas = tk.Canvas(frame, bg=COLOR_BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((400, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if not neighborhoods:
        tk.Label(scroll_frame, text="Connection error. Please check your internet connection.",
                 font=SMALL_FONT, bg=COLOR_BG, fg="red", wraplength=300).pack(pady=20)
    else:
        for neighborhood in neighborhoods:
            btn = tk.Canvas(scroll_frame, width=300, height=36, bg=COLOR_BG, highlightthickness=0)
            rect = btn.create_rectangle(0, 0, 300, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
            btn.create_text(150, 18, text=neighborhood, fill=COLOR_TEXT, font=BODY_FONT)
            btn.bind("<Button-1>", lambda e, n=neighborhood: show_results(
                __import__('queries').filter_by_neighborhood(n, city),
                title=f"Galleries in {n}",
                show_neighborhood=False,
                back_command=lambda: show_home()
            ))
            btn.bind("<Enter>", lambda e, b=btn, r=rect: b.itemconfig(r, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
            btn.bind("<Leave>", lambda e, b=btn, r=rect: b.itemconfig(r, fill=COLOR_WHITE, outline=COLOR_BORDER))
            btn.pack(pady=4)

    tk.Canvas(scroll_frame, width=300, height=1, bg=COLOR_BORDER, highlightthickness=0).pack(pady=8)

    back_btn = tk.Canvas(scroll_frame, width=300, height=36, bg=COLOR_BG, highlightthickness=0)
    back_btn.create_text(150, 18, text="← Back", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_home())
    back_btn.pack(pady=4)
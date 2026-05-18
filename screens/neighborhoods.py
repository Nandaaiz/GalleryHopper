import tkinter as tk
from styles import *

def setup_neighborhoods(frame, tree, show_results, show_home):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Choose a Neighborhood", font=SUBHEAD_FONT).pack(pady=20)

    canvas = tk.Canvas(frame)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((400, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    neighborhoods = sorted(set(g.neighborhood for g in tree.list_all()))

    for neighborhood in neighborhoods:
        tk.Button(
            scroll_frame,
            text=neighborhood,
            width=BUTTON_WIDTH,
            command=lambda n=neighborhood: show_results(
                [g for g in tree.list_all() if g.neighborhood == n],
                title=f"Galleries in {n}",
                show_neighborhood=False
            )
        ).pack(pady=3)

    tk.Button(scroll_frame, text="← Back", width=BUTTON_WIDTH, command=show_home).pack(pady=20)
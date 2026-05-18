import tkinter as tk
from styles import *

def setup_styles(frame, tree, show_results, show_home):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Choose an Art Style", font=SUBHEAD_FONT).pack(pady=20)

    canvas = tk.Canvas(frame)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((400, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    styles = set()
    for g in tree.list_all():
        for s in g.art_style:
            styles.add(s)

    for style in sorted(styles):
        tk.Button(
            scroll_frame,
            text=style,
            width=BUTTON_WIDTH,
            command=lambda s=style: show_results(
                [g for g in tree.list_all() if s.lower() in [x.lower() for x in g.art_style]],
                title=f"Galleries — {s}"
            )
        ).pack(pady=2)

    tk.Button(scroll_frame, text="← Back", width=BUTTON_WIDTH, command=show_home).pack(pady=20)
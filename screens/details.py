import tkinter as tk
from styles import *

def setup_details(frame, gallery, show_results):
    for widget in frame.winfo_children():
        widget.destroy()

    type_label = "🏛 Museum" if gallery.type == "museum" else "🖼 Gallery"

    # scrollable area
    canvas = tk.Canvas(frame, bg=COLOR_BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=40)
    scrollbar.pack(side="right", fill="y")

    # type
    tk.Label(scroll_frame, text=type_label, font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor="w", pady=(30, 4))

    # name
    tk.Label(scroll_frame, text=gallery.name, font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT, wraplength=600).pack(anchor="w", pady=(0, 24))

    # divider
    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # location
    tk.Label(scroll_frame, text="LOCATION", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text=gallery.neighborhood, font=BODY_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # art styles
    tk.Label(scroll_frame, text="ART STYLES", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 6))
    styles_frame = tk.Frame(scroll_frame, bg=COLOR_BG)
    styles_frame.pack(anchor="w")
    for style in gallery.art_style:
        tk.Label(styles_frame, text=style, font=SMALL_FONT, bg=COLOR_ACCENT_LT, fg=COLOR_ACCENT, padx=8, pady=4).pack(side="left", padx=4, pady=2)

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # getting there
    tk.Label(scroll_frame, text="🚇 GETTING THERE", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text="Coming soon — subway lines near this gallery", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # current exhibitions
    tk.Label(scroll_frame, text="🎭 CURRENT EXHIBITIONS", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text="No information available at the moment.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # upcoming exhibitions
    tk.Label(scroll_frame, text="📅 UPCOMING EXHIBITIONS", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text="No information available at the moment.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=16)

    # back button
    back_btn = tk.Canvas(scroll_frame, width=200, height=36, bg=COLOR_BG, highlightthickness=0)
    rect = back_btn.create_rectangle(0, 0, 200, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
    back_btn.create_text(100, 18, text="← Back to Results", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_results())
    back_btn.bind("<Enter>", lambda e: back_btn.itemconfig(rect, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    back_btn.bind("<Leave>", lambda e: back_btn.itemconfig(rect, fill=COLOR_WHITE, outline=COLOR_BORDER))
    back_btn.pack(anchor="w", pady=(0, 30))
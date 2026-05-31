import tkinter as tk
from styles import *

def make_button(parent, text, command, bg, fg, width=300):
    canvas = tk.Canvas(parent, width=width, height=36, bg=parent["bg"], highlightthickness=0)
    rect = canvas.create_rectangle(0, 0, width, 36, fill=bg, outline=bg)
    label = canvas.create_text(width/2, 18, text=text, fill=fg, font=BODY_FONT)
    canvas.bind("<Button-1>", lambda e: command())
    canvas.bind("<Enter>", lambda e: canvas.itemconfig(rect, fill=COLOR_ACCENT_LT if bg != COLOR_ACCENT else "#3a4e2c"))
    canvas.bind("<Leave>", lambda e: canvas.itemconfig(rect, fill=bg))
    return canvas

def setup_home(frame, entry_search, load_neighborhoods, load_styles, list_all, show_frame, frame_neighborhoods, frame_styles, quit_app):

    tk.Label(frame, text="GalleryHopper", font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=30)
    tk.Label(frame, text="Find art galleries in NYC", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=4)

    entry_search.configure(font=BODY_FONT, relief="solid", bd=1)
    entry_search.pack(pady=20)

    make_button(frame, "List by Neighborhood", lambda: [load_neighborhoods(), show_frame(frame_neighborhoods)], "white", COLOR_TEXT).pack(pady=4)
    make_button(frame, "List by Art Style", lambda: [load_styles(), show_frame(frame_styles)], "white", COLOR_TEXT).pack(pady=4)
    make_button(frame, "List All Galleries", list_all, "white", COLOR_TEXT).pack(pady=4)
    make_button(frame, "Exit", quit_app, COLOR_BG, COLOR_GRAY, width=150).pack(pady=16)
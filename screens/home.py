import tkinter as tk
from styles import *

def make_button(parent, text, command, bg, fg, width=300):
    canvas = tk.Canvas(parent, width=width, height=36, bg=parent["bg"], highlightthickness=0)
    rect = canvas.create_rectangle(0, 0, width, 36, fill=bg, outline=bg)
    canvas.create_text(width/2, 18, text=text, fill=fg, font=BODY_FONT)
    canvas.bind("<Button-1>", lambda e: command())
    canvas.bind("<Enter>", lambda e: canvas.itemconfig(rect, fill=COLOR_ACCENT_LT if bg != COLOR_ACCENT else "#3a4e2c"))
    canvas.bind("<Leave>", lambda e: canvas.itemconfig(rect, fill=bg))
    return canvas

def setup_home(frame, load_neighborhoods, load_styles, list_all, show_frame, frame_neighborhoods, frame_styles, quit_app, load_profile=None, load_route=None, current_city=None, current_lang=None, set_city=None, set_lang=None, search_by_name=None):

    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="GalleryHopper", font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=(20, 4))

    # ── City selector ─────────────────────────────────
    city_frame = tk.Frame(frame, bg=COLOR_BG)
    city_frame.pack(pady=4)

    city = current_city["value"] if current_city else "New York"

    nyc_bg = COLOR_ACCENT if city == "New York" else COLOR_WHITE
    nyc_fg = "white" if city == "New York" else COLOR_TEXT
    sp_bg = COLOR_ACCENT if city == "São Paulo" else COLOR_WHITE
    sp_fg = "white" if city == "São Paulo" else COLOR_TEXT

    nyc_btn = tk.Canvas(city_frame, width=140, height=30, bg=COLOR_BG, highlightthickness=0)
    nyc_rect = nyc_btn.create_rectangle(0, 0, 140, 30, fill=nyc_bg, outline=COLOR_BORDER)
    nyc_btn.create_text(70, 15, text="🗽 New York", fill=nyc_fg, font=SMALL_FONT)
    nyc_btn.bind("<Button-1>", lambda e: set_city("New York") if set_city else None)
    nyc_btn.pack(side="left", padx=4)

    sp_btn = tk.Canvas(city_frame, width=140, height=30, bg=COLOR_BG, highlightthickness=0)
    sp_rect = sp_btn.create_rectangle(0, 0, 140, 30, fill=sp_bg, outline=COLOR_BORDER)
    sp_btn.create_text(70, 15, text="🌿 São Paulo", fill=sp_fg, font=SMALL_FONT)
    sp_btn.bind("<Button-1>", lambda e: set_city("São Paulo") if set_city else None)
    sp_btn.pack(side="left", padx=4)

    # ── Language selector ─────────────────────────────
    lang_frame = tk.Frame(frame, bg=COLOR_BG)
    lang_frame.pack(pady=2)

    lang = current_lang["value"] if current_lang else "EN"

    en_bg = COLOR_ACCENT if lang == "EN" else COLOR_WHITE
    en_fg = "white" if lang == "EN" else COLOR_TEXT
    pt_bg = COLOR_ACCENT if lang == "PT" else COLOR_WHITE
    pt_fg = "white" if lang == "PT" else COLOR_TEXT

    en_btn = tk.Canvas(lang_frame, width=60, height=26, bg=COLOR_BG, highlightthickness=0)
    en_btn.create_rectangle(0, 0, 60, 26, fill=en_bg, outline=COLOR_BORDER)
    en_btn.create_text(30, 13, text="EN", fill=en_fg, font=SMALL_FONT)
    en_btn.bind("<Button-1>", lambda e: set_lang("EN") if set_lang else None)
    en_btn.pack(side="left", padx=2)

    pt_btn = tk.Canvas(lang_frame, width=60, height=26, bg=COLOR_BG, highlightthickness=0)
    pt_btn.create_rectangle(0, 0, 60, 26, fill=pt_bg, outline=COLOR_BORDER)
    pt_btn.create_text(30, 13, text="PT", fill=pt_fg, font=SMALL_FONT)
    pt_btn.bind("<Button-1>", lambda e: set_lang("PT") if set_lang else None)
    pt_btn.pack(side="left", padx=2)

    tk.Label(frame, text="Find art galleries in NYC & SP", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=4)

    # ── Search entry ──────────────────────────────────
    entry_search = tk.Entry(frame, width=40, font=BODY_FONT, bg=COLOR_WHITE, fg=COLOR_GRAY,
                            relief="flat", bd=0, highlightthickness=0,
                            insertbackground=COLOR_TEXT, justify="center")
    entry_search.insert(0, "Search by gallery name...")

    def on_click(e):
        if entry_search.get() == "Search by gallery name...":
            entry_search.delete(0, tk.END)
            entry_search.config(fg=COLOR_TEXT)

    def on_leave(e):
        if entry_search.get() == "":
            entry_search.insert(0, "Search by gallery name...")
            entry_search.config(fg=COLOR_GRAY)

    entry_search.bind("<FocusIn>", on_click)
    entry_search.bind("<FocusOut>", on_leave)
    if search_by_name:
        entry_search.bind("<Return>", lambda e: search_by_name(entry_search))
    entry_search.pack(pady=12)

    make_button(frame, "List by Neighborhood", lambda: [load_neighborhoods(), show_frame(frame_neighborhoods)], "white", COLOR_TEXT).pack(pady=4)
    make_button(frame, "List by Art Style", lambda: [load_styles(), show_frame(frame_styles)], "white", COLOR_TEXT).pack(pady=4)
    make_button(frame, "List All Galleries", list_all, "white", COLOR_TEXT).pack(pady=4)

    if load_route:
        make_button(frame, "Build a Route 🗺", load_route, COLOR_ACCENT, "white").pack(pady=4)

    make_button(frame, "Exit", quit_app, COLOR_BG, COLOR_GRAY, width=150).pack(pady=12)
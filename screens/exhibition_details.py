import tkinter as tk
from styles import *
from datetime import datetime

def setup_exhibition_details(frame, exhibition, show_gallery):
    for widget in frame.winfo_children():
        widget.destroy()

    # ── Scrollable area ───────────────────────────────
    canvas = tk.Canvas(frame, bg=COLOR_BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((400, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)
    scroll_frame.configure(width=600)

    canvas.pack(side="left", fill="both", expand=True, padx=40)
    scrollbar.pack(side="right", fill="y")

    # ── Header ────────────────────────────────────────
    tk.Label(scroll_frame, text="🎭 Exhibition", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor="w", pady=(30, 4))
    tk.Label(scroll_frame, text=exhibition.get("title"), font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT, wraplength=580).pack(anchor="w", pady=(0, 8))

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Artist ────────────────────────────────────────
    tk.Label(scroll_frame, text="ARTIST", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text=exhibition.get("artist"), font=BODY_FONT, bg=COLOR_BG, fg=COLOR_TEXT, wraplength=580).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Dates ─────────────────────────────────────────
    tk.Label(scroll_frame, text="DATES", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))

    def format_date(date_str):
        try:
            d = datetime.strptime(date_str, "%Y-%m-%d")
            return d.strftime("%B %d, %Y")
        except:
            return date_str

    start = format_date(exhibition.get('date_start', ''))
    end = format_date(exhibition.get('date_end', ''))
    tk.Label(scroll_frame, text=f"{start} — {end}", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Gallery ───────────────────────────────────────
    tk.Label(scroll_frame, text="GALLERY", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text=exhibition.get("gallery_name"), font=BODY_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Styles ────────────────────────────────────────
    tk.Label(scroll_frame, text="ART STYLES", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 6))
    styles_frame = tk.Frame(scroll_frame, bg=COLOR_BG)
    styles_frame.pack(anchor="w")
    for style in exhibition.get("style", []):
        tk.Label(styles_frame, text=style, font=SMALL_FONT, bg=COLOR_ACCENT_LT, fg=COLOR_ACCENT, padx=8, pady=4).pack(side="left", padx=4, pady=2)

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Description ───────────────────────────────────
    tk.Label(scroll_frame, text="ABOUT", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 6))
    description = exhibition.get("description", "No description available.")
    tk.Label(scroll_frame, text=description, font=BODY_FONT, bg=COLOR_BG, fg=COLOR_TEXT, wraplength=560, justify="left").pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=16)

    # ── Back button ───────────────────────────────────
    back_btn = tk.Canvas(scroll_frame, width=220, height=36, bg=COLOR_BG, highlightthickness=0)
    rect = back_btn.create_rectangle(0, 0, 220, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
    back_btn.create_text(110, 18, text="← Back to Gallery", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_gallery())
    back_btn.bind("<Enter>", lambda e: back_btn.itemconfig(rect, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    back_btn.bind("<Leave>", lambda e: back_btn.itemconfig(rect, fill=COLOR_WHITE, outline=COLOR_BORDER))
    back_btn.pack(anchor="w", pady=(0, 30))
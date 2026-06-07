import tkinter as tk
from styles import *

def setup_details(frame, gallery, show_results, current_user={}):
    for widget in frame.winfo_children():
        widget.destroy()

    type_label = "🏛 Museum" if gallery.get("type") == "museum" else "🖼 Gallery"

    canvas = tk.Canvas(frame, bg=COLOR_BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((400, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)
    scroll_frame.configure(width=600)

    canvas.pack(side="left", fill="both", expand=True, padx=40)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scroll_frame, text=type_label, font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor="w", pady=(30, 4))
    tk.Label(scroll_frame, text=gallery.get("name"), font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT, wraplength=600).pack(anchor="w", pady=(0, 24))

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    tk.Label(scroll_frame, text="LOCATION", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text=gallery.get("neighborhood"), font=BODY_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    tk.Label(scroll_frame, text="ART STYLES", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 6))
    styles_frame = tk.Frame(scroll_frame, bg=COLOR_BG)
    styles_frame.pack(anchor="w")
    for style in gallery.get("art_style", []):
        tk.Label(styles_frame, text=style, font=SMALL_FONT, bg=COLOR_ACCENT_LT, fg=COLOR_ACCENT, padx=8, pady=4).pack(side="left", padx=4, pady=2)

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    tk.Label(scroll_frame, text="🚇 GETTING THERE", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text="Coming soon — subway lines near this gallery", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    tk.Label(scroll_frame, text="🎭 CURRENT EXHIBITIONS", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text="No information available at the moment.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    tk.Label(scroll_frame, text="📅 UPCOMING EXHIBITIONS", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text="No information available at the moment.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=16)

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # Mark as visited button
    def mark_visited():
        if current_user.get("email"):
            from user import user_manager
            user_manager.add_to_visited(current_user["email"], gallery.get("name"))
            visited_btn.itemconfig(visited_rect, fill=COLOR_ACCENT)
            visited_btn.itemconfig(visited_text, fill="white", text="✓ Visited!")

    visited_btn = tk.Canvas(scroll_frame, width=200, height=36, bg=COLOR_BG, highlightthickness=0)
    visited_rect = visited_btn.create_rectangle(0, 0, 200, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
    visited_text = visited_btn.create_text(100, 18, text="Mark as Visited", fill=COLOR_TEXT, font=SMALL_FONT)
    visited_btn.bind("<Button-1>", lambda e: mark_visited())
    visited_btn.bind("<Enter>",
                     lambda e: visited_btn.itemconfig(visited_rect, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    visited_btn.bind("<Leave>", lambda e: visited_btn.itemconfig(visited_rect, fill=COLOR_WHITE, outline=COLOR_BORDER))
    visited_btn.pack(anchor="w", pady=(0, 8))

    back_btn = tk.Canvas(scroll_frame, width=200, height=36, bg=COLOR_BG, highlightthickness=0)
    rect = back_btn.create_rectangle(0, 0, 200, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
    back_btn.create_text(100, 18, text="← Back to Results", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_results())
    back_btn.bind("<Enter>", lambda e: back_btn.itemconfig(rect, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    back_btn.bind("<Leave>", lambda e: back_btn.itemconfig(rect, fill=COLOR_WHITE, outline=COLOR_BORDER))
    back_btn.pack(anchor="w", pady=(0, 30))
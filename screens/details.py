import tkinter as tk
from styles import *
from exhibition import get_exhibitions_by_gallery

def setup_details(frame, gallery, show_results, current_user={}):
    for widget in frame.winfo_children():
        widget.destroy()

    type_label = "🏛 Museum" if gallery.get("type") == "museum" else "🖼 Gallery"

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
    tk.Label(scroll_frame, text=type_label, font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor="w", pady=(30, 4))
    tk.Label(scroll_frame, text=gallery.get("name"), font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT, wraplength=600).pack(anchor="w", pady=(0, 24))

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Location ──────────────────────────────────────
    tk.Label(scroll_frame, text="LOCATION", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text=gallery.get("neighborhood"), font=BODY_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(anchor="w")
    if gallery.get("address"):
        tk.Label(scroll_frame, text=gallery.get("address"), font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Hours & Admission ─────────────────────────────
    tk.Label(scroll_frame, text="HOURS & ADMISSION", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    hours = gallery.get("hours", "Check website for current hours")
    admission = gallery.get("admission", "Check website")
    tk.Label(scroll_frame, text=f"🕐 {hours}", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_TEXT, wraplength=550).pack(anchor="w")
    tk.Label(scroll_frame, text=f"🎟 {admission}", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_TEXT, wraplength=550).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Art Styles ────────────────────────────────────
    tk.Label(scroll_frame, text="ART STYLES", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 6))
    styles_frame = tk.Frame(scroll_frame, bg=COLOR_BG)
    styles_frame.pack(anchor="w")
    for style in gallery.get("art_style", []):
        tk.Label(styles_frame, text=style, font=SMALL_FONT, bg=COLOR_ACCENT_LT, fg=COLOR_ACCENT, padx=8, pady=4).pack(side="left", padx=4, pady=2)

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Getting There ─────────────────────────────────
    tk.Label(scroll_frame, text="🚇 GETTING THERE", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 2))
    tk.Label(scroll_frame, text="Coming soon — subway lines near this gallery", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    # ── Exhibitions ───────────────────────────────────
    tk.Label(scroll_frame, text="🎭 EXHIBITIONS", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", pady=(8, 6))

    exhibitions = get_exhibitions_by_gallery(gallery.get("name"))

    if exhibitions:
        for ex in exhibitions:
            ex_frame = tk.Frame(scroll_frame, bg=COLOR_ACCENT_LT, pady=8)
            ex_frame.pack(fill="x", pady=4)

            tk.Label(ex_frame, text=ex.get("title"), font=DETAIL_FONT, bg=COLOR_ACCENT_LT, fg=COLOR_TEXT, wraplength=500).pack(anchor="w", padx=12)
            tk.Label(ex_frame, text=f"Artist: {ex.get('artist')}", font=SMALL_FONT, bg=COLOR_ACCENT_LT, fg=COLOR_GRAY, wraplength=500).pack(anchor="w", padx=12)
            tk.Label(ex_frame, text=f"{ex.get('date_start')} → {ex.get('date_end')}", font=SMALL_FONT, bg=COLOR_ACCENT_LT, fg=COLOR_ACCENT).pack(anchor="w", padx=12, pady=(2, 0))

            # Mark exhibition as visited
            def mark_ex_visited(ex_title=ex.get("title")):
                if current_user.get("email"):
                    from user import user_manager
                    user_manager.add_to_visited(current_user["email"], ex_title)
                    visited_label.config(text="✓ Marked as visited!", fg=COLOR_ACCENT)
                else:
                    visited_label.config(text="Create an account to use this feature!", fg=COLOR_GRAY)

            visited_label = tk.Label(ex_frame, text="", font=SMALL_FONT, bg=COLOR_ACCENT_LT, fg=COLOR_ACCENT)
            visited_label.pack(anchor="w", padx=12)

            mark_btn = tk.Canvas(ex_frame, width=180, height=28, bg=COLOR_ACCENT_LT, highlightthickness=0)
            rect = mark_btn.create_rectangle(0, 0, 180, 28, fill=COLOR_WHITE, outline=COLOR_BORDER)
            mark_btn.create_text(90, 14, text="Mark as Visited", fill=COLOR_TEXT, font=SMALL_FONT)
            mark_btn.bind("<Button-1>", lambda e, t=ex.get("title"): mark_ex_visited(t))
            mark_btn.bind("<Enter>", lambda e, b=mark_btn, r=rect: b.itemconfig(r, fill=COLOR_ACCENT_LT))
            mark_btn.bind("<Leave>", lambda e, b=mark_btn, r=rect: b.itemconfig(r, fill=COLOR_WHITE))
            mark_btn.pack(anchor="w", padx=12, pady=(4, 8))
    else:
        tk.Label(scroll_frame, text="No exhibitions available at the moment.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=16)

    # ── Back button ───────────────────────────────────
    back_btn = tk.Canvas(scroll_frame, width=200, height=36, bg=COLOR_BG, highlightthickness=0)
    rect = back_btn.create_rectangle(0, 0, 200, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
    back_btn.create_text(100, 18, text="← Back to Results", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_results())
    back_btn.bind("<Enter>", lambda e: back_btn.itemconfig(rect, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    back_btn.bind("<Leave>", lambda e: back_btn.itemconfig(rect, fill=COLOR_WHITE, outline=COLOR_BORDER))
    back_btn.pack(anchor="w", pady=(0, 30))
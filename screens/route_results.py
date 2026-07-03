import tkinter as tk
from styles import *

def setup_route_results(frame, selected_styles, galleries, show_home, show_details):
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
    tk.Label(scroll_frame, text="Your Route", font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(anchor="w", pady=(30, 4))
    tk.Label(scroll_frame, text=f"Styles: {', '.join(selected_styles)}", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w")

    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=12)

    if not galleries:
        tk.Label(scroll_frame, text="No galleries found for the selected styles.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=20)
    else:
        # ── Group by neighborhood ─────────────────────
        by_neighborhood = {}
        for g in galleries:
            hood = g.get("neighborhood", "Other")
            if hood not in by_neighborhood:
                by_neighborhood[hood] = []
            by_neighborhood[hood].append(g)

        for neighborhood, hood_galleries in sorted(by_neighborhood.items()):
            # Neighborhood header
            tk.Label(scroll_frame, text=f"📍 {neighborhood}", font=SUBHEAD_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(anchor="w", pady=(12, 4))

            for g in hood_galleries:
                g_frame = tk.Frame(scroll_frame, bg=COLOR_WHITE, pady=10)
                g_frame.pack(fill="x", pady=3)

                # Gallery name
                tk.Label(g_frame, text=g.get("name"), font=BODY_FONT, bg=COLOR_WHITE, fg=COLOR_TEXT).pack(anchor="w", padx=12)

                # Matching styles
                g_styles = [s for s in g.get("art_style", []) if s in selected_styles]
                tk.Label(g_frame, text=f"Matches: {', '.join(g_styles)}", font=SMALL_FONT, bg=COLOR_WHITE, fg=COLOR_ACCENT).pack(anchor="w", padx=12)

                # Full match warning
                matching_count = len(g_styles)
                if matching_count > 1:
                    tk.Label(g_frame, text=f"⚠️ This gallery has {matching_count} of your chosen styles!", font=SMALL_FONT, bg=COLOR_WHITE, fg=COLOR_GRAY).pack(anchor="w", padx=12)

                g_frame.bind("<Button-1>", lambda e, gallery=g: show_details(gallery))
                for child in g_frame.winfo_children():
                    child.bind("<Button-1>", lambda e, gallery=g: show_details(gallery))

            tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=6)

    # ── Back button ───────────────────────────────────
    back_btn = tk.Canvas(scroll_frame, width=200, height=36, bg=COLOR_BG, highlightthickness=0)
    rect = back_btn.create_rectangle(0, 0, 200, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
    back_btn.create_text(100, 18, text="← Home", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_home())
    back_btn.bind("<Enter>", lambda e: back_btn.itemconfig(rect, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    back_btn.bind("<Leave>", lambda e: back_btn.itemconfig(rect, fill=COLOR_WHITE, outline=COLOR_BORDER))
    back_btn.pack(anchor="w", pady=(8, 30))
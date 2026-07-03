import tkinter as tk
from styles import *

def setup_route_builder(frame, all_styles, show_route, show_home):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Build a Route", font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=30)
    tk.Label(frame, text="Choose up to 3 art styles", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack()

    tk.Frame(frame, height=1, bg=COLOR_BORDER).pack(fill="x", padx=60, pady=16)

    selected = []
    selected_label = tk.Label(frame, text="Selected: none", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY)
    selected_label.pack(pady=4)

    msg_label = tk.Label(frame, text="", font=SMALL_FONT, bg=COLOR_BG, fg="red")
    msg_label.pack()

    # ── Scrollable style buttons ──────────────────────
    canvas = tk.Canvas(frame, bg=COLOR_BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((400, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    buttons = {}

    def toggle_style(style, btn, rect):
        if style in selected:
            selected.remove(style)
            btn.itemconfig(rect, fill=COLOR_WHITE, outline=COLOR_BORDER)
            btn.itemconfig(buttons[style]["text"], fill=COLOR_TEXT)
        else:
            if len(selected) >= 3:
                msg_label.config(text="You can only choose up to 3 styles!")
                return
            selected.append(style)
            btn.itemconfig(rect, fill=COLOR_ACCENT, outline=COLOR_ACCENT)
            btn.itemconfig(buttons[style]["text"], fill="white")
        msg_label.config(text="")
        if selected:
            selected_label.config(text=f"Selected: {', '.join(selected)}")
        else:
            selected_label.config(text="Selected: none")

    for style in all_styles:
        btn = tk.Canvas(scroll_frame, width=300, height=36, bg=COLOR_BG, highlightthickness=0)
        rect = btn.create_rectangle(0, 0, 300, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
        text = btn.create_text(150, 18, text=style, fill=COLOR_TEXT, font=BODY_FONT)
        btn.bind("<Button-1>", lambda e, s=style, b=btn, r=rect: toggle_style(s, b, r))
        btn.bind("<Enter>", lambda e, b=btn, r=rect: b.itemconfig(r, fill=COLOR_ACCENT_LT) if b.itemcget(r, "fill") == COLOR_WHITE else None)
        btn.bind("<Leave>", lambda e, b=btn, r=rect: b.itemconfig(r, fill=COLOR_WHITE) if b.itemcget(r, "fill") == COLOR_ACCENT_LT else None)
        btn.pack(pady=4)
        buttons[style] = {"btn": btn, "rect": rect, "text": text}

    # ── Bottom buttons ────────────────────────────────
    tk.Frame(scroll_frame, height=1, bg=COLOR_BORDER).pack(fill="x", pady=8)

    build_btn = tk.Canvas(scroll_frame, width=300, height=36, bg=COLOR_BG, highlightthickness=0)
    rect_build = build_btn.create_rectangle(0, 0, 300, 36, fill=COLOR_ACCENT, outline=COLOR_ACCENT)
    build_btn.create_text(150, 18, text="Build Route →", fill="white", font=BODY_FONT)
    build_btn.bind("<Button-1>", lambda e: show_route(selected) if selected else msg_label.config(text="Please select at least 1 style!"))
    build_btn.bind("<Enter>", lambda e: build_btn.itemconfig(rect_build, fill="#3a4e2c"))
    build_btn.bind("<Leave>", lambda e: build_btn.itemconfig(rect_build, fill=COLOR_ACCENT))
    build_btn.pack(pady=4)

    back_btn = tk.Canvas(scroll_frame, width=300, height=36, bg=COLOR_BG, highlightthickness=0)
    back_btn.create_text(150, 18, text="← Back", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_home())
    back_btn.pack(pady=4)
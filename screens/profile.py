import tkinter as tk
from styles import *
from user import user_manager
from database import db

users_collection = db["users"]

def setup_profile(frame, current_user, show_home, show_results):
    for widget in frame.winfo_children():
        widget.destroy()

    # Header
    header = tk.Frame(frame, bg=COLOR_BG)
    header.pack(fill="x", padx=40, pady=(20, 0))

    tk.Label(header, text="My Profile", font=HEADING_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(side="left")

    back_btn = tk.Canvas(header, width=80, height=32, bg=COLOR_BG, highlightthickness=0)
    rect_back = back_btn.create_rectangle(0, 0, 80, 32, fill=COLOR_WHITE, outline=COLOR_BORDER)
    back_btn.create_text(40, 16, text="← Home", fill=COLOR_GRAY, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_home())
    back_btn.bind("<Enter>", lambda e: back_btn.itemconfig(rect_back, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    back_btn.bind("<Leave>", lambda e: back_btn.itemconfig(rect_back, fill=COLOR_WHITE, outline=COLOR_BORDER))
    back_btn.pack(side="right")

    tk.Frame(frame, height=1, bg=COLOR_BORDER).pack(fill="x", padx=40, pady=12)

    # User info
    user = users_collection.find_one({"email": current_user.get("email")})

    tk.Label(frame, text=user.get("name", ""), font=SUBHEAD_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=4)
    tk.Label(frame, text=user.get("email", ""), font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack()

    tk.Frame(frame, height=1, bg=COLOR_BORDER).pack(fill="x", padx=40, pady=16)

    # Visited galleries
    tk.Label(frame, text="VISITED GALLERIES", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="w", padx=40, pady=(0, 8))

    visited = user.get("visited", [])

    # Scrollable area
    canvas = tk.Canvas(frame, bg=COLOR_BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((400, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=40)
    scrollbar.pack(side="right", fill="y")

    if visited:
        import queries
        for i, name in enumerate(visited):
            gallery = queries.search_by_name(name)
            if gallery:
                type_label = "🏛 Museum" if gallery.get("type") == "museum" else "🖼 Gallery"
                item_frame = tk.Frame(scroll_frame, bg=COLOR_WHITE, pady=12)
                item_frame.grid(row=i//2, column=i%2, pady=4, padx=4, sticky="nsew")
                scroll_frame.grid_columnconfigure(0, weight=1, minsize=200)
                scroll_frame.grid_columnconfigure(1, weight=1, minsize=200)
                tk.Label(item_frame, text=type_label, font=SMALL_FONT, bg=COLOR_WHITE, fg=COLOR_ACCENT).pack(anchor="w", padx=16)
                tk.Label(item_frame, text=gallery.get("name"), font=BODY_FONT, bg=COLOR_WHITE, fg=COLOR_TEXT).pack(anchor="w", padx=16)
                tk.Label(item_frame, text=gallery.get("neighborhood"), font=SMALL_FONT, bg=COLOR_WHITE, fg=COLOR_GRAY).pack(anchor="w", padx=16, pady=(0,8))
                item_frame.bind("<Button-1>", lambda e, g=gallery: show_results([g], title=g.get("name", "")))
                for child in item_frame.winfo_children():
                    child.bind("<Button-1>", lambda e, g=gallery: show_results([g], title=g.get("name", "")))
    else:
        tk.Label(scroll_frame, text="No galleries visited yet.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=20)
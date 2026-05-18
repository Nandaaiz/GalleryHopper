import tkinter as tk
from styles import *

def setup_details(frame, gallery, show_results):
    for widget in frame.winfo_children():
        widget.destroy()

    type_label = "🏛 Museum" if gallery.type == "museum" else "🖼 Gallery"

    tk.Label(frame, text=gallery.name, font=TITLE_FONT).pack(pady=20)
    tk.Label(frame, text=type_label, font=BODY_FONT).pack()

    tk.Frame(frame, height=1, bg=COLOR_GRAY).pack(fill="x", padx=20, pady=10)

    tk.Label(frame, text="📍 Location", font=DETAIL_FONT).pack(anchor="w", padx=30)
    tk.Label(frame, text=gallery.neighborhood, font=BODY_FONT).pack(anchor="w", padx=40)

    tk.Frame(frame, height=1, bg=COLOR_GRAY).pack(fill="x", padx=20, pady=10)

    tk.Label(frame, text="🎨 Art Styles", font=DETAIL_FONT).pack(anchor="w", padx=30)
    tk.Label(frame, text=", ".join(gallery.art_style), font=BODY_FONT, wraplength=600).pack(anchor="w", padx=40)

    tk.Frame(frame, height=1, bg=COLOR_GRAY).pack(fill="x", padx=20, pady=10)

    tk.Label(frame, text="🚇 Getting There", font=DETAIL_FONT).pack(anchor="w", padx=30)
    tk.Label(frame, text="Coming soon — subway lines near this gallery", font=BODY_FONT, fg=COLOR_GRAY).pack(anchor="w", padx=40)

    tk.Frame(frame, height=1, bg=COLOR_GRAY).pack(fill="x", padx=20, pady=10)

    tk.Label(frame, text="🎭 Current Exhibitions", font=DETAIL_FONT).pack(anchor="w", padx=30)
    tk.Label(frame, text="No information available at the moment.", font=BODY_FONT, fg=COLOR_GRAY).pack(anchor="w", padx=40)

    tk.Frame(frame, height=1, bg=COLOR_GRAY).pack(fill="x", padx=20, pady=10)

    tk.Label(frame, text="📅 Upcoming Exhibitions", font=DETAIL_FONT).pack(anchor="w", padx=30)
    tk.Label(frame, text="No information available at the moment.", font=BODY_FONT, fg=COLOR_GRAY).pack(anchor="w", padx=40)

    tk.Button(frame, text="← Back to Results", width=BUTTON_WIDTH, command=show_results).pack(pady=20)
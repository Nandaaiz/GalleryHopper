import tkinter as tk
from styles import *

def setup_home(frame, entry_search, search_by_name, load_neighborhoods, load_styles, list_all, show_frame, frame_neighborhoods, frame_styles, quit_app):

    tk.Label(frame, text="GalleryHopper", font=TITLE_FONT).pack(pady=20)
    tk.Label(frame, text="Find art galleries in NYC", font=("Helvetica", 14)).pack()

    entry_search.pack(pady=10)

    tk.Button(frame, text="Search by Name", width=BUTTON_WIDTH, command=search_by_name).pack(pady=5)
    tk.Button(frame, text="Filter by Neighborhood", width=BUTTON_WIDTH, command=lambda: [load_neighborhoods(), show_frame(frame_neighborhoods)]).pack(pady=5)
    tk.Button(frame, text="Filter by Art Style", width=BUTTON_WIDTH, command=lambda: [load_styles(), show_frame(frame_styles)]).pack(pady=5)
    tk.Button(frame, text="List All Galleries", width=BUTTON_WIDTH, command=list_all).pack(pady=5)
    tk.Button(frame, text="Exit", width=BUTTON_WIDTH, command=quit_app).pack(pady=20)
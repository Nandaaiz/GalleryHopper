import tkinter as tk
from styles import *
from screens.home import setup_home
from screens.results import setup_results
from screens.details import setup_details
from screens.neighborhoods import setup_neighborhoods
from screens.styles_screen import setup_styles
from screens.login import setup_login
from screens.register import setup_register
from screens.profile import setup_profile
from session import save_session, load_session, clear_session
from database import db
import queries
from screens.exhibition_details import setup_exhibition_details
from screens.route_builder import setup_route_builder
from screens.route_results import setup_route_results

# ── window setup ─────────────────────────────────────
window = tk.Tk()
window.title(WINDOW_TITLE)
window.geometry(WINDOW_SIZE)
window.configure(bg=COLOR_BG)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# ── frames ────────────────────────────────────────────
frame_login         = tk.Frame(window, bg=COLOR_BG)
frame_register      = tk.Frame(window, bg=COLOR_BG)
frame_home          = tk.Frame(window, bg=COLOR_BG)
frame_neighborhoods = tk.Frame(window, bg=COLOR_BG)
frame_styles        = tk.Frame(window, bg=COLOR_BG)
frame_results       = tk.Frame(window, bg=COLOR_BG)
frame_details       = tk.Frame(window, bg=COLOR_BG)
frame_profile       = tk.Frame(window, bg=COLOR_BG)
frame_exhibition    = tk.Frame(window, bg=COLOR_BG)
frame_route_builder = tk.Frame(window, bg=COLOR_BG)
frame_route_results = tk.Frame(window, bg=COLOR_BG)

for frame in (frame_login, frame_register, frame_home, frame_neighborhoods, frame_styles, frame_results, frame_details, frame_profile, frame_exhibition, frame_route_builder, frame_route_results):
    frame.grid(row=0, column=0, sticky="nsew")

# ── current user ──────────────────────────────────────
current_user = {}

# ── city and language ─────────────────────────────────
current_city = {"value": "New York"}
current_lang = {"value": "EN"}

# ── helper ────────────────────────────────────────────
def show_frame(frame):
    frame.tkraise()

# ── show details ──────────────────────────────────────
def show_details(gallery):
    setup_details(
        frame_details,
        gallery,
        lambda: show_frame(frame_results),
        current_user,
        lambda ex: show_exhibition(ex, lambda: show_frame(frame_details)),
        current_lang["value"]
    )
    show_frame(frame_details)

def show_exhibition(exhibition, back_to_gallery):
    setup_exhibition_details(frame_exhibition, exhibition, back_to_gallery, current_lang["value"])
    show_frame(frame_exhibition)

# ── set back command ──────────────────────────────────
def set_back_command(command):
    back_btn.bind("<Button-1>", lambda e: command())

# ── show results ──────────────────────────────────────
def show_results(results, title="Results", show_neighborhood=True, back_command=None):
    label_results_title.config(text=title)
    if back_command:
        set_back_command(back_command)
    else:
        set_back_command(lambda: show_frame(frame_home))
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    if results:
        for i, g in enumerate(results):
            type_label = "🏛 Museum" if g.get("type") == "museum" else "🖼 Gallery"
            item_frame = tk.Frame(scroll_frame, bg=COLOR_WHITE, pady=12)
            item_frame.grid(row=i // 2, column=i % 2, pady=4, padx=20, sticky="nsew")
            scroll_frame.grid_columnconfigure(0, weight=1, minsize=200)
            scroll_frame.grid_columnconfigure(1, weight=1, minsize=200)
            tk.Label(item_frame, text=type_label, font=SMALL_FONT, bg=COLOR_WHITE, fg=COLOR_ACCENT).pack(anchor="w", padx=16)
            tk.Label(item_frame, text=g.get("name"), font=SUBHEAD_FONT, bg=COLOR_WHITE, fg=COLOR_TEXT).pack(anchor="w", padx=16)
            if show_neighborhood:
                tk.Label(item_frame, text=g.get("neighborhood"), font=DETAIL_FONT, bg=COLOR_WHITE, fg=COLOR_GRAY).pack(anchor="w", padx=16, pady=(0, 8))
            item_frame.bind("<Button-1>", lambda e, gallery=g: show_details(gallery))
            for child in item_frame.winfo_children():
                child.bind("<Button-1>", lambda e, gallery=g: show_details(gallery))
    else:
        tk.Label(scroll_frame, text="No results found.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).grid(row=0, column=0, columnspan=2, pady=40)
    show_frame(frame_results)

# ── search by name ────────────────────────────────────
def search_by_name(entry_search):
    name = entry_search.get()
    if not name or name == "Search by gallery name...":
        show_results([], title="Search Result")
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        tk.Label(scroll_frame, text="Please insert a gallery name.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).grid(row=0, column=0, columnspan=2, pady=40)
        show_frame(frame_results)
    else:
        result = queries.search_by_name(name)
        if result:
            show_results([result], title="Search Result")
        else:
            show_results([], title="Search Result")
            for widget in scroll_frame.winfo_children():
                widget.destroy()
            tk.Label(scroll_frame, text="Gallery not found.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).grid(row=0, column=0, columnspan=2, pady=40)
            show_frame(frame_results)

# ── route ─────────────────────────────────────────────
def load_route_builder():
    setup_route_builder(frame_route_builder, queries.get_all_styles(current_city["value"]), show_route_results, lambda: show_frame(frame_home))
    show_frame(frame_route_builder)

def show_route_results(selected_styles):
    if not selected_styles:
        return
    seen = set()
    galleries = []
    for style in selected_styles:
        for g in queries.filter_by_art_style(style, current_city["value"]):
            name = g.get("name")
            if name not in seen:
                seen.add(name)
                galleries.append(g)
    setup_route_results(frame_route_results, selected_styles, galleries, lambda: show_frame(frame_home), show_details)
    show_frame(frame_route_results)

# ── list all ──────────────────────────────────────────
def list_all():
    show_results(queries.list_all(current_city["value"]), title="All Galleries & Museums")

# ── load neighborhoods ────────────────────────────────
def load_neighborhoods():
    setup_neighborhoods(frame_neighborhoods, queries.get_all_neighborhoods(current_city["value"]), show_results, lambda: show_frame(frame_home), current_city["value"])

# ── load styles ───────────────────────────────────────
def load_styles():
    setup_styles(frame_styles, queries.get_all_styles(current_city["value"]), show_results, lambda: show_frame(frame_home), current_city["value"])

# ── load profile ──────────────────────────────────────
def load_profile():
    if current_user.get("email"):
        setup_profile(frame_profile, current_user, lambda: show_frame(frame_home), show_results)
        show_frame(frame_profile)
    else:
        show_frame(frame_login)

# ── city and lang setters ─────────────────────────────
def set_city(city):
    current_city["value"] = city
    refresh_home()

def set_lang(lang):
    current_lang["value"] = lang
    refresh_home()

def refresh_home():
    setup_home(
        frame_home, load_neighborhoods, load_styles,
        list_all, show_frame, frame_neighborhoods, frame_styles,
        window.quit, load_profile, load_route_builder,
        current_city, current_lang, set_city, set_lang,
        search_by_name
    )
    show_frame(frame_home)

# ── setup screens ─────────────────────────────────────
setup_home(
    frame_home, load_neighborhoods, load_styles,
    list_all, show_frame, frame_neighborhoods, frame_styles,
    window.quit, load_profile, load_route_builder,
    current_city, current_lang, set_city, set_lang,
    search_by_name
)

label_results_title, scroll_frame, back_btn = setup_results(
    frame_results,
    lambda: show_frame(frame_home)
)

# ── start ─────────────────────────────────────────────
show_frame(frame_home)
window.mainloop()
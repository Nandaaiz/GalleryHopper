# GalleryHopper 🗽🌿

A Python desktop app to discover art galleries and museums in New York City and São Paulo.

## About
GalleryHopper was created to make art more accessible and fun — helping users discover galleries and museums, explore current exhibitions, and plan visits. Built as a personal portfolio project, using a Binary Search Tree (BST) implemented from scratch in v1, and MongoDB Atlas in v2 for persistent data storage.

## Features
- 🔍 Search gallery or museum by name (with alias support — search "MET", "MoMA", "Whitney", "MASP")
- 📍 Browse by neighborhood
- 🎨 Browse by art style
- 🗺 Build a route — choose up to 3 art styles and get gallery suggestions grouped by neighborhood
- 🏛 List all galleries and museums
- 📋 Gallery details — location, address, hours, admission and current exhibitions
- 🎭 Exhibition details — artist, dates, description
- 🌆 City selector — New York or São Paulo
- 🌐 Language toggle — EN / PT for exhibition descriptions

## Tech Stack
- Python 3.12
- tkinter (GUI)
- MongoDB Atlas (database)
- pymongo + python-dotenv + certifi
- Binary Search Tree (BST) — implemented from scratch (v1)
- Object-Oriented Programming (OOP)
- bcrypt (password encryption — v2, ready for v3)

## Data
- 37 NYC galleries and museums across 8 neighborhoods
- 32 São Paulo galleries and museums across 12 neighborhoods
- 35+ real NYC exhibitions with descriptions
- 22+ real SP exhibitions with descriptions in EN and PT
- Hours, address and admission info for all venues

## Project Structure
GalleryHopper/
├── screens/
│ ├── home.py
│ ├── results.py
│ ├── details.py
│ ├── neighborhoods.py
│ ├── styles_screen.py
│ ├── login.py
│ ├── register.py
│ ├── profile.py
│ ├── exhibition_details.py
│ ├── route_builder.py
│ └── route_results.py
├── scripts/
│ ├── migrate.py
│ ├── update_galleries.py
│ ├── update_exhibitions.py
│ ├── add_new_galleries.py
│ ├── add_sp_galleries.py
│ └── remove_gallery.py
├── styles.py
├── app.py
├── database.py
├── queries.py
├── user.py
├── session.py
├── exhibition.py
├── bst.py
├── node.py
└── data.py


## Roadmap
- **V1** — BST + tkinter ✅
- **V2** — MongoDB + exhibitions system + route builder + São Paulo + EN/PT toggle ✅
- **V3** — Reactivate login and profile + Google Maps API + optimized route + web or mobile interface + admin panel for gallery registration

## Author
Developed by Ananda
GitHub: [Nandaaiz](https://github.com/Nandaaiz)
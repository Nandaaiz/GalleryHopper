from bst import BST

tree = BST()

from bst import BST

tree = BST()

# Chelsea — galleries
tree.insert("Gagosian Gallery", "Chelsea", ["Contemporary", "Modern Art", "Sculpture", "Painting"], "gallery")
tree.insert("David Zwirner", "Chelsea", ["Contemporary", "Photography", "Minimalism"], "gallery")
tree.insert("Hauser and Wirth", "Chelsea", ["Contemporary", "Modern Art", "Installation"], "gallery")
tree.insert("Pace Gallery", "Chelsea", ["Contemporary", "Photography", "Modern Art"], "gallery")
tree.insert("ACA Galleries", "Chelsea", ["Contemporary", "Painting", "Sculpture"], "gallery")
tree.insert("Berry Campbell", "Chelsea", ["American Art", "Painting", "Sculpture"], "gallery")
tree.insert("Luhring Augustine", "Chelsea", ["Contemporary", "Modern Art", "Painting"], "gallery")
tree.insert("Petzel Gallery", "Chelsea", ["Contemporary", "Painting", "Figurative"], "gallery")
tree.insert("Yancey Richardson Gallery", "Chelsea", ["Photography", "Contemporary"], "gallery")
tree.insert("Miles McEnery Gallery", "Chelsea", ["Contemporary", "Painting"], "gallery")

# Upper East Side — galleries
tree.insert("Galerie Buchholz", "Upper East Side", ["Modern Art", "Conceptual Art", "Sculpture"], "gallery")
tree.insert("Anita Shapolsky Gallery", "Upper East Side", ["Abstract Expressionism", "American Art"], "gallery")
tree.insert("White Cube New York", "Upper East Side", ["Contemporary", "Conceptual Art"], "gallery")
tree.insert("Alexander Berggruen", "Upper East Side", ["Contemporary", "Painting"], "gallery")
tree.insert("Spruth Magers", "Upper East Side", ["Conceptual Art", "Photography", "Contemporary"], "gallery")

# Upper East Side — museums
tree.insert("Solomon R. Guggenheim Museum", "Upper East Side", ["Impressionism", "Post-Impressionism", "Modern Art", "Contemporary"], "museum", ["Guggenheim", "Guggenheim Museum"])
tree.insert("The Metropolitan Museum of Art", "Upper East Side", ["Ancient Art", "Medieval Art", "Modern Art", "Contemporary", "Asian Art", "Fashion", "Global Art"], "museum", ["MET", "Metropolitan", "Met Museum"])

# Tribeca — galleries
tree.insert("Almine Rech", "Tribeca", ["Contemporary", "Painting", "International Art"], "gallery")
tree.insert("David Zwirner 52 Walker", "Tribeca", ["Contemporary", "Installation"], "gallery")
tree.insert("James Cohan Gallery", "Tribeca", ["Contemporary", "Global Art"], "gallery")

# Midtown — museums
tree.insert("Museum of Modern Art MoMA", "Midtown", ["Modern Art", "Contemporary", "Design", "Photography", "Film"], "museum", ["MoMA", "MOMA", "Museum of Modern Art"])

# Lower East Side — galleries
tree.insert("The Foundation of ART NYC", "Lower East Side", ["Contemporary", "Painting", "Installation"], "gallery")
tree.insert("Sperone Westwater", "Lower East Side", ["Contemporary", "Arte Povera", "American Art"], "gallery")

# Lower East Side — museums
tree.insert("New Museum", "Lower East Side", ["Contemporary", "Experimental Art", "Performance"], "museum", ["New Museum of Contemporary Art"])

# Brooklyn — galleries
tree.insert("CARVALHO", "Brooklyn", ["Contemporary", "Painting", "Sculpture"], "gallery")
tree.insert("Aidron Duckworth Gallery", "Brooklyn", ["Street Art", "Graffiti", "Experimental Art"], "gallery")
tree.insert("Ortega y Gasset Projects", "Brooklyn", ["Contemporary", "Experimental Art"], "gallery")
tree.insert("Smack Mellon", "Brooklyn", ["Contemporary", "Installation", "Experimental Art"], "gallery")
tree.insert("Platform Project Space", "Brooklyn", ["Contemporary", "Textile Art", "Painting"], "gallery")
tree.insert("AIR Gallery", "Brooklyn", ["Feminist Art", "Contemporary"], "gallery")
tree.insert("Amant", "Brooklyn", ["Experimental Art", "Performance", "Sound Art"], "gallery")
tree.insert("Art Cake", "Brooklyn", ["Abstract Art", "American Art"], "gallery")

# Queens — galleries
tree.insert("Mrs.", "Queens", ["Contemporary", "Painting"], "gallery")
tree.insert("Culture Lab LIC", "Queens", ["Community Art", "Contemporary"], "gallery")

# Meatpacking — museums
tree.insert("Whitney Museum of American Art", "Meatpacking", ["American Art", "Contemporary", "Abstract Expressionism", "Pop Art"], "museum", ["Whitney", "Whitney Museum"])


# Menu functions

def show_results(results):
    text_results.delete("1.0", tk.END)
    if results:
        for g in results:
            type_label = "🏛 Museum" if g.type == "museum" else "🖼 Gallery"
            text_results.insert(tk.END, f"{type_label} | {g.name} - {g.neighborhood} - {', '.join(g.art_style)}\n")
    else:
        text_results.insert(tk.END, "No galleries found.")

def search_by_name(tree):
    name = input("Enter gallery name: ")
    result = tree.search(name)
    if result:
        print("Found:", result.name, "-", result.neighborhood, "-", ", ".join(result.art_style))
    else:
        print("Gallery not found.")

def filter_by_neighborhood(tree):
    neighborhood = input("Enter neighborhood: ").lower()
    results = [g for g in tree.list_all() if g.neighborhood.lower() == neighborhood]
    if results:
        for g in results:
            print("-", g.name, "-", ", ".join(g.art_style))
    else:
        print("No galleries found in this neighborhood.")

def filter_by_art_style(tree):
    style = input("Enter art style: ").lower()
    results = [g for g in tree.list_all() if style in [s.lower() for s in g.art_style]]
    if results:
        for g in results:
            print("-", g.name, "-", g.neighborhood)
    else:
        print("No galleries found with this art style.")

def list_all(tree):
    print("\nAll galleries in alphabetical order:")
    for g in tree.list_all():
        print("-", g.name, "-", g.neighborhood, "-", ", ".join(g.art_style))

def list_all_styles(tree):
    styles = set()
    for g in tree.list_all():
        for style in g.art_style:
            styles.add(style)
    sorted_styles = sorted(styles)
    print("\nAvailable art styles:")
    for i, style in enumerate(sorted_styles, 1):
        print(f"{i}. {style}")
    choice = input("\nEnter the number to explore a style (or 0 to go back): ")
    if choice == "0":
        return
    if choice.isdigit() and 1 <= int(choice) <= len(sorted_styles):
        selected = sorted_styles[int(choice) - 1]
        results = [g for g in tree.list_all() if selected.lower() in [s.lower() for s in g.art_style]]
        print(f"\nGalleries with '{selected}':")
        for g in results:
            print("-", g.name, "-", g.neighborhood)
    else:
        print("Invalid option.")

def menu():
    while True:
        print("\n=== GalleryHopper ===")
        print("1. Search gallery by name")
        print("2. Filter by neighborhood")
        print("3. Filter by art style")
        print("4. List all galleries")
        print("5. Show all art styles")
        print("0. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            search_by_name(tree)
        elif option == "2":
            filter_by_neighborhood(tree)
        elif option == "3":
            filter_by_art_style(tree)
        elif option == "4":
            list_all(tree)
        elif option == "5":
            list_all_styles(tree)
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# menu()

# Menu functions

def search_by_name(tree):
    name = input("Enter gallery name: ")
    result = tree.search(name)
    if result:
        print("Found:", result.name, "-", result.neighborhood, "-", ", ".join(result.art_style))
    else:
        print("Gallery not found.")

def filter_by_neighborhood(tree):
    neighborhood = input("Enter neighborhood: ").lower()
    results = [g for g in tree.list_all() if g.neighborhood.lower() == neighborhood]
    if results:
        for g in results:
            print("-", g.name, "-", ", ".join(g.art_style))
    else:
        print("No galleries found in this neighborhood.")

def filter_by_art_style(tree):
    style = input("Enter art style: ").lower()
    results = [g for g in tree.list_all() if style in [s.lower() for s in g.art_style]]
    if results:
        for g in results:
            print("-", g.name, "-", g.neighborhood)
    else:
        print("No galleries found with this art style.")

def list_all(tree):
    print("\nAll galleries in alphabetical order:")
    for g in tree.list_all():
        print("-", g.name, "-", g.neighborhood, "-", ", ".join(g.art_style))


def list_all_styles(tree):
    styles = set()
    for g in tree.list_all():
        for style in g.art_style:
            styles.add(style)

    sorted_styles = sorted(styles)

    print("\nAvailable art styles:")
    for i, style in enumerate(sorted_styles, 1):
        print(f"{i}. {style}")

    choice = input("\nEnter the number to explore a style (or 0 to go back): ")

    if choice == "0":
        return

    if choice.isdigit() and 1 <= int(choice) <= len(sorted_styles):
        selected = sorted_styles[int(choice) - 1]
        results = [g for g in tree.list_all() if selected.lower() in [s.lower() for s in g.art_style]]
        print(f"\nGalleries with '{selected}':")
        for g in results:
            print("-", g.name, "-", g.neighborhood)
    else:
        print("Invalid option.")

def menu():
    while True:
        print("\n=== GalleryHopper ===")
        print("1. Search gallery by name")
        print("2. Filter by neighborhood")
        print("3. Filter by art style")
        print("4. List all galleries")
        print("5. Show all art styles")
        print("0. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            search_by_name(tree)
        elif option == "2":
            filter_by_neighborhood(tree)
        elif option == "3":
            filter_by_art_style(tree)
        elif option == "4":
            list_all(tree)
        elif option == "5":
            list_all_styles(tree)
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

#menu()
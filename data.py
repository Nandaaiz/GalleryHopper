def load_data(tree):
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
    tree.insert("Solomon R. Guggenheim Museum", "Upper East Side",
                ["Impressionism", "Post-Impressionism", "Modern Art", "Contemporary"], "museum",
                ["Guggenheim", "Guggenheim Museum"])
    tree.insert("The Metropolitan Museum of Art", "Upper East Side",
                ["Ancient Art", "Medieval Art", "Modern Art", "Contemporary", "Asian Art", "Fashion", "Global Art"],
                "museum", ["MET", "Metropolitan", "Met Museum"])

    # Tribeca — galleries
    tree.insert("Almine Rech", "Tribeca", ["Contemporary", "Painting", "International Art"], "gallery")
    tree.insert("David Zwirner 52 Walker", "Tribeca", ["Contemporary", "Installation"], "gallery")
    tree.insert("James Cohan Gallery", "Tribeca", ["Contemporary", "Global Art"], "gallery")

    # Midtown — museums
    tree.insert("Museum of Modern Art MoMA", "Midtown", ["Modern Art", "Contemporary", "Design", "Photography", "Film"],
                "museum", ["MoMA", "MOMA", "Museum of Modern Art"])

    # Lower East Side — galleries
    tree.insert("The Foundation of ART NYC", "Lower East Side", ["Contemporary", "Painting", "Installation"], "gallery")
    tree.insert("Sperone Westwater", "Lower East Side", ["Contemporary", "Arte Povera", "American Art"], "gallery")

    # Lower East Side — museums
    tree.insert("New Museum", "Lower East Side", ["Contemporary", "Experimental Art", "Performance"], "museum",
                ["New Museum of Contemporary Art"])

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

    # West Village — museums
    tree.insert("Whitney Museum of American Art", "West Village",
                ["American Art", "Contemporary", "Abstract Expressionism", "Pop Art"], "museum",
                ["Whitney", "Whitney Museum"])


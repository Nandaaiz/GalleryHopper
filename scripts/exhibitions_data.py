from database import db
from queries import search_by_name

exhibitions_collection = db["exhibitions"]

def migrate_exhibitions():
    exhibitions_collection.delete_many({})

    exhibitions = [
        # ── CHELSEA ──────────────────────────────────────
        {
            "gallery_name": "Gagosian Gallery",
            "title": "Giuseppe Penone: The Reflection of Bronze",
            "artist": "Giuseppe Penone",
            "style": ["Sculpture", "Arte Povera"],
            "date_start": "2026-04-22",
            "date_end": "2026-07-17",
            "status": "open"
        },
        {
            "gallery_name": "Gagosian Gallery",
            "title": "Anselm Kiefer: Seal My Ears Shut and I Shall Hear You Still",
            "artist": "Anselm Kiefer",
            "style": ["Painting", "Contemporary"],
            "date_start": "2026-05-15",
            "date_end": "2026-06-27",
            "status": "open"
        },
        {
            "gallery_name": "Gagosian Gallery",
            "title": "Helen Frankenthaler: The Moment and the Distance",
            "artist": "Helen Frankenthaler",
            "style": ["Painting", "Abstract Expressionism"],
            "date_start": "2026-04-30",
            "date_end": "2026-07-02",
            "status": "open"
        },
        {
            "gallery_name": "David Zwirner",
            "title": "Lisa Yuskavage: Solo",
            "artist": "Lisa Yuskavage",
            "style": ["Figurative", "Painting"],
            "date_start": "2026-05-14",
            "date_end": "2026-06-26",
            "status": "open"
        },
        {
            "gallery_name": "David Zwirner",
            "title": "Gerhard Richter: Landschaften",
            "artist": "Gerhard Richter",
            "style": ["Painting", "Contemporary"],
            "date_start": "2026-05-07",
            "date_end": "2026-07-10",
            "status": "open"
        },
        {
            "gallery_name": "David Zwirner",
            "title": "Jasper Johns: Copy/Trace",
            "artist": "Jasper Johns",
            "style": ["Print", "Engraving"],
            "date_start": "2026-05-07",
            "date_end": "2026-06-26",
            "status": "open"
        },
        {
            "gallery_name": "Hauser and Wirth",
            "title": "Firelei Báez: Feet squelching on wet grass, nourished by uncertainty",
            "artist": "Firelei Báez",
            "style": ["Painting", "Afro-Latin Art"],
            "date_start": "2026-05-12",
            "date_end": "2026-07-31",
            "status": "open"
        },
        {
            "gallery_name": "Hauser and Wirth",
            "title": "Carol Rama: I See You You See Me",
            "artist": "Carol Rama",
            "style": ["Figurative", "Historical"],
            "date_start": "2026-05-12",
            "date_end": "2026-07-31",
            "status": "open"
        },
        {
            "gallery_name": "Pace Gallery",
            "title": "David Hockney: The Moon Room",
            "artist": "David Hockney",
            "style": ["Painting", "Pop Art"],
            "date_start": "2026-05-15",
            "date_end": "2026-08-14",
            "status": "open"
        },
        {
            "gallery_name": "Pace Gallery",
            "title": "Emily Kam Kngwarray: The Turning Season",
            "artist": "Emily Kam Kngwarray",
            "style": ["Aboriginal Art"],
            "date_start": "2026-05-15",
            "date_end": "2026-08-14",
            "status": "open"
        },
        {
            "gallery_name": "Berry Campbell",
            "title": "Sally Silberberg: Shifting Ground",
            "artist": "Sally Silberberg",
            "style": ["Sculpture"],
            "date_start": "2026-04-23",
            "date_end": "2026-05-30",
            "status": "closed"
        },
        {
            "gallery_name": "Luhring Augustine",
            "title": "Patterns",
            "artist": "Coletiva — Tauba Auerbach, Frank Stella, Rashid Johnson e outros",
            "style": ["Painting", "Sculpture", "Textile"],
            "date_start": "2026-06-21",
            "date_end": "2026-08-02",
            "status": "open"
        },
        {
            "gallery_name": "Petzel Gallery",
            "title": "LOUCHE: Sleeping Through the Apocalypse",
            "artist": "Coletiva",
            "style": ["Contemporary"],
            "date_start": "2026-06-11",
            "date_end": "2026-07-17",
            "status": "open"
        },
        {
            "gallery_name": "Yancey Richardson Gallery",
            "title": "Mary Ellen Bartley: Color Anthology",
            "artist": "Mary Ellen Bartley",
            "style": ["Photography", "Minimalism"],
            "date_start": "2026-05-29",
            "date_end": "2026-07-02",
            "status": "open"
        },
        {
            "gallery_name": "Yancey Richardson Gallery",
            "title": "Victoria Sambunaris: Fall Line",
            "artist": "Victoria Sambunaris",
            "style": ["Photography"],
            "date_start": "2026-05-29",
            "date_end": "2026-07-02",
            "status": "open"
        },
        {
            "gallery_name": "Miles McEnery Gallery",
            "title": "Whitney Bedford: Solo",
            "artist": "Whitney Bedford",
            "style": ["Contemporary"],
            "date_start": "2026-05-14",
            "date_end": "2026-06-20",
            "status": "open"
        },

        # ── UPPER EAST SIDE ───────────────────────────────
        {
            "gallery_name": "Solomon R. Guggenheim Museum",
            "title": "Carol Bove: Solo",
            "artist": "Carol Bove",
            "style": ["Sculpture", "Installation"],
            "date_start": "2026-03-05",
            "date_end": "2026-08-02",
            "status": "open"
        },
        {
            "gallery_name": "Solomon R. Guggenheim Museum",
            "title": "Guggenheim Pop",
            "artist": "Coletiva",
            "style": ["Pop Art"],
            "date_start": "2026-06-05",
            "date_end": "2027-01-10",
            "status": "open"
        },
        {
            "gallery_name": "The Metropolitan Museum of Art",
            "title": "Raphael: Sublime Poetry",
            "artist": "Raphael",
            "style": ["Renaissance", "Painting"],
            "date_start": "2026-03-29",
            "date_end": "2026-06-28",
            "status": "open"
        },
        {
            "gallery_name": "The Metropolitan Museum of Art",
            "title": "Lillian Bassman: Bazaar and Beyond",
            "artist": "Lillian Bassman",
            "style": ["Photography", "Fashion"],
            "date_start": "2026-03-02",
            "date_end": "2026-07-26",
            "status": "open"
        },

        # ── TRIBECA ───────────────────────────────────────
        {
            "gallery_name": "Almine Rech",
            "title": "Vaughn Spann: (All) Americans",
            "artist": "Vaughn Spann",
            "style": ["Painting"],
            "date_start": "2026-05-08",
            "date_end": "2026-06-13",
            "status": "open"
        },
        {
            "gallery_name": "Almine Rech",
            "title": "Alejandro Cardenas: ARACHNE",
            "artist": "Alejandro Cardenas",
            "style": ["Painting", "Installation"],
            "date_start": "2026-05-08",
            "date_end": "2026-06-13",
            "status": "open"
        },
        {
            "gallery_name": "James Cohan Gallery",
            "title": "Mary Sully: Solo",
            "artist": "Mary Sully",
            "style": ["Abstract", "Native American Art"],
            "date_start": "2026-05-15",
            "date_end": "2026-06-27",
            "status": "open"
        },
        {
            "gallery_name": "James Cohan Gallery",
            "title": "Fred Tomaselli: Blooms Disrupted",
            "artist": "Fred Tomaselli",
            "style": ["Painting", "Collage"],
            "date_start": "2026-05-15",
            "date_end": "2026-06-27",
            "status": "open"
        },
        {
            "gallery_name": "David Zwirner 52 Walker",
            "title": "Statics of an Egg",
            "artist": "Coletiva",
            "style": ["Contemporary"],
            "date_start": "2026-05-08",
            "date_end": "2026-06-27",
            "status": "open"
        },

        # ── MIDTOWN ───────────────────────────────────────
        {
            "gallery_name": "Museum of Modern Art MoMA",
            "title": "Marcel Duchamp: Retrospective",
            "artist": "Marcel Duchamp",
            "style": ["Modern Art", "Conceptual Art"],
            "date_start": "2026-04-12",
            "date_end": "2026-08-22",
            "status": "open"
        },
        {
            "gallery_name": "Museum of Modern Art MoMA",
            "title": "Frida Kahlo & Diego Rivera: The Last Dream",
            "artist": "Frida Kahlo, Diego Rivera",
            "style": ["Painting", "Mexican Art"],
            "date_start": "2026-03-21",
            "date_end": "2026-09-12",
            "status": "open"
        },

        # ── LOWER EAST SIDE ───────────────────────────────
        {
            "gallery_name": "New Museum",
            "title": "New Humans: Memories of the Future",
            "artist": "Coletiva — mais de 200 artistas",
            "style": ["Contemporary", "Experimental Art"],
            "date_start": "2026-03-21",
            "date_end": "2026-12-31",
            "status": "open"
        },

        # ── BROOKLYN ──────────────────────────────────────
        {
            "gallery_name": "Aidron Duckworth Gallery",
            "title": "Carbon Life",
            "artist": "Coletiva",
            "style": ["Street Art", "Experimental Art"],
            "date_start": "2026-05-02",
            "date_end": "2026-07-06",
            "status": "open"
        },
        {
            "gallery_name": "Ortega y Gasset Projects",
            "title": "Reuben Telushkin: Shadow + Substance",
            "artist": "Reuben Telushkin",
            "style": ["Contemporary", "Experimental Art"],
            "date_start": "2026-06-10",
            "date_end": "2026-07-19",
            "status": "open"
        },
        {
            "gallery_name": "Platform Project Space",
            "title": "Kathryn Lynch: Heads",
            "artist": "Kathryn Lynch",
            "style": ["Contemporary", "Painting"],
            "date_start": "2026-06-04",
            "date_end": "2026-06-20",
            "status": "open"
        },
        {
            "gallery_name": "Art Cake",
            "title": "The Dinner of Sublimation",
            "artist": "Coletiva",
            "style": ["Abstract Art"],
            "date_start": "2026-06-06",
            "date_end": "2026-06-27",
            "status": "open"
        },

        # ── WEST VILLAGE ──────────────────────────────────
        {
            "gallery_name": "Whitney Museum of American Art",
            "title": "82nd Whitney Biennial",
            "artist": "56 artistas e coletivos",
            "style": ["American Art", "Contemporary"],
            "date_start": "2026-03-08",
            "date_end": "2026-08-23",
            "status": "open"
        },
    ]

    exhibitions_collection.insert_many(exhibitions)
    print(f"{len(exhibitions)} exhibitions inserted into MongoDB!")

if __name__ == "__main__":
    migrate_exhibitions()
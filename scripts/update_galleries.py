import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import db

galleries_collection = db["galleries"]

# Verificar nomes no banco
print("Galleries in database:")
for g in galleries_collection.find({}, {"name": 1}):
    print(f"  '{g['name']}'")

updates = [
    {
        "name": "Gagosian Gallery",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "555 W 24th St / 541 W 24th St / 21st St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "David Zwirner",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "533 W 19th St / 537 W 20th St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "Hauser and Wirth",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "542 W 22nd St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "Pace Gallery",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "540 W 25th St / 508-510 W 25th St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "Berry Campbell",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "524 W 26th St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "Luhring Augustine",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "531 W 24th St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "Petzel Gallery",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "520 W 25th St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "Yancey Richardson Gallery",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "525 W 22nd St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "Miles McEnery Gallery",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "511 & 515 W 22nd St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "ACA Galleries",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "529 W 20th St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "L'Space Gallery",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 11am–6pm",
            "address": "524 W 19th St, Chelsea",
            "status": "open"
        }
    },
    {
        "name": "Solomon R. Guggenheim Museum",
        "data": {
            "admission": "$30",
            "hours": "Tue–Sun 11am–6pm (Fri until 8pm)",
            "address": "1071 Fifth Avenue, Upper East Side",
            "status": "open"
        }
    },
    {
        "name": "The Metropolitan Museum of Art",
        "data": {
            "admission": "$30",
            "hours": "Sun–Thu 10am–5pm, Fri–Sat 10am–9pm",
            "address": "1000 Fifth Avenue, Upper East Side",
            "status": "open"
        }
    },
    {
        "name": "Galerie Buchholz",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "31 W 54th St, Upper East Side",
            "status": "open"
        }
    },
    {
        "name": "Anita Shapolsky Gallery",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 11am–6pm",
            "address": "152 East 65th St, Upper East Side",
            "status": "open"
        }
    },
    {
        "name": "White Cube New York",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "1002 Madison Avenue, Upper East Side",
            "status": "open"
        }
    },
    {
        "name": "Alexander Berggruen",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "1018 Madison Avenue, Upper East Side",
            "status": "open"
        }
    },
    {
        "name": "Spruth Magers",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "22 East 80th St, Upper East Side",
            "status": "open"
        }
    },
    {
        "name": "Almine Rech",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "361 Broadway, Tribeca",
            "status": "open"
        }
    },
    {
        "name": "James Cohan Gallery",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "48 & 52 Walker St, Tribeca",
            "status": "open"
        }
    },
    {
        "name": "David Zwirner 52 Walker",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 10am–6pm",
            "address": "52 Walker St, Tribeca",
            "status": "open"
        }
    },
    {
        "name": "Museum of Modern Art MoMA",
        "data": {
            "admission": "$30",
            "hours": "Mon/Wed/Thu/Sun 10:30am–5:30pm, Fri–Sat 10:30am–8pm",
            "address": "11 W 53rd St, Midtown",
            "status": "open"
        }
    },
    {
        "name": "The Foundation of ART NYC",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 11am–6pm",
            "address": "37-39 Clinton St, Lower East Side",
            "status": "open"
        }
    },
    {
        "name": "Sperone Westwater",
        "data": {
            "admission": "Free",
            "hours": "Closed",
            "address": "257 Bowery, Lower East Side",
            "status": "closed"
        }
    },
    {
        "name": "New Museum",
        "data": {
            "admission": "$22",
            "hours": "Tue–Sun 11am–6pm (Thu until 9pm)",
            "address": "235 Bowery, Lower East Side",
            "status": "open"
        }
    },
    {
        "name": "CARVALHO",
        "data": {
            "admission": "Free",
            "hours": "Tue–Sat 11am–6pm",
            "address": "110-112 Waterbury St, Bushwick, Brooklyn",
            "status": "open"
        }
    },
    {
        "name": "Aidron Duckworth Gallery",
        "data": {
            "admission": "Free",
            "hours": "Sat–Sun 12pm–6pm",
            "address": "169 Coffey St, Red Hook, Brooklyn",
            "status": "open"
        }
    },
    {
        "name": "Ortega y Gasset Projects",
        "data": {
            "admission": "Free",
            "hours": "Thu–Sun 12pm–6pm",
            "address": "363 3rd Avenue, Gowanus, Brooklyn",
            "status": "open"
        }
    },
    {
        "name": "Smack Mellon",
        "data": {
            "admission": "Free",
            "hours": "Wed–Sun 12pm–6pm",
            "address": "92 Plymouth St, DUMBO, Brooklyn",
            "status": "open"
        }
    },
    {
        "name": "Platform Project Space",
        "data": {
            "admission": "Free",
            "hours": "Thu–Sun 12pm–6pm",
            "address": "20 Jay St, DUMBO, Brooklyn",
            "status": "closing"
        }
    },
    {
        "name": "AIR Gallery",
        "data": {
            "admission": "Free",
            "hours": "Temporarily closed — relocating to West Village",
            "address": "155 Plymouth St, DUMBO, Brooklyn",
            "status": "relocating"
        }
    },
    {
        "name": "Amant",
        "data": {
            "admission": "Free",
            "hours": "Thu–Sun 12pm–6pm",
            "address": "315 Maujer St, East Williamsburg, Brooklyn",
            "status": "open"
        }
    },
    {
        "name": "Art Cake",
        "data": {
            "admission": "Free",
            "hours": "Sat–Sun 12pm–6pm",
            "address": "214 40th St, Sunset Park, Brooklyn",
            "status": "open"
        }
    },
    {
        "name": "Mrs.",
        "data": {
            "admission": "Free",
            "hours": "Tue–Fri 11am–6pm, Sat 12pm–5pm",
            "address": "60-40 56th Drive, Maspeth, Queens",
            "status": "open"
        }
    },
    {
        "name": "Culture Lab LIC",
        "data": {
            "admission": "Free",
            "hours": "Check website for current hours",
            "address": "5-25 46th Ave, Long Island City, Queens",
            "status": "open"
        }
    },
    {
        "name": "Whitney Museum of American Art",
        "data": {
            "admission": "$30 (Free Fri 5–10pm & 2nd Sun of month, always free under 25)",
            "hours": "Wed–Sun 10:30am–6pm (Fri until 10pm)",
            "address": "99 Gansevoort St, West Village",
            "status": "open"
        }
    },
    {
        "name": "MoMA PS1",
        "data": {
            "admission": "$20",
            "hours": "Thu–Sun 12pm–6pm",
            "address": "22-25 Jackson Ave, Long Island City, Queens",
            "status": "open"
        }
    },
]

def update_all():
    count = 0
    for item in updates:
        result = galleries_collection.update_one(
            {"name": item["name"]},
            {"$set": item["data"]}
        )
        if result.matched_count > 0:
            print(f"✓ Updated: {item['name']}")
        else:
            print(f"⚠ Not found: {item['name']}")
        count += 1
    print(f"\nDone! {count} galleries processed.")

if __name__ == "__main__":
    update_all()
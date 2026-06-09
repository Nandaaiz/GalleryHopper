import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import db

exhibitions_collection = db["exhibitions"]

updates = [
    {
        "title": "Giuseppe Penone: The Reflection of Bronze",
        "description": "Penone, a central figure of Arte Povera, explores the relationship between nature and language through large bronze sculptures capturing organic forms — trunks, branches, footprints — merging the human with the natural."
    },
    {
        "title": "Anselm Kiefer: Seal My Ears Shut and I Shall Hear You Still",
        "description": "Kiefer, a major reference in post-war European painting, works with heavy materials such as lead, straw and ashes on monumental canvases evoking mythology, history and collective trauma."
    },
    {
        "title": "Helen Frankenthaler: The Moment and the Distance",
        "description": "A retrospective focused on Frankenthaler's soak-stain technique, in which paint is poured directly onto unprimed canvas, creating fluid and luminous color fields."
    },
    {
        "title": "Lisa Yuskavage: Solo",
        "description": "The artist's tenth exhibition with the gallery. New and recent paintings alongside an unpublished series of collages — a new medium for the artist. Yuskavage combines color field influences with trompe-l'oeil devices in psychologically charged female figures."
    },
    {
        "title": "Gerhard Richter: Landschaften",
        "description": "A selection of landscapes from the archive of the German artist, considered one of the greatest living painters. The works navigate between abstraction and photorealistic representation, a central theme throughout Richter's career."
    },
    {
        "title": "Jasper Johns: Copy/Trace",
        "description": "A presentation focused on the process of reproduction and tracing in Johns' work — one of the most influential artists of the 20th century, famous for his targets, flags and maps."
    },
    {
        "title": "Firelei Báez: Feet squelching on wet grass, nourished by uncertainty",
        "description": "The Dominican-American artist creates large-scale paintings reimagining historical and mythological figures, especially Black and Afro-Latin women, drawing from visual sources ranging from colonial maps to illuminated manuscripts."
    },
    {
        "title": "Carol Rama: I See You You See Me",
        "description": "An exhibition dedicated to Italian artist Carol Rama (1918-2015), belatedly recognized as one of the most original figures in European art. Her disturbing and erotically charged works mix industrial materials with fragments of the human body."
    },
    {
        "title": "David Hockney: The Moon Room",
        "description": "Hockney created these works during COVID-19 isolation at his 17th-century farmhouse in Normandy. These are digital paintings printed in large format, celebrating the arrival of spring with exuberant colors. His tenth solo exhibition with the gallery."
    },
    {
        "title": "Emily Kam Kngwarray: The Turning Season",
        "description": "An exhibition of the Anmatyerr artist (1910-1996), one of the most celebrated painters of Australian Aboriginal art, whose abstract works map the sacred territory of her homeland through sinuous lines and dots."
    },
    {
        "title": "Patterns",
        "description": "Over 20 artists exploring pattern as motif, organizing principle and compositional strategy. Includes Tauba Auerbach, Frank Stella, Rashid Johnson, Christopher Wool, Rosemarie Trockel, Jack Whitten and Philip Taaffe."
    },
    {
        "title": "Mary Ellen Bartley: Color Anthology",
        "description": "Bartley photographs books as objects — her practice evokes classical still-life painting and minimalism while examining the formal and poetic qualities of the book."
    },
    {
        "title": "Victoria Sambunaris: Fall Line",
        "description": "New large-scale topographic portraits — highly detailed and dramatically composed photographs documenting the transformations of the American West landscape caused by human intervention."
    },
    {
        "title": "Carol Bove: Solo",
        "description": "The largest museum retrospective of the Genevan artist to date. Bove is known for her twisted steel sculpture-collages and rigorous spatial choreography, tracing her evolution from delicate early drawings to monumental works in industrial metal."
    },
    {
        "title": "Guggenheim Pop",
        "description": "A new exhibition examining how artists of the second half of the 20th century responded to and reshaped the social and historical contexts of their time. Includes works from the D. Daskalopoulos collection."
    },
    {
        "title": "Raphael: Sublime Poetry",
        "description": "The first major Raphael retrospective in the US — over 200 works gathered from institutions across Europe. Includes La Fornarina, portraits of women with unicorns and rarely loaned mythological scenes. Curated by Carmen C. Bambach."
    },
    {
        "title": "Lillian Bassman: Bazaar and Beyond",
        "description": "A retrospective of the American photographer known for her ethereal and blurred images for Harper's Bazaar in the 1940s and 60s."
    },
    {
        "title": "Vaughn Spann: (All) Americans",
        "description": "Spann uses the American flag as a starting point to question issues of belonging, protection and exclusion. The work confronts the viewer like a roadside banner warning that some will find little shelter here."
    },
    {
        "title": "Alejandro Cardenas: ARACHNE",
        "description": "A dynamic installation with new paintings and a series of drawings. A seductive gesamtkunstwerk — reimaginings of art, design, mythology and fantasy masterfully woven into a dreamlike vision of the future."
    },
    {
        "title": "Mary Sully: Solo",
        "description": "First solo gallery exhibition in New York. Sully (1896-1963), a Yankton Dakota artist, created in the 1920s a series of personality prints — celebrity portraits in triptych format fusing modern art, design and Native American visual forms."
    },
    {
        "title": "Fred Tomaselli: Blooms Disrupted",
        "description": "Tomaselli creates works of extraordinary visual complexity using leaves, flowers, pills and other materials embedded in resin, alongside paintings with influences from botanical art and psychedelia."
    },
    {
        "title": "Statics of an Egg",
        "description": "An intergenerational group exhibition organized around the idea that artists separated by continents and centuries are connected by shared interest in the material world. Themes: translucency, luminosity, assemblage and absence of color."
    },
    {
        "title": "Marcel Duchamp: Retrospective",
        "description": "Around 300 works spanning 6 decades. The first Duchamp retrospective in the US since 1973, in partnership with the Philadelphia Museum of Art. Includes Nude Descending a Staircase No. 2, The Large Glass, Fountain and the complete readymade series."
    },
    {
        "title": "Frida Kahlo & Diego Rivera: The Last Dream",
        "description": "Five paintings by Kahlo, over a dozen works by Rivera and photographic portraits of the artists by Lola Álvarez Bravo and Leo Matiz. Presented in partnership with the Metropolitan Opera and its production of El Último Sueño de Frida y Diego."
    },
    {
        "title": "New Humans: Memories of the Future",
        "description": "Over 200 artists, writers, architects, scientists and filmmakers exploring how technological advances have inspired changing definitions of the human. Includes robotics, sculpture, video installations and permanent new commissions. Inaugural exhibition of the museum's 60,000 sq ft expansion designed by OMA."
    },
    {
        "title": "Carbon Life",
        "description": "A group exhibition exploring themes of carbon, life and environmental transformation through contemporary art and experimental practices."
    },
    {
        "title": "Reuben Telushkin: Shadow + Substance",
        "description": "The artist explores the relationship between physical presence and absence, light and shadow, creating works that oscillate between the tangible and the intangible."
    },
    {
        "title": "Kathryn Lynch: Heads",
        "description": "The final exhibition at Platform Project Space before the gallery permanently closes. Lynch's paintings capture the raw energy and psychological depth of the human figure."
    },
    {
        "title": "The Dinner of Sublimation",
        "description": "A group exhibition at Art Cake's Sunset Park space exploring themes of transformation, desire and the sublime through diverse artistic practices."
    },
    {
        "title": "82nd Whitney Biennial",
        "description": "Curated by Marcela Guerrero and Drew Sawyer. 56 artists, duos and collectives examining the environments, mood and challenges of contemporary American art. The longest-running survey of American art, active since 1932. Free Fridays 5-10pm and second Sunday of each month."
    },
    {
        "title": "Greater New York 2026",
        "description": "53 artists and collectives living and working in the NYC metropolitan area. Over 150 works including site-specific installations, new productions, performances and recent works. The sixth edition of PS1's quinquennial survey, organized by the full curatorial team in celebration of the institution's 50th anniversary."
    },
    {
        "title": "Shape of Dreams: Leonora Carrington",
        "description": "An exhibition dedicated to the British-Mexican artist (1917-2011), a central figure of Surrealism and one of the most original visions of the 20th century. Carrington created fantastic and autobiographical worlds inhabited by hybrid creatures, witches, animals and initiatory figures. Features an interactive Tarot Booth during visits."
    },
    {
        "title": "Kim Gordon: Count Your Chickens",
        "description": "Kim Gordon, co-founder of Sonic Youth, visual artist and writer. An exhibition continuing her multimedia practice exploring sound, language and visual culture."
    },
    {
        "title": "CFGNY: Puddles into Pond",
        "description": "CFGNY (Concept Foreign Garments New York) is an interdisciplinary collective blurring the boundaries between fashion, art and queer Asian culture."
    },
    {
        "title": "Christelle Oyiri: Belief May Vary",
        "description": "Work by the French artist and DJ exploring spirituality, belief and sound culture through immersive installations and visual art."
    },
]

def update_all():
    count = 0
    for item in updates:
        result = exhibitions_collection.update_one(
            {"title": item["title"]},
            {"$set": {"description": item["description"]}}
        )
        if result.matched_count > 0:
            print(f"✓ Updated: {item['title'][:50]}")
        else:
            print(f"⚠ Not found: {item['title'][:50]}")
        count += 1
    print(f"\nDone! {count} exhibitions processed.")

if __name__ == "__main__":
    update_all()
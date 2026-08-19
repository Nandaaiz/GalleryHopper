import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import db

exhibitions_collection = db["exhibitions"]

updates = [
    {
        "title": "Giuseppe Penone: The Reflection of Bronze",
        "description_pt": "Penone, figura central da Arte Povera, explora a relação entre natureza e linguagem através de grandes esculturas em bronze que capturam formas orgânicas — troncos, galhos, pegadas — fundindo o humano com o natural."
    },
    {
        "title": "Anselm Kiefer: Seal My Ears Shut and I Shall Hear You Still",
        "description_pt": "Kiefer, referência maior da pintura europeia pós-guerra, trabalha com materiais pesados como chumbo, palha e cinzas em telas monumentais que evocam mitologia, história e trauma coletivo."
    },
    {
        "title": "Helen Frankenthaler: The Moment and the Distance",
        "description_pt": "Retrospectiva focada na técnica de soak-stain desenvolvida por Frankenthaler, em que a tinta é derramada diretamente na tela sem preparação, criando campos de cor fluidos e luminosos."
    },
    {
        "title": "Lisa Yuskavage: Solo",
        "description_pt": "Décima exposição da artista com a galeria. Pinturas novas e recentes além de uma série inédita de colagens. Yuskavage combina influências do campo de cor com dispositivos trompe-l'oeil em figuras femininas carregadas de psicologia."
    },
    {
        "title": "Gerhard Richter: Landschaften",
        "description_pt": "Seleção de paisagens do arquivo do artista alemão, considerado um dos maiores pintores vivos. As obras navegam entre abstração e representação fotorrealista, tema central de toda a carreira de Richter."
    },
    {
        "title": "Jasper Johns: Copy/Trace",
        "description_pt": "Apresentação focada no processo de reprodução e tracejamento na obra de Johns — um dos artistas mais influentes do século XX, famoso pelos alvos, bandeiras e mapas."
    },
    {
        "title": "Firelei Báez: Feet squelching on wet grass, nourished by uncertainty",
        "description_pt": "A artista dominicano-americana cria pinturas em grande escala que reimaginam figuras históricas e mitológicas, especialmente mulheres negras e afro-latinas, a partir de fontes visuais que vão de mapas coloniais a manuscritos iluminados."
    },
    {
        "title": "Carol Rama: I See You You See Me",
        "description_pt": "Exposição dedicada à artista italiana Carol Rama (1918–2015), tardiamente reconhecida como uma das figuras mais originais da arte europeia. Suas obras perturbadoras misturam materiais industriais com fragmentos do corpo humano."
    },
    {
        "title": "David Hockney: The Moon Room",
        "description_pt": "Hockney criou estas obras durante o isolamento da COVID-19 em sua fazenda do século XVII na Normandia. São pinturas digitais impressas em grande formato, celebrando a chegada da primavera com cores exuberantes."
    },
    {
        "title": "Emily Kam Kngwarray: The Turning Season",
        "description_pt": "Exposição da artista Anmatyerr (1910–1996), uma das pintoras mais celebradas da Arte Aborígene australiana, cujas obras abstratas mapeiam o território sagrado de sua terra natal através de linhas sinuosas e pontos."
    },
    {
        "title": "Patterns",
        "description_pt": "Mais de 20 artistas explorando padrão como motivo, princípio organizador e estratégia compositiva. Inclui Tauba Auerbach, Frank Stella, Rashid Johnson, Christopher Wool, Rosemarie Trockel, Jack Whitten e Philip Taaffe."
    },
    {
        "title": "LOUCHE: Sleeping Through the Apocalypse",
        "description_pt": "Exposição coletiva de arte contemporânea. Detalhes completos dos artistas sendo divulgados — consultar o site da galeria."
    },
    {
        "title": "Mary Ellen Bartley: Color Anthology",
        "description_pt": "Bartley fotografa livros como objetos — sua prática evoca a pintura de natureza-morta clássica e o minimalismo enquanto examina as qualidades formais e poéticas do livro."
    },
    {
        "title": "Victoria Sambunaris: Fall Line",
        "description_pt": "Novos retratos topográficos em grande escala — fotografias altamente detalhadas documentando as transformações da paisagem do Oeste americano causadas pela intervenção humana."
    },
    {
        "title": "Whitney Bedford: Solo",
        "description_pt": "Bedford cria paisagens de memória carregadas de melancolia e temporalidade."
    },
    {
        "title": "Carol Bove: Solo",
        "description_pt": "A maior retrospectiva de museu da artista genebriana até o momento. Bove é conhecida por suas esculturas-colagem de aço torcido e por sua coreografia espacial rigorosa."
    },
    {
        "title": "Guggenheim Pop",
        "description_pt": "Nova exposição examinando como artistas da segunda metade do século XX responderam e reformularam os contextos sociais e históricos de seu tempo. Inclui obras da coleção D. Daskalopoulos."
    },
    {
        "title": "Raphael: Sublime Poetry",
        "description_pt": "Primeira grande retrospectiva de Raphael nos EUA — mais de 200 obras reunidas de instituições de toda a Europa. Inclui La Fornarina e cenas mitológicas raramente emprestadas. Curadoria de Carmen C. Bambach."
    },
    {
        "title": "Lillian Bassman: Bazaar and Beyond",
        "description_pt": "Retrospectiva da fotógrafa americana conhecida por suas imagens etéreas e borradas para a Harper's Bazaar nas décadas de 1940–60."
    },
    {
        "title": "Vaughn Spann: (All) Americans",
        "description_pt": "Spann usa a bandeira americana como ponto de partida para questionar questões de pertencimento, proteção e exclusão."
    },
    {
        "title": "Alejandro Cardenas: ARACHNE",
        "description_pt": "Instalação dinâmica com novas pinturas e série de desenhos — reimaginações de arte, design, mitologia e fantasia magistralmente tecidas em uma visão onírica do futuro."
    },
    {
        "title": "Mary Sully: Solo",
        "description_pt": "Primeira exposição solo em galeria em Nova York. Sully (1896–1963), artista Dakota Yankton, criou nos anos 1920 'personality prints' — retratos de celebridades em formato tríptico que fundiram arte moderna e formas visuais Nativas Americanas."
    },
    {
        "title": "Fred Tomaselli: Blooms Disrupted",
        "description_pt": "Tomaselli cria obras de extraordinária complexidade visual usando folhas, flores, pílulas e outros materiais incorporados em resina, com influências de arte botânica e psicodélica."
    },
    {
        "title": "Statics of an Egg",
        "description_pt": "Exposição coletiva intergeracional organizada em torno da ideia de que artistas separados por continentes e séculos são conectados por interesse compartilhado no mundo material."
    },
    {
        "title": "Marcel Duchamp: Retrospective",
        "description_pt": "Cerca de 300 obras abrangendo 6 décadas. Primeiro retrospecto nos EUA desde 1973, em parceria com o Philadelphia Museum of Art. Inclui Nude Descending a Staircase, The Large Glass e Fountain."
    },
    {
        "title": "Frida Kahlo & Diego Rivera: The Last Dream",
        "description_pt": "Cinco pinturas de Kahlo, mais de uma dúzia de obras de Rivera e retratos fotográficos dos artistas. Apresentado em parceria com a Metropolitan Opera e sua produção de El Último Sueño de Frida y Diego."
    },
    {
        "title": "New Humans: Memories of the Future",
        "description_pt": "Mais de 200 artistas, escritores, arquitetos e cineastas explorando como os avanços tecnológicos têm inspirado definições mutáveis do humano. Exposição inaugural da expansão de 60.000 sq ft projetada pela OMA."
    },
    {
        "title": "Carbon Life",
        "description_pt": "Exposição coletiva explorando temas de carbono, vida e transformação ambiental através da arte contemporânea."
    },
    {
        "title": "Reuben Telushkin: Shadow + Substance",
        "description_pt": "O artista explora a relação entre presença física e ausência, luz e sombra, criando obras que oscilam entre o tangível e o intangível."
    },
    {
        "title": "The Dinner of Sublimation",
        "description_pt": "Exposição coletiva explorando temas de transformação, desejo e o sublime através de diversas práticas artísticas."
    },
    {
        "title": "82nd Whitney Biennial",
        "description_pt": "Curadoria de Marcela Guerrero e Drew Sawyer. 56 artistas, duos e coletivos examinando os ambientes e desafios da arte americana contemporânea. A mais longa survey de arte americana em atividade desde 1932."
    },
    {
        "title": "Greater New York 2026",
        "description_pt": "53 artistas e coletivos que vivem e trabalham na área metropolitana de NYC. Mais de 150 obras incluindo instalações site-specific, novas produções e performances. Sexta edição da survey quinquenal do PS1."
    },
    {
        "title": "Shape of Dreams: Leonora Carrington",
        "description_pt": "Exposição dedicada à artista britânico-mexicana (1917–2011), figura central do Surrealismo. Carrington criava mundos fantásticos habitados por criaturas híbridas, bruxas e figuras iniciáticas."
    },
    {
        "title": "Kim Gordon: Count Your Chickens",
        "description_pt": "Kim Gordon, co-fundadora do Sonic Youth, artista visual e escritora. Exposição que continua sua prática multimídia explorando som, linguagem e cultura visual."
    },
    {
        "title": "CFGNY: Puddles into Pond",
        "description_pt": "CFGNY (Concept Foreign Garments New York) é um coletivo interdisciplinar que borra as fronteiras entre moda, arte e cultura queer asiática."
    },
    {
        "title": "Christelle Oyiri: Belief May Vary",
        "description_pt": "Obra da artista e DJ francesa explorando espiritualidade, crença e sound culture através de instalações imersivas e arte visual."
    },
]

def update_all():
    count = 0
    for item in updates:
        result = exhibitions_collection.update_one(
            {"title": item["title"]},
            {"$set": {"description_pt": item["description_pt"]}}
        )
        if result.matched_count > 0:
            print(f"✓ {item['title'][:50]}")
        else:
            print(f"⚠ Not found: {item['title'][:50]}")
        count += 1
    print(f"\nDone! {count} exhibitions processed.")

if __name__ == "__main__":
    update_all()
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import db

galleries_collection = db["galleries"]
exhibitions_collection = db["exhibitions"]

galleries = [
    # ── MUSEUS & INSTITUTOS ───────────────────────────
    {
        "name": "MASP",
        "neighborhood": "Bela Vista",
        "art_style": ["Modern Art", "Contemporary", "Latin American", "Photography", "Sculpture"],
        "type": "museum",
        "alias": ["Museu de Arte de São Paulo", "MASP Paulista"],
        "city": "São Paulo",
        "admission": "R$60 · Terças gratuito",
        "hours": "Ter 10h–20h | Qua–Dom 10h–18h | Seg fechado",
        "address": "Av. Paulista, 1578 — Bela Vista, SP",
        "status": "open"
    },
    {
        "name": "Pinacoteca de São Paulo",
        "neighborhood": "Luz",
        "art_style": ["Brazilian Art", "Modern Art", "Contemporary", "Sculpture", "Photography"],
        "type": "museum",
        "alias": ["Pina", "Pina Luz", "Pina Estação", "Pina Contemporânea"],
        "city": "São Paulo",
        "admission": "R$40 · Sábados gratuito",
        "hours": "Qua–Seg 10h–18h | Ter fechado",
        "address": "Praça da Luz, 2 — Luz, SP",
        "status": "open"
    },
    {
        "name": "MAM São Paulo",
        "neighborhood": "Vila Mariana",
        "art_style": ["Modern Art", "Contemporary", "Brazilian Art", "Installation"],
        "type": "museum",
        "alias": ["MAM", "Museu de Arte Moderna"],
        "city": "São Paulo",
        "admission": "R$30 · Domingos gratuito",
        "hours": "Ter–Dom 10h–18h | Seg fechado",
        "address": "Av. Pedro Álvares Cabral, s/n — Parque Ibirapuera, SP",
        "status": "open"
    },
    {
        "name": "MAC USP",
        "neighborhood": "Vila Mariana",
        "art_style": ["Contemporary", "Modern Art", "International", "Brazilian Art"],
        "type": "museum",
        "alias": ["MAC", "Museu de Arte Contemporânea"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Dom 10h–21h | Seg fechado",
        "address": "Av. Pedro Álvares Cabral, 1301 — Parque Ibirapuera, SP",
        "status": "open"
    },
    {
        "name": "MAB FAAP",
        "neighborhood": "Higienópolis",
        "art_style": ["Modern Art", "International", "Brazilian Art", "Surrealism"],
        "type": "museum",
        "alias": ["MAB", "Museu de Arte Brasileira"],
        "city": "São Paulo",
        "admission": "R$50 · R$25 meia",
        "hours": "Ter–Dom 9h–20h | Seg fechado",
        "address": "Rua Alagoas, 903 — Higienópolis, SP",
        "status": "open"
    },
    {
        "name": "Instituto Tomie Ohtake",
        "neighborhood": "Pinheiros",
        "art_style": ["Contemporary", "Design", "Architecture", "Photography"],
        "type": "museum",
        "alias": ["Tomie Ohtake", "ITO"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Dom 11h–19h | Seg fechado",
        "address": "Rua Coropé, 88 — Pinheiros, SP",
        "status": "open"
    },
    {
        "name": "IMS Paulista",
        "neighborhood": "Bela Vista",
        "art_style": ["Photography", "Documentary", "Contemporary", "Brazilian Art"],
        "type": "museum",
        "alias": ["IMS", "Instituto Moreira Salles"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Dom 10h–20h | Seg fechado",
        "address": "Av. Paulista, 2424 — Bela Vista, SP",
        "status": "open"
    },
    {
        "name": "Itaú Cultural",
        "neighborhood": "Bela Vista",
        "art_style": ["Brazilian Art", "Contemporary", "Digital Art", "Performance"],
        "type": "museum",
        "alias": ["IC"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sáb 11h–20h | Dom 11h–19h | Seg fechado",
        "address": "Av. Paulista, 149 — Bela Vista, SP",
        "status": "open"
    },
    {
        "name": "Fundação Bienal de São Paulo",
        "neighborhood": "Ibirapuera",
        "art_style": ["Contemporary", "International", "Installation", "Experimental"],
        "type": "museum",
        "alias": ["Bienal", "Pavilhão da Bienal"],
        "city": "São Paulo",
        "admission": "Varia por edição",
        "hours": "Consultar site para próxima edição",
        "address": "Av. Pedro Álvares Cabral, s/n — Parque Ibirapuera, SP",
        "status": "open"
    },
    # ── GALERIAS COM EXPOSIÇÃO ────────────────────────
    {
        "name": "Galeria Vermelho",
        "neighborhood": "Higienópolis",
        "art_style": ["Contemporary", "Experimental", "Performance", "Installation"],
        "type": "gallery",
        "alias": ["Vermelho"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 10h–19h | Sáb 11h–17h",
        "address": "Rua Minas Gerais, 350 — Higienópolis, SP",
        "status": "open"
    },
    {
        "name": "Nara Roesler Gallery",
        "neighborhood": "Jardim Europa",
        "art_style": ["Contemporary", "Latin American", "Brazilian Art", "Abstract"],
        "type": "gallery",
        "alias": ["Nara Roesler"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 11h–15h",
        "address": "Av. Europa, 655 — Jardim Europa, SP",
        "status": "open"
    },
    {
        "name": "Mendes Wood DM",
        "neighborhood": "Barra Funda",
        "art_style": ["Contemporary", "Conceptual", "Brazilian Art", "International"],
        "type": "gallery",
        "alias": ["Mendes Wood"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 11h–19h | Sáb 10h–17h",
        "address": "Rua Barra Funda, 216 — Barra Funda, SP",
        "status": "open"
    },
    {
        "name": "Fortes D'Aloia & Gabriel",
        "neighborhood": "Barra Funda",
        "art_style": ["Contemporary", "Brazilian Art", "International", "Sculpture"],
        "type": "gallery",
        "alias": ["Fortes D'Aloia", "FDAG"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 10h–19h | Sáb 10h–18h",
        "address": "Rua James Holland, 71 — Barra Funda, SP",
        "status": "open"
    },
    {
        "name": "Galeria Luisa Strina",
        "neighborhood": "Cerqueira César",
        "art_style": ["Contemporary", "Conceptual", "International", "Brazilian Art"],
        "type": "gallery",
        "alias": ["Luisa Strina"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Qua e Sex 10h–19h | Sáb 10h–17h",
        "address": "Rua Padre João Manuel, 755 — Cerqueira César, SP",
        "status": "open"
    },
    {
        "name": "Casa Triângulo",
        "neighborhood": "Jardins",
        "art_style": ["Contemporary", "Brazilian Art", "International"],
        "type": "gallery",
        "alias": ["Triangulo"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 10h–19h | Sáb 10h–17h",
        "address": "Rua Estados Unidos, 1324 — Jardins, SP",
        "status": "open"
    },
    {
        "name": "Zipper Galeria",
        "neighborhood": "Jardim América",
        "art_style": ["Contemporary", "Urban Art", "Photography", "Brazilian Art"],
        "type": "gallery",
        "alias": ["Zipper"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 11h–17h",
        "address": "Rua Estados Unidos, 1494 — Jardim América, SP",
        "status": "open"
    },
    {
        "name": "Galeria Raquel Arnaud",
        "neighborhood": "Vila Madalena",
        "art_style": ["Contemporary", "Abstract", "Brazilian Art", "International"],
        "type": "gallery",
        "alias": ["Raquel Arnaud"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–18h | Sáb 10h–15h",
        "address": "Rua Fidalga, 125 — Vila Madalena, SP",
        "status": "open"
    },
    {
        "name": "Galeria Marcelo Guarnieri",
        "neighborhood": "Jardins",
        "art_style": ["Modern Art", "Contemporary", "Brazilian Art"],
        "type": "gallery",
        "alias": ["Marcelo Guarnieri", "Guarnieri"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 10h–17h",
        "address": "Alameda Lorena, 1835 — Jardim Paulista, SP",
        "status": "open"
    },
    {
        "name": "Galeria 18",
        "neighborhood": "Vila Madalena",
        "art_style": ["Contemporary", "Emerging Artists", "Multi-Media"],
        "type": "gallery",
        "alias": ["Galeria Dezoito"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 12h–19h | Sáb 12h–17h",
        "address": "Rua Simpatia, 23 — Vila Madalena, SP",
        "status": "open"
    },
    {
        "name": "Luciana Brito Galeria",
        "neighborhood": "Itaim Bibi",
        "art_style": ["Contemporary", "Brazilian Art", "International", "Conceptual"],
        "type": "gallery",
        "alias": ["Luciana Brito"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 10h–19h | Sáb 12h–17h",
        "address": "Av. Nove de Julho, 5162 — Itaim Bibi, SP",
        "status": "open"
    },
    {
        "name": "Simões de Assis",
        "neighborhood": "Jardins",
        "art_style": ["Contemporary", "Brazilian Art", "Afro-Brazilian"],
        "type": "gallery",
        "alias": ["Simoes de Assis"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 10h–15h",
        "address": "Al. Lorena, 2050A — Jardins, SP",
        "status": "open"
    },
    # ── GALERIAS SEM EXPOSIÇÃO CONFIRMADA ─────────────
    {
        "name": "Almeida & Dale Galeria de Arte",
        "neighborhood": "Vila Madalena",
        "art_style": ["Modern Art", "Contemporary", "Brazilian Modernism"],
        "type": "gallery",
        "alias": ["Almeida Dale"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 11h–16h",
        "address": "Rua Fradique Coutinho, 1430 — Vila Madalena, SP",
        "status": "open"
    },
    {
        "name": "Galeria Leme",
        "neighborhood": "Butantã",
        "art_style": ["Contemporary", "Conceptual", "Brazilian Art"],
        "type": "gallery",
        "alias": ["Leme"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 9h–18h",
        "address": "Av. Valdemar Ferreira, 130 — Butantã, SP",
        "status": "open"
    },
    {
        "name": "Pivô Arte e Pesquisa",
        "neighborhood": "República",
        "art_style": ["Experimental", "Contemporary", "Installation", "Conceptual"],
        "type": "gallery",
        "alias": ["Pivô", "Pivo"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 13h–19h | Sáb–Dom 12h–18h",
        "address": "Av. Ipiranga, 200 — Edifício Copan, República, SP",
        "status": "open"
    },
    {
        "name": "Galeria Jaqueline Martins",
        "neighborhood": "Pinheiros",
        "art_style": ["Conceptual", "Historical", "Performance", "Contemporary"],
        "type": "gallery",
        "alias": ["Jaqueline Martins"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 11h–19h | Sáb 11h–16h",
        "address": "Rua Virgílio de Carvalho Pinto, 74 — Pinheiros, SP",
        "status": "open"
    },
    {
        "name": "Central Galeria",
        "neighborhood": "Higienópolis",
        "art_style": ["Contemporary", "Brazilian Art", "Emerging Artists"],
        "type": "gallery",
        "alias": ["Central"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 10h–19h | Sáb 10h–16h",
        "address": "Rua Minas Gerais, 350 — Higienópolis, SP",
        "status": "open"
    },
    {
        "name": "Galeria Pilar",
        "neighborhood": "Vila Madalena",
        "art_style": ["Contemporary", "Brazilian Art", "Emerging Artists", "Photography"],
        "type": "gallery",
        "alias": ["Pilar"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 11h–19h | Sáb 11h–17h",
        "address": "Rua Mourato Coelho, 1319 — Vila Madalena, SP",
        "status": "open"
    },
    {
        "name": "Choque Cultural",
        "neighborhood": "Jardim Paulista",
        "art_style": ["Urban Art", "Street Art", "Contemporary", "Graffiti"],
        "type": "gallery",
        "alias": ["Choque"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Ter–Sex 11h–19h | Sáb 11h–17h",
        "address": "Alameda Sarutaiá, 206 — Jardim Paulista, SP",
        "status": "open"
    },
    {
        "name": "Galeria Carbono",
        "neighborhood": "Itaim Bibi",
        "art_style": ["Contemporary", "Prints", "Editions", "Multiple"],
        "type": "gallery",
        "alias": ["Carbono"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 10h–15h",
        "address": "Rua Pedroso Alvarenga, 1208 — Itaim Bibi, SP",
        "status": "open"
    },
    {
        "name": "Galeria Lume",
        "neighborhood": "Itaim Bibi",
        "art_style": ["Contemporary", "Brazilian Art", "International"],
        "type": "gallery",
        "alias": ["Lume"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 10h–17h",
        "address": "Rua Estados Unidos, 2393 — Itaim Bibi, SP",
        "status": "open"
    },
    {
        "name": "Galeria Dan",
        "neighborhood": "Jardins",
        "art_style": ["Contemporary", "Brazilian Art", "Modern Art"],
        "type": "gallery",
        "alias": ["Dan"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 10h–16h",
        "address": "Rua Estados Unidos, 1638 — Jardim América, SP",
        "status": "open"
    },
    {
        "name": "Galeria Marília Razuk",
        "neighborhood": "Higienópolis",
        "art_style": ["Contemporary", "Brazilian Art", "Emerging Artists"],
        "type": "gallery",
        "alias": ["Marilia Razuk", "Razuk"],
        "city": "São Paulo",
        "admission": "Gratuito",
        "hours": "Seg–Sex 10h–19h | Sáb 11h–17h",
        "address": "Rua Sergipe, 476 — Higienópolis, SP",
        "status": "open"
    },
]

exhibitions = [
    {
        "gallery_name": "MASP",
        "title": "Carolina Caycedo: confluências",
        "artist": "Carolina Caycedo",
        "style": ["Installation", "Video Art", "Performance"],
        "date_start": "2026-07-03",
        "date_end": "2026-10-04",
        "status": "open",
        "description": "Retrospective of the Colombian-British artist about rivers, environmental resistance and riverside knowledge through video, performance and installation.",
        "description_pt": "Retrospectiva da artista colombiana-britânica sobre rios, resistência ambiental e saberes ribeirinhos via vídeo, performance e instalação."
    },
    {
        "gallery_name": "MASP",
        "title": "Sol Calero: Casa María Lionza",
        "artist": "Sol Calero",
        "style": ["Installation", "Latin American Art"],
        "date_start": "2026-07-03",
        "date_end": "2026-12-31",
        "status": "open",
        "description": "Immersive pavilion in the Vão Livre with murals, mosaics and furniture inspired by Latin American culture.",
        "description_pt": "Pavilhão imersivo no Vão Livre com murais, mosaicos e mobiliário inspirados na cultura latino-americana e na divindade venezuelana María Lionza."
    },
    {
        "gallery_name": "MASP",
        "title": "Regina José Galindo: Sala de Vídeo",
        "artist": "Regina José Galindo",
        "style": ["Video Art", "Performance"],
        "date_start": "2026-07-03",
        "date_end": "2026-08-23",
        "status": "open",
        "description": "Guatemalan artist explores political violence, the female body and collective memory through video and performance works.",
        "description_pt": "Artista guatemalteca explora violência política, corpo feminino e memória coletiva através de vídeo e performance."
    },
    {
        "gallery_name": "MASP",
        "title": "Damián Ortega: matéria e energia",
        "artist": "Damián Ortega",
        "style": ["Sculpture", "Installation", "Conceptual"],
        "date_start": "2026-05-15",
        "date_end": "2026-09-13",
        "status": "open",
        "description": "First major solo exhibition of the Mexican artist in Brazil. Decomposes everyday objects to investigate materiality and politics.",
        "description_pt": "Primeira grande individual do artista mexicano no Brasil. Decompõe objetos cotidianos para investigar materialidade e política."
    },
    {
        "gallery_name": "Pinacoteca de São Paulo",
        "title": "Macunaíma é Duwid",
        "artist": "Group show",
        "style": ["Brazilian Art", "Indigenous Art", "Contemporary"],
        "date_start": "2026-01-01",
        "date_end": "2026-12-31",
        "status": "open",
        "description": "Group show that revisits Mário de Andrade from an indigenous perspective, confronting modernism with the cosmologies of original peoples.",
        "description_pt": "Coletiva que revisita Mário de Andrade com perspectiva indígena, confrontando o modernismo com cosmologias dos povos originários."
    },
    {
        "gallery_name": "Pinacoteca de São Paulo",
        "title": "Beatriz Milhazes: obra gráfica",
        "artist": "Beatriz Milhazes",
        "style": ["Brazilian Art", "Prints", "Contemporary"],
        "date_start": "2026-05-01",
        "date_end": "2026-12-31",
        "status": "open",
        "description": "Special room with 23 years of graphic production by Milhazes in collaboration with Durham Press (New York). Donated by the artist to the Pinacoteca.",
        "description_pt": "Sala especial com 23 anos de produção gráfica de Milhazes em colaboração com a Durham Press (Nova York). Doado pela artista à Pinacoteca."
    },
    {
        "gallery_name": "MAB FAAP",
        "title": "Miró: Mestre das Formas",
        "artist": "Joan Miró",
        "style": ["Modern Art", "Surrealism", "International"],
        "date_start": "2026-08-07",
        "date_end": "2026-10-12",
        "status": "open",
        "description": "Over 100 original works by Joan Miró — paintings, sculptures, engravings, tapestries and photographs, many exhibited in Brazil for the first time.",
        "description_pt": "Mais de 100 obras originais do catalão Joan Miró — pinturas, esculturas, gravuras, tapeçarias e fotografias, muitas inéditas no Brasil. Curadoria de Jordi J. Clavero."
    },
    {
        "gallery_name": "Instituto Tomie Ohtake",
        "title": "Luiz Zerbini: Estrelas escolhidas",
        "artist": "Luiz Zerbini",
        "style": ["Contemporary", "Installation", "Brazilian Art"],
        "date_start": "2026-06-26",
        "date_end": "2026-08-16",
        "status": "open",
        "description": "230 works — monotypes, paintings, artist books and installations with botanical materials from Inhotim and Sítio Burle Marx.",
        "description_pt": "230 obras — monotipias, pinturas, livros de artista e instalações com materiais botânicos do Inhotim e Sítio Burle Marx."
    },
    {
        "gallery_name": "IMS Paulista",
        "title": "O que elas viram: fotolivros históricos de mulheres, 1843–1999",
        "artist": "Group show",
        "style": ["Photography", "Documentary", "Historical"],
        "date_start": "2026-03-07",
        "date_end": "2026-08-03",
        "status": "open",
        "description": "Around 100 works by women photographers over more than 150 years, highlighting pioneering figures made invisible by photographic history.",
        "description_pt": "Cerca de 100 obras de fotógrafas mulheres ao longo de mais de 150 anos, destacando pioneiras invisibilizadas da história fotográfica mundial."
    },
    {
        "gallery_name": "IMS Paulista",
        "title": "Zumví Arquivo Afro Fotográfico",
        "artist": "Group show",
        "style": ["Photography", "Documentary", "Afro-Brazilian"],
        "date_start": "2026-01-01",
        "date_end": "2026-12-31",
        "status": "open",
        "description": "Over 400 photographs documenting political movements, afro blocos, religious practices and popular markets in Bahia.",
        "description_pt": "Mais de 400 fotografias sobre movimentos políticos, blocos afro, religiosidades e mercados populares da Bahia."
    },
    {
        "gallery_name": "Itaú Cultural",
        "title": "Solange Pessoa: outras escalas",
        "artist": "Solange Pessoa",
        "style": ["Contemporary", "Installation", "Brazilian Art"],
        "date_start": "2026-08-04",
        "date_end": "2026-11-01",
        "status": "open",
        "description": "First solo exhibition of the Minas Gerais artist in Brazil — 150 unpublished drawings, films and installation with organic materials.",
        "description_pt": "Primeira individual da artista mineira no Brasil — 150 desenhos inéditos, filmes e instalação. Pesquisa com materiais orgânicos como terra, couro e penas."
    },
    {
        "gallery_name": "Galeria Vermelho",
        "title": "Suspicious Mind",
        "artist": "Group show",
        "style": ["Contemporary", "Experimental"],
        "date_start": "2026-08-01",
        "date_end": "2026-08-31",
        "status": "open",
        "description": "August group show at the gallery reference in experimental contemporary art, founded in 2002 in three restored houses in Higienópolis.",
        "description_pt": "Mostra coletiva de agosto da galeria referência em arte contemporânea experimental, fundada em 2002 em três casas restauradas em Higienópolis."
    },
    {
        "gallery_name": "Nara Roesler Gallery",
        "title": "Antes da forma, o encanto — Mônica Ventura",
        "artist": "Mônica Ventura",
        "style": ["Contemporary", "Brazilian Art"],
        "date_start": "2026-05-26",
        "date_end": "2026-08-01",
        "status": "open",
        "description": "Curated by Catarina Duncan. Revisits the colonial genealogy of the fetish to propose a symbolic system of matter, ritual and form.",
        "description_pt": "Curadoria de Catarina Duncan. Revisita a genealogia colonial do 'fetiche' para propor sistema simbólico de matéria, ritual e forma."
    },
    {
        "gallery_name": "Mendes Wood DM",
        "title": "Lygia Pape: Sendo",
        "artist": "Lygia Pape",
        "style": ["Contemporary", "Conceptual", "Brazilian Art"],
        "date_start": "2026-04-07",
        "date_end": "2026-08-01",
        "status": "open",
        "description": "First solo gallery exhibition dedicated to Lygia Pape (1927–2004). Works that evidence the conceptual and sensorial radicality of the artist.",
        "description_pt": "Primeira individual da galeria dedicada a Lygia Pape (1927–2004). Reúne obras que evidenciam a radicalidade conceitual e sensorial da artista."
    },
    {
        "gallery_name": "Fortes D'Aloia & Gabriel",
        "title": "Iran do Espírito Santo: Peças Frias — O Desenho",
        "artist": "Iran do Espírito Santo",
        "style": ["Contemporary", "Conceptual", "Sculpture"],
        "date_start": "2026-06-30",
        "date_end": "2026-08-31",
        "status": "open",
        "description": "Drawings and sculptures from 2007 to 2025. Rigorous geometries and empty space as central elements.",
        "description_pt": "Desenhos e esculturas de 2007 a 2025. Geometrias rigorosas e espaço vazio como elementos centrais da prática."
    },
    {
        "gallery_name": "Galeria Luisa Strina",
        "title": "Alfredo Jaar: O Lado Escuro da Lua",
        "artist": "Alfredo Jaar",
        "style": ["Contemporary", "Conceptual", "International"],
        "date_start": "2026-08-08",
        "date_end": "2026-12-31",
        "status": "open",
        "description": "48 works created during the Pinochet dictatorship. Jaar is known for works about media silence and genocide.",
        "description_pt": "48 obras criadas nas décadas de 1970 e 1980 durante a ditadura de Pinochet. Jaar é conhecido por trabalhos sobre silêncio midiático e genocídio."
    },
    {
        "gallery_name": "Casa Triângulo",
        "title": "Vânia Mignone: Sem Palavras",
        "artist": "Vânia Mignone",
        "style": ["Contemporary", "Brazilian Art"],
        "date_start": "2026-08-01",
        "date_end": "2026-08-31",
        "status": "open",
        "description": "Solo exhibition celebrating 30 years of partnership between the artist and Casa Triângulo.",
        "description_pt": "Individual que celebra 30 anos de parceria entre a artista e a Casa Triângulo."
    },
    {
        "gallery_name": "Zipper Galeria",
        "title": "Flávia Junqueira: Tudo que inventei aconteceu",
        "artist": "Flávia Junqueira",
        "style": ["Contemporary", "Painting", "Installation"],
        "date_start": "2026-08-08",
        "date_end": "2026-09-19",
        "status": "open",
        "description": "Solo show exploring the boundary between imagination and memory through painting and installation.",
        "description_pt": "Individual explorando a fronteira entre imaginação e memória via pintura e instalação."
    },
    {
        "gallery_name": "Galeria Raquel Arnaud",
        "title": "Carlos Zilio: nem mais nem menos, pinturas recentes",
        "artist": "Carlos Zilio",
        "style": ["Contemporary", "Painting", "Brazilian Art"],
        "date_start": "2026-06-10",
        "date_end": "2026-08-22",
        "status": "open",
        "description": "Curated by Tadeu Chiarelli. Recent paintings investigating the specificity of painting as presence — not discourse.",
        "description_pt": "Curadoria de Tadeu Chiarelli. Pinturas recentes investigando a especificidade da pintura como presença — não discurso."
    },
    {
        "gallery_name": "Galeria 18",
        "title": "Habitar a Paisagem — Flávia Fabbriziani",
        "artist": "Flávia Fabbriziani",
        "style": ["Contemporary", "Brazilian Art"],
        "date_start": "2026-08-05",
        "date_end": "2026-09-05",
        "status": "open",
        "description": "Solo show curated by Jurandy Valença. Contemporary art in a welcoming and plural environment.",
        "description_pt": "Individual com curadoria de Jurandy Valença. Arte contemporânea em ambiente receptivo e plural."
    },
    {
        "gallery_name": "Luciana Brito Galeria",
        "title": "Fabiana de Barros: Imagens do Interior",
        "artist": "Fabiana de Barros",
        "style": ["Contemporary", "Brazilian Art", "Installation"],
        "date_start": "2026-08-22",
        "date_end": "2026-10-17",
        "status": "open",
        "description": "Engravings, collages and mineral resin assemblages, including holographic installation in the garden designed by Burle Marx.",
        "description_pt": "Gravuras, colagens e assemblages de resina mineral, incluindo instalação holográfica no jardim projetado por Burle Marx."
    },
    {
        "gallery_name": "Simões de Assis",
        "title": "Ayrson Heráclito: Ojú-Inú",
        "artist": "Ayrson Heráclito",
        "style": ["Contemporary", "Afro-Brazilian", "Installation"],
        "date_start": "2026-08-08",
        "date_end": "2026-12-31",
        "status": "open",
        "description": "Works shaped by Afro-Brazilian cosmology and ritual references that guide the practice of the Bahian artist.",
        "description_pt": "Obras atravessadas pela cosmologia afro-brasileira e pelas referências rituais que orientam a prática do artista baiano."
    },
]

def add_sp():
    # Add galleries
    result = galleries_collection.insert_many(galleries)
    print(f"✓ {len(result.inserted_ids)} galleries added!")

    # Add exhibitions
    result = exhibitions_collection.insert_many(exhibitions)
    print(f"✓ {len(result.inserted_ids)} exhibitions added!")

if __name__ == "__main__":
    add_sp()
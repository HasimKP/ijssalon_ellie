prijzen = {
    "aardbei": 3,
    "Vanille": 4,
    "chocolade": 5,
    }
aanbieding = 0.8 * prijzen["aardbei"]
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding} "
reclame_tekst2 = reclame_tekst[:62]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el) < 4:
        print(el.lower())
    else:
        print(el.upper())

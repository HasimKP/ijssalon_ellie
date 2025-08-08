from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    tekst = f"vandaag in de aanbieding: emmertje ijs(1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro"
    print(tekst)

aanbieding_1('coco', 5, 4) 

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(inkomsten, 0.09))

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

print(laag_en_hoog(inkomsten))

def gemiddelde(mijn_lijst):
    gem = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gem} euro."

print(gemiddelde(inkomsten))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

getallen = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(getallen))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)

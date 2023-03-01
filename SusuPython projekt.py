import random



# Kezdeti pontok
kezdeti_ugyesseg = 0
kezdeti_eletero = 0
kezdeti_szerencse = 0

# Dobókockával a képességek meghatározása
kezdeti_ugyesseg += 6 + random.randint(1, 6)
kezdeti_eletero += 12 + random.randint(1, 6) + random.randint(1, 6)
kezdeti_szerencse += 6 + random.randint(1, 6)

# Kalandlap
kalandlap = {
    "Ügyesség": kezdeti_ugyesseg,
    "Életerő": kezdeti_eletero,
    "Szerencse": kezdeti_szerencse
}

# A kalandlap megjelenítése
print("Kezdeti pontok:")
for key, value in kalandlap.items():
    print(f"{key}: {value}")


class Csata:

  def __init__(self, teremtmeny_ugyesseg, jatekos_ugyesseg, teremtmeny_eletero, jatekos_eletero, teremtmeny_szerencse, jatekos_szerencse):

    self.teremtmeny_ugyesseg = teremtmeny_ugyesseg
    self.jatekos_ugyesseg = jatekos_ugyesseg
    self.teremtmeny_eletero = teremtmeny_eletero
    self.jatekos_eletero = jatekos_eletero
    self.teremtmeny_szerencse = teremtmeny_szerencse
    self.jatekos_szerencse = jatekos_szerencse

  def harc():
  
    while teremtmeny_eletero > 0 and jatekos_eletero > 0:
    # A teremtmény támadóerejének meghatározása
      teremtmeny_tamadoero = random.randint(1, 6) + random.randint(1, 6) + teremtmeny_ugyesseg

    # A játékos támadóerejének meghatározása
      jatekos_tamadoero = random.randint(1, 6) + random.randint(1, 6) + jatekos_ugyesseg

    # A támadóerők összemérése
    if jatekos_tamadoero > teremtmeny_tamadoero:
      print("Nyertél!")
      teremtmeny_eletero -= 2
    elif teremtmeny_tamadoero > jatekos_tamadoero:
      print("A teremtmény Nyert!")
      jatekos_eletero -= 2
    else:
      print("Döntetlen! Kezd újra!")

    # A szerencse használata
    if teremtmeny_szerencse > 0:
      teremtmeny_szerencse -= 1
      teremtmeny_eletero += 1
    if jatekos_szerencse > 0:
      jatekos_szerencse -= 1
      jatekos_eletero += 1

    if jatekos_eletero > 0:
      return "Nyertél!"
    else:
      return "A teremtmény nyert!"

valasz_igen = ["Igen", "I", "igen", "i"]
valasz_nem = ["Nem", "N", "nem", "n"]
tovabb_valasz = ["t"]
nyertel_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]
irany_valasz = ["észak", "nyugat"]
szetnezni_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]

print("""
1.
Belöknek a lenti alagútba, és rád zárják az ajtót, kizárva ezzel a nyíláson át beszűrődő természetes világosságot. Innentől kezdve kizárólag a falra rögzített fáklyáktól remélhetsz valamennyi fényt. Ahogy szemed hozzászokik a homályhoz, látod, hogy az alagút észak felé indul. Nagyot sóhajtasz a dolog igazságtalansága felett, majd elindulsz abba az irányba. Lapozz a 41-re. A továbbhaladáshoz nyomd meg a 't' betűt!""")

tovabb = input("")

if tovabb in tovabb_valasz:
    print("\n41. Az alagút, bár folyamatosan jobbra-balra kanyarog, nagyjából mégis tartja az északi irányt, végül élesen oldalra kanyarodik, és ekkor majdnem belefutsz egy fekete köpenybe öltözött alakba. Tőrt tart a kezében, az arcán ülő tekintet rettegésről árulkodik! Rájössz, hogy nem te vagy az egyetlen, akit most próbára tesznek, és hogy mindketten ugyanazon Szobor után kutattok. A fickó rád veti magát, nyilvánvaló, hogy mielőbb végezni akar veled. Harcolnod kell! Tolvaj: ÜGYESSÉG: 7 ÉLETERŐ: 6 Ha győzöl, lapozz a 85-re.\n")


teremtmeny_ugyesseg = 7
jatekos_ugyesseg = kezdeti_ugyesseg
teremtmeny_eletero = 6
jatekos_eletero = kezdeti_eletero

nyertel = input("Nyertél? [Igen/Nem]")
if nyertel_valasz == "igen":
    print("\n85. A Tolvajnál mindössze 3 Aranytallert és egy háromszög alakú, penészes gyümölcsöt találsz. Még soha nem láttál chhez hasonlót, de gyanitod, hogy ez lehet a Xentos, a hosszú élet gyümölcse. Ha nem lenne ilyen borzalmas állapotban, gond nélkül megko káztatnád, hogy belekóstolj, igy azonban úgy döntesz, hogy itt hagyod és folytatod az utad észak felé. Hamarosan egy útelágazás-hoz érsz. Ha továbbra is északnak tartasz lapozz a 108-ra. Ha a nyugati irányba lo gazó új járaton mennél tovább, lapozz a 147-re.\n")
else: print("Vesztettél!")
  

irany = input("Melyik irányba szeretnél tovább haladni? [észak/nyugat]")
if irany_valasz == "észak":
  print("\n108. Északi irányba követed az átjárót. Hamarosan elérsz egy keleti elágazáshoz. Hogyha egyenesen mész tovább, lapozz a 146-ra. Ha letérsz jobbra, lapozz a 79-re.\n")

else: 
    print("\n144. Mikor már félúton jársz a fényfolt felé, a talaj megnyílik alattad, de még az elött sikerül visszalépned, hogy te is beleesnél - korábbi óvatosságod meghozta gyümölcsét. Ahogy közelebbről is megvizsgálod, megállapítod, hogy egy kis, kör alakú verem az a padló kellős közepén. Rozoga létra fut lefelé végig az oldalán, de vagy túl sötét van, vagy túl mély lyuk, mert nem látod az alját. Ha szét akarsz nézni benne, lapozz a 7-re. Ha inkább átugórnád és kiderítenéd, mi a fényfolt forrása, lapozz a 96-ra.\n")

szetnezni = input("Szét akarsz nézni benne?")
if szetnezni_valasz == 'Igen':
  print('\n7. Mikor végül eléred a verem alját, semmit nem látsz. A falakat végigtapogatva annyit meg tudsz állapítani, hogy az alagút kelet felé megy tovább. Ha a vaksötét ellenére is bevállalod ezt a járatot, lapozz a 165-re. Ha inkább visszatérnél a fenti folyosóra és északnak folytatnád az utad, lapozz a 96-ra.\n')

else: print('\n 96. Az alagút kanyarulata mögül túlvilági ragyogás árad. Ahogy a falra vetült játékot nézed, úgy érzed, a fény magától lüktet és változtatja a színét. Nagyon óvatosan fordulsz be a kanyarban, amin tul igen bizarr látvány fogad. Három nagyon alacsony, ezüstszínů, lebegő kopenybe öltözött alak táncol valamilyen rituális táncot a fény forrása körül. Az üreg falát itt mindenhol tükrök borítják, és a változó színek oda- vissza ugrálnak azok közt, a lüktető ragyogástól és szédülés tör rád. A forrás egy hatalmas kristály, mely egy magas talapzaton nyugszik, de képtelen vagy megállapítani, pontosan miféle kő is ez. Egyébként sincs idöd sokat spekulálni ezen, mivel az ezernyi tükörképnek köszönhetően az ala- kok felfigyelnek egy óvatlan mozdulatodra. A lények dühödten felkiáltva vetik rád magukat. Egy ellenfélként küzdj meg vele. Ha győzöl, lapozz a 191-re.\n')

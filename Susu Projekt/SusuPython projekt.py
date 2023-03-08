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

    if nyertel1_valasz == 'Nem':
      return "Vesztettél!"
    if nyertel1_valasz == 'Nem':
      return "Vesztettél!"

valasz_igen = ["Igen", "I", "igen", "i"]
valasz_nem = ["Nem", "N", "nem", "n"]
tovabb_valasz = ["t"]
nyertel1_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]
nyertel2_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]
irany_valasz = ["észak", "nyugat", "Észak", "Nyugat"]
szetnezni_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]
lyuk_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]
megnezed_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]
lebeges_kopenye_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]
szerencse_valasz = ["Igen", "I", "igen", "i", "Nem", "N", "nem", "n"]

print("\n1. Belöknek a lenti alagútba, és rád zárják az ajtót, kizárva ezzel a nyíláson át beszűrődő természetes világosságot. Innentől kezdve kizárólag a falra rögzített fáklyáktól remélhetsz valamennyi fényt. Ahogy szemed hozzászokik a homályhoz, látod, hogy az alagút észak felé indul. Nagyot sóhajtasz a dolog igazságtalansága felett, majd elindulsz abba az irányba. Lapozz a 41-re. A továbbhaladáshoz nyomd meg a 't' betűt!")

tovabb = input("")

if tovabb in tovabb_valasz:
  print("\n41. Az alagút, bár folyamatosan jobbra-balra kanyarog, nagyjából mégis tartja az északi irányt, végül élesen oldalra kanyarodik, és ekkor majdnem belefutsz egy fekete köpenybe öltözött alakba. Tőrt tart a kezében, az arcán ülő tekintet rettegésről árulkodik! Rájössz, hogy nem te vagy az egyetlen, akit most próbára tesznek, és hogy mindketten ugyanazon Szobor után kutattok. A fickó rád veti magát, nyilvánvaló, hogy mielőbb végezni akar veled. Harcolnod kell! Tolvaj: ÜGYESSÉG: 7 ÉLETERŐ: 6 Ha győzöl, lapozz a 85-re.\n")


teremtmeny_ugyesseg = 7
jatekos_ugyesseg = kezdeti_ugyesseg
teremtmeny_eletero = 6
jatekos_eletero = kezdeti_eletero

nyertel1 = input("Nyertél? [igen/nem]")
if nyertel1_valasz == "igen":
  print("\n85. A Tolvajnál mindössze 3 Aranytallert és egy háromszög alakú, penészes gyümölcsöt találsz. Még soha nem láttál chhez hasonlót, de gyanitod, hogy ez lehet a Xentos, a hosszú élet gyümölcse. Ha nem lenne ilyen borzalmas állapotban, gond nélkül megko káztatnád, hogy belekóstolj, igy azonban úgy döntesz, hogy itt hagyod és folytatod az utad észak felé. Hamarosan egy útelágazás-hoz érsz. Ha továbbra is északnak tartasz lapozz a 108-ra. Ha a nyugati irányba lo gazó új járaton mennél tovább, lapozz a 147-re.\n")
if nyertel1_valasz == "nem":
  print("Vesztettél!")
      
irany = input("Melyik irányba szeretnél tovább haladni? [észak/nyugat]")
if irany_valasz == "észak":
  print("\n108. Északi irányba követed az átjárót. Hamarosan elérsz egy keleti elágazáshoz. Hogyha egyenesen mész tovább, lapozz a 146-ra. Ha letérsz jobbra, lapozz a 79-re.\n")

if irany_valasz == "nyugat":
  print("\n144. Mikor már félúton jársz a fényfolt felé, a talaj megnyílik alattad, de még az elött sikerül visszalépned, hogy te is beleesnél - korábbi óvatosságod meghozta gyümölcsét. Ahogy közelebbről is megvizsgálod, megállapítod, hogy egy kis, kör alakú verem az a padló kellős közepén. Rozoga létra fut lefelé végig az oldalán, de vagy túl sötét van, vagy túl mély lyuk, mert nem látod az alját. Ha szét akarsz nézni benne, lapozz a 7-re. Ha inkább átugórnád és kiderítenéd, mi a fényfolt forrása, lapozz a 96-ra.\n")

szetnezni = input("Szét akarsz nézni benne?")
if szetnezni_valasz == "igen":
  print('\n7. Mikor végül eléred a verem alját, semmit nem látsz. A falakat végigtapogatva annyit meg tudsz állapítani, hogy az alagút kelet felé megy tovább. Ha a vaksötét ellenére is bevállalod ezt a járatot, lapozz a 165-re. Ha inkább visszatérnél a fenti folyosóra és északnak folytatnád az utad, lapozz a 96-ra.\n')

if szetnezni_valasz == "nem":
  print('\n 96. Az alagút kanyarulata mögül túlvilági ragyogás árad. Ahogy a falra vetült játékot nézed, úgy érzed, a fény magától lüktet és változtatja a színét. Nagyon óvatosan fordulsz be a kanyarban, amin tul igen bizarr látvány fogad. Három nagyon alacsony, ezüstszínů, lebegő kopenybe öltözött alak táncol valamilyen rituális táncot a fény forrása körül. Az üreg falát itt mindenhol tükrök borítják, és a változó színek oda- vissza ugrálnak azok közt, a lüktető ragyogástól és szédülés tör rád. A forrás egy hatalmas kristály, mely egy magas talapzaton nyugszik, de képtelen vagy megállapítani, pontosan miféle kő is ez. Egyébként sincs idöd sokat spekulálni ezen, mivel az ezernyi tükörképnek köszönhetően az ala- kok felfigyelnek egy óvatlan mozdulatodra. A lények dühödten felkiáltva vetik rád magukat. Egy ellenfélként küzdj meg vele. Ha győzöl, lapozz a 191-re.\n')

nyertel2 = input("Nyertél? [igen/nem]")
if nyertel2_valasz == "igen":
  print("\n191. A három teremtmény estèt ikatata fo jenkint Aranytallért találsz. Eztina Kristályhoz lepsz, a belőle áradó, gytery rien biktető feny azonban már halványodni kendett, és mire felemeled, már csak egy nagy, driddelen avugombot tartasz a ke zodben. Kirumkodva vagod a foldhor, abol darabokra torik. A barlangban azon kival cupin egyetlen érdekes dolgot találsz egy nagyjából egy méter mórójú lyukat a fal- ban, több moter magasan. Elé húzod az emelvényt, melyen korábban a kristály állt, thills es batekintesz rajta. Sina csúszdát pillantasz meg, mely anyhén lelle lujt. He eran a lyuk at akarod folytatni at utal, la- pozz a 123-m. Ha az északi alagúton it tivomál, lapozz a 33-ra\n")
if nyertel2_valasz == "igen":
  print("Vesztettél!")

lyuk = input("Ezen a lyukon át akarod folytatni?")
if lyuk_valasz == 'igen':
  print("\n123. Nagy nehezen bemászol a lyukba és ereszkedni kezdesz. A levegő hőmérsékleté rohamosan növekedni kezd, és rájössz, hogy nagy hibát követtél el. Egyenesen egy föld-alatti kemence felé tartasz. Lángnyelvek csapnak feléd, ahogy próbálsz visszamászni a lejtőn. Kétségbeesetten kaparod a falat, de képtelen vagy megakadályozni, hogy a tűz kellős közepébe ne zuhanj. Ahogy a csúszda végéhez közeledsz, már a láng pattanásait is hallod, és megpillantod a pokoli lángnyelveket. Lendületed miatt egy ideig még a levegőben repülsz utána azonban, ahogy fejjel előre a tűzbe zuhansz, a szörnyű meleg egy pillanat alatt füstpamaccsá változtat. Kalandod itt véget ér, VESZTETTÉL!\n")

if lyuk_valasz == "nem":
  print("\n33. Az alagút egy ideig kanyarog, de végig észak felé megy. Hamarosan egy ajtó jelenik meg a jobb oldali falban. Ha megnézed nyitva van-e. Lapozz, az 5-re. Ha inkább hagynád az ajtót és tovább folytatnád az utadat. lapozz a 14-re.\n")

megnezed = input("Megnézed? [igen/nem]")
if megnezed_valasz == "igen":
  print("\n5. Az ajtó egy tágas terembe nyílik, melynek északi oldalán egy újabb kijárat van, egy lelógó kötél szomszédságában. Csapdának nem látod jelét, így áthaladsz a szobán és leveszed a kötelet. Lenyomod a kilincset, de így sem sikerül előrébb jutnod, alighanem zárva van. Ha van nálad egy Aranykulcs, lapozz a 110-re. Hogyha nincs, úgy távozol a szobából és folytatod, az utadat északi irányba lapozz a 14-re\n")

if megnezed_valasz == "nem":
  print("\n14. Ahogy észak felé haladsz. Nyugatról egy alagutat látsz befutni. Úgy döntesz, inkább egyenesen mész tovább. Lapozz a 67-re. A továbbhaladáshoz nyomd meg a 't' betűt!\n")

tovabb = input("")

if tovabb in tovabb_valasz:
  print("\n67 Az alagút hamarosan tágulni kezd és csodálatos látvány tárul a szemed elé. Egy földalatti völgyet határoló magas sziklafal kellős közepén, egy keskeny szirten találod magad. Nem látsz lefelé vezető utat, és nem mered megkockáztatni, hogy visszafordulj, Nálad van a Lebegés Köpenye? Ha igen, lapozz a 105-re. Ha nem, lapozza 86-ra\n")

lebeges_kopenye = input("Nálad van a Lebegés Köpenye [igen/nem]")
if lebeges_kopenye_valasz == "igen":
  print("\n105. Döbbenten veszed észre, hogy köpenyed felfúvódik és felemel a lábadról. Lassan lebegsz le a talajra, és könnyedén érsz földet. Alig mered elhinni, mekkora szerencséd van. Lapozza 27- re.\n")
if lebeges_kopenye_valasz == "nem":
  print("\n86. Ahogy körbenézel, észreveszed egy kötelet, amit egy nagyméreti sziklához kötöztek Amennyire cinéred, nincs túl jó állapotban, és azt sem látod, milyen mélyen ér le a szakadókba, de úgy tűnik, ez az egyetlen lehetőséged a lejutásra, Tedd próbára - EN Hogyha szerencséd van, lapozz a 190-re. Ha nincs, lapozz a 4-re.\n")

tovabb = input("")

if tovabb in tovabb_valasz:
  print("\n27. Egy hatalmas völgy lábánál állsz, melyet egy gyors folyású folyó vájt ki. Próbálsz valami megoldást találni az átkelésre, de csak egy kicsi, eléggé rozoga és korhadt hidat látsz. Ahogy megközelíted, látod. amint két óriási termesz eszi a fát. Hófehér testükön igen nyugtalanítóan hat két vérvörös szemük. A lények bármelyike bármikor beléd marhatna. Ha sietsz talán még sikerül átkelned rajta azelőtt, hogy végleg összeroskadna. A másik lehetőséged, hogy megpróbálsz átúszni a sebes folyón. Ha az első megoldást választod, lapozz a 40-re. Ha úgy gondolod, elég jó úszó vagy. ezzel próbálkoznál, lapozz a 2-re.\n")

szerencse = input("Próbára tetted a szerencséd. Volt szerencséd vagy nem? [igen/nem]")
if szerencse_valasz == "igen":
  print("\n190:Már majdnem dired a sziklaszint aljat amikor a kötel clogy Innon le kell uera- nod. Nagyjából két méterre van alattad a talaj, de clég sildas. Tad próbána - cao Ta szarencsés vagy, biztonsághan sebesülés nélkül landols a talajon lapozz 27. Hogyha nincs szurumusod, lapozz 54-es.\n")

if szerencse_valasz == "nem":
  print("\n4. A kötél igen rossz állapotban van, és még félúton sem jársz, mikor elszakad... Kalandod itt véget ér.\n")
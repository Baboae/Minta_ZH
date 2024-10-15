https://elearning.unideb.hu/mod/page/view.php?id=145542

Állatok
Előkészületek
Hozz létre egy zoo csomagot!
Az állatokat ábrázoló osztály
Készíts egy osztályt, mely segítségével állatokat ábrázolhatunk. Az osztályt helyezd a zoo csomag model moduljába. Egy állat három attribútummal rendelkezik:
az állat faja (sztring, publikus)
az állat kora (valós, privát)
az állat súlya (valós, védett)
Egészítsd ki az osztályt egy konstruktorral, amelynek segítségével mindhárom adattagjának kezdőérték adható. A kor alapértelemzett értéke legyen 0.0.
Definiálj egy-egy tulajdonságot, mellyel lekérdezhető egy állat kora és súlya. Biztosíts arra lehetőséget, hogy egy állat súlyát módosítani is lehesssen.
Definiáld felül a __repr__() metódust úgy, hogy az állat adatait vesszőkkel és szóközökkel elválasztva adja vissza.
Definiáld felül az __str__() metódust úgy, hogy az állat adatait az alábbiak szerint adja vissza:
formátum: "<faj>: <kor> év, <súly> kg"
példa: "elefánt: 3.5 év, 870.0 kg"
Definiáld felül az __eq__() metódust úgy, hogy két állat akkor legyen egyenlő, ha mindhárom adattagjuk megegyezik.
Egészítsd ki az osztály definícióját úgy, hogy példányai a következők szerint legyenek összehasonlíthatók:
a faj szerint növekvő sorrend
a kor szerint csökkenő sorrend
a súly szerint növekvő sorrend
Egészítsd ki az osztály definícióját egy statikus metódussal, amely paraméterként megkap egy állatokat tartalmazó listát és egy fajnevet. A metódus adja vissza, hogy a megadott fajhoz milyen életkorú példányok tartoznak a listában.
Az emlősöket ábrázoló osztály
Származtass az állatokat leíró osztályból egy olyan osztályt, mely emlősöket reprezentál. Ezt az osztályt is a model modulba helyezd el. Az emlősök az állatok tulajdonságain kívül még egy további adattaggal is rendelkeznek:
a lábak száma (egész, privát)
Egészítsd ki az osztályt egy konstruktorral, amelynek segítségével mind a négy adattagjának kezdőérték adható. A kor az emlősök esetében is rendelkezzen alapértelmezett értékkel.
Definiálj egy tulajdonságot, mellyel lekérdezhető és beállítható a lábak száma.
Definiáld felül a __repr__() metódust úgy, hogy az adatokat vesszőkkel és szóközökkel elválasztva adja vissza. A megoldásban használd fel az örökölt __repr__() metódust is.
Definiáld felül az állatokat leíró osztályból örökölt __str__() metódust úgy, hogy az emlősök adatait az alábbiak szerint adja vissza. A megoldásban használd fel az örökölt __str__() metódust is.
formátum: "<faj>: <kor> év, <súly> kg (lábak száma: <lábakSzáma>)"
példa: "elefánt: 3.5 év, 870.0 kg (lábak száma: 4)"
Főprogram
Készíts egy test nevű modult a zoo csomagban, amely a főprogramot tartalmazza. A főprogram csak akkor kerüljön meghívásra, ha valóban ezt a modult interpretálják közvetlenül.
A standard inputon állatok adatait találod. Egészítsd ki úgy a főprogramot, hogy az alábbiak szerint tudja őket beolvasni és feldolgozni:
Az állatok számát (n) az első parancssori argumentum adja meg.
Ha a program nem rendelkezik parancssori argumentummal (vagy az nem egy pozitív egész értéket tartalmaz), akkor azt egy kivétel eldobásával jelzi.
A bemeneten pontosan n darab sor szerepel, mindegyikben egy-egy állat adatai találhatók a következő formában:
"<faj>;<év>;<súly>" állatok esetén
"<faj>;<év>;<súly>;<lábakSzáma>" emlősök esetén
A program beolvassa, majd egy listában tárolja el a bemeneten szereplő állatokat.
A program rendezi a listát, majd a standard kimenetre írja a tartalmát (soronként egy-egy elemet).
Példa input
(Nem szabad elfeledkezni a parancssorról: az alábbi input használata esetén egy 6-ost kell elhelyezni benne.)

pelikán;3;12
róka;4;17;4
elefánt;3.5;8700;4
pelikán;3;11
csimpánz;5;47;2
pelikán;4;10

"""
1. Afișați în consolă rezultatul expresiei: 9 * (12-5) - 2**3
2. Se știe că Andrei are 7 mere. Ana are de 3 ori mai multe mere decât Andrei,
iar Ștefan are de 49 de ori mai multe mere decât Andrei. Să se afle câte mere au cei
trei copii în total folosindu-se o expresie care conține adunarea, înmulțirea și ridicarea la putere (+,*,**).
3. Creați un convertor de timp, transformând astfel orele și minutele introduse de la tastatură în secunde.
Exemplu: Pentru ore=5, minute=54, se va tipări 21240 de secunde.
4. Alex a încheiat o cursă pe locul al x-lea (x - variabila introdusă de la tastatură).
La sosire Alex a aflat că fiecare al y-lea alergător a fost descalificat. Pe ce loc este Alex acum?
Exemplu: x=2012, y=7; se tipărește: "Alex a terminat pe locul 1725".
5. Citim de la tastatură un nr natural a. Puteți calcula suma numerelor naturale mai mici sau egale cu a?
6. Folosind un număr de 5 cifre, scrieți un program care să afișeze numărul obținut prin inversarea primelor două cifre ale sale cu ultimele două cifre. Exemplu: Pentru numărul 12345, obținem numărul 45312.
7. Fie x un număr natural de exact 4 cifre. Să se calculeze produsul cifrelor sale.
Exemplu: pentru x=2147 se va afișa 56 (2*1*4*7=56).
8. Cifru
Fifi primește cadou de la fratele mai mare un jurnal. Pentru a-l putea deschide trebuie introdus un cifru, număr natural format din 4 cifre. Fratele lui Fifi îi spune un număr de patru cifre și îi precizează că cifrul este cel mai mare număr care se obține din acesta prin permutarea circulară cu o poziție a cifrelor numărului. Știind numărul, ajutați-l pe Fifi să găsească cifrul pentru a putea deschide jurnalul.
Exemplu: dacă numărul spus de fratele lui Fifi este 1234, cifrul este 4123 (prin permutarea circulară cu o poziție se obțin numerele 2341, 3412, 4123, 1234, iar maximul este 4123).
9. Se citește un număr "n" de la tastatură. Dacă acesta aparține intervalului [1, 100], se va afișa mesajul: "Este cuprins între 1 și 100". În caz contrar se va afișa: "Nu este cuprins între 1 și 100".
10. Se citesc numerele naturale x şi y. Să se calculeze produsul lor, fără a utiliza operatorul de înmulţire.
11. Fie n un număr natural cu cel puțin două cifre și maxim nouă cifre. Să se verifice dacă numărul n și numărul obținut din n prin interschimbarea primei cifre cu ultima cifră sunt ambele numere prime.
Exemplu: numărul 137 nu îndeplinește condițiile deoarece 731 (numărul obținut după interschimbarea cifrelor) nu este prim. Numărul 179 îndeplinește condițiile deoarece și 179 și 971 sunt numere prime.
12. Într-o cutie se află 300 de bile, numerotate cu numere începând de la unu, din trei în trei. Toate bilele cărora le corespund numere pare sunt verzi. Să se afle câte bile verzi sunt.
13. Verificați dacă un șir de caractere citit are sau nu lungimea mai mare decât 20.
14. Se introduce un șir de caractere. Afișați-l cu majuscule, citit de la dreapta la stânga.
15. Se citește un șir de caractere. Afisați câte caractere are șirul.
16. Se citește o propoziție de la tastatură. Să se afișeze câte vocale, respectiv câte consoane se află în aceasta. Exemplu: Fred merge pe plajă. Se afișează: 10 consoane și 6 vocale.
17. Alfabetul pythonistilor. Noi, pythoniștii, ne-am întelege mult mai bine într-o limbă, a noastră, for fun! E o regulă foarte simplă: după fiecare cuvânt, se adaugă respectivul cuvânt, dar scris invers. Realizează programul!
Exemplu: se citește "Noi suntem informaticieni." --- se traduce ca: "Noiion suntemmetnus informaticieniineicitamrofni."
18. Să se afle câte numere impare se găsesc între 24 și 800.
19. Campionatul mondial de Formula 1 a decis să penalizeze anumiți piloți pentru încălcarea regulilor. Astfel se acordă poziții de penalizare pe grila de start în funcție de gravitatea abaterii. Se cere să se ordoneze clasamentul după acordarea tuturor penalizărilor.
Date de intrare: fiecare pilot are un cod unic format din mai multe părți astfel:
Prima cifră reprezintă numărul echipei din care face parte pilotul
A doua cifră și a treia cifră formează numărul de cursă al pilotului
A patra și a cincea cifră reprezintă poziția de pe grila de start a pilotului
Ultimele două cifre reprezintă numărul de poziții cu care este penalizat pilotul
Se vor citi 10 astfel de coduri, unul pentru fiecare pilot.
Date de ieșire: se va afișa în ordinea poziției după acordarea penalizărilor, separat printr-un spațiu, numărul echipei din care face parte pilotul și numărul acestuia. Se va trece la un rând nou după fiecare rezultat.
20. Proiect - Oracol.
Scrieți un program care să creeze un fișier text cu rol de jurnal personal. Programul trebuie să afișeze/informeze utilizatorul la fiecare pas, să verifice existența fișierului și să afișeze "Am creat fișierul!"; "Fișierul există, ce doriți să faceți? Introduceți 1 pentru citire, 2 pentru adăugări, 3 pentru ștergerea definitivă a fișierului, 0 pentru ieșire".
Atenție! Folosiți modulul datetime (documentați-vă pe Internet): from datetime import date și data = date.today() sau folosiți o altă metodă (citire de la tastatură) pentru a putea insera data curentă la începutul fiecărei adăugări.
"""


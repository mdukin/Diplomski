ZI

===

1.) Sustav neizrazitog upravljanja izgrađen od pravila kod kojih je neizraziti skup u konsekvensu neizrazit skup čija je funkcija pripadnosti nužno monotona konsekvens(?) je za koju vrstu zaključivanja.
	A) Mamdanijevo
	B) Tsakumotovo
	C) Zadeh
	D) TSK

2.) Sustav neizrazitog upravljanja kod kojeg je konsekvens zadan skalarnom funkcijom nad ulaznim varijablama konsekvens(?) je za koju vrstu zaključivanja.
	A) Mamdanijevo
	B) Tsakumotovo
	C) Zadeh
	D) TSK

---

Na raspolaganju je skup uzoraka oblika {(x,y)}
	- 4 uzorka: {(8,2), (9,2), (8,0), (9,0)}
Učimo mrežu INSTAR (bez naprednih mehanika) koja ima 2 neurona: 
	- N1 - početni položaj (2,1)
	- N2 - početni položaj (7,0)
Stopa učenja je 0.1.
Sličnost je definirana na temelju Euklidske udaljenosti (ne kosinusne!)
Pretpostavite da se u prvoj iteraciji na ulazu mreže dovodi prvi uzorak iz skupa (8,2)
 
3.) Označimo sa delta_1 udaljenost za koju će se u toj iteraciji pomaknuti neuron N1, a s delta_2 udaljnost za koju će se pomaknuti neuron N2. 
U odgovorima su dane ograde na te udaljenosti:
	A) delta_1 < 0.3 i delta_2 > 0.1
	B) delta_1 < 0.3 i delta_2 < 0.15
	C) delta_1 > 0.05
	D) delta_2 > 0.4

---

Nad istim skupom podataka učimo Kohonenovu samoorganizirajuću mapu izgrađenu od 3 neurona u lancu N1, N2 i N3 (tim redoslijedom).
Položaj tih neurona redom: (9,3), (11,3), (13,3). Funkcija susjedstva: f(d) = 1/(1 + (d*s)^2), pri čemu je d relevantna udaljenost 2 neurona, a s parametar.
	
4.) Razmotrite stanje koje vlada po završetku postupka učenja (npr. nakon 10000 iteracija).
Označimo s n1 broj uzoraka koji pripadaju razredu koji predstavlja neuron N1, a s n2 broj uzoraka koji pripadaju razredu koji predstavlja neuron N2.
	A) n2>n1
	B) n1=1, n2=3
	C) n1=3, n2=1
	D) n1=n2=2

5.) Ako u prvoj iteraciji mreži predoćimo drugi uzorak (tj. (9,2)) te ako je početna stopa učenja 0.1 i s=1.
	Odredite koliko će se pomaknuti neuron N3, delta_3 je taj pomak:
	A) delta_3 < 0.05
	B) delta_3 >= 0.05 i delta_3 < 0.1
	C) delta_3 >= 0.1 i delta_3 < 0.3
	D) delta_3 >= 0.3

6.) Kako postupak učenja samoorganizirajuće mreže napreduje (a prije konačnog finog podešenja) s vremenom želimo:
	A) stopu učenja smanjiti, s smanjiti
	B) stopu učenja smanjiti, s povećati
	C) stopu učenja povećati, s smanjiti
	D) stopu učenja povećati, s povećati

---

Razmatramo sustav ANFIS, obavlja preslikavanje f : R -> R.
Pravila su oblika:
	"Ako x je A onda f = k * sin(l*x) + m"
pri čemu neizraziti skup A u antecedentu ima funkciju pripadnosti oblika:
	mu_A(x) = 1/(1+(x-a)^2), a je parametar
Pretpostavimo da skup ima 2 pravila:
	(a, k, l, m) su u prvom (1, 1, 1, 1), a drugom (2, 1, 2, 0)

7.) Ako je na ulazu dovodena vrijednost 1, odredite koji će biti izlaz sustava
	A) f < 0.5
	B) f >= 1 i f < 1.4
	C) f > 1.4
	D) f >= 0.5 i f < 1

---

Neka je u skupu uzoraka za učenje evidentirano da sustav ANFIS vrijednosti 1 treba preslikavati u 0.6, koristimo pojedinačno učenje.
Stopa učenja je 0.5.
Koristimo polovično kvadratno odstupanje kao pogrešku za koji će iznos postupka korigirati parmetre a i l u prvom pravilu.

8.) Parametar l će u prvom pravilu iznositi:
	A) -0.17
	B) 0.34
	C) 0.0
	D) -0.04

9.) Parametar a će u prvom pravilu iznositi:
	A) 0.0
	B) 0.17
	C) -0.16
	D) -0.28

10.) Problem permutacija susreli smo kod:
	A) određivanja optimalnog broj pravila za sustav ANFIS
	B) traženja prikladne stope učenja mreže INSTAR
	C) određivanja broja neurona Kohonenove samoogranizrajuće
	D) učenja unaprijedne mreže evolucijskim algoritmom

11.) Implementirali smo genetski algoritam tako da kao reprezentaciju koristi polje cijelih brojeva, a zadaća mu je razviti optimalnu arhitekturu umjetne neuronske mreže. 
Primjerice ako je neki kromosom predstavljen poljem od 3 elementa (2,7,1) i ako to tumačimo kao neuronsku mrežu koja ima 3 sloja (prvi sloj ima 2 neurona, drugi sloj 7 neurona, treći sloj ima 1 neuron) koristimo kodiranje koje nazivamo:
	A) težinsko
	B) permutacijsko
	C) brojčano
	D) indirektno

12.) Za pronalazak optimalne arhitekture neuronske mreže koja obavlja preslikavanje (x,y) -> 2 koristimo stanični razvoj.
Jedno rješenje predstavljeno je stablom označenom na slici, gdje simboli u čvorovima imaju uobičajeno značenje.
Pretpostavite da su u razvijenoj mreži sve težine 1 (i nema pomaka), a prijenosna funkcija svih neurona je f(net) = (net/3)^2.
Odredite što će takva mreža dati na izlazu y ako joj se na ulaz dovede (1,2).
(Slika mreže se nalazi na originalnoj slici na [linku](https://discord.com/channels/650803962504675343/1006553759717007380/1013143638735335424))
	A) 0.25 < y < 0.5
	B) 0.5 < y < 0.75
	C) 0 < y < 0.25
	D) y > 0.75

---

Razmatramo algoritam SAPSO za učenje sustava ANFIS, n ulaza, m pravila.

13.) Što je od ponuđenog istina:
	A) broj podrojeva = m
	B) broj podčestica u svakom podroju = n
	C) dobrota podčestica u svakom podroju računa se za svaki podroj nezavisno
	D) broj parametara koje algortam optimizira = m*n

14.) Ako je trenutno položaj čestice x, koliko joj drugih položaja postupak uzima u obzir prilikom ažuriranja tog položaja čestice u nultoj iteraciji algoritma:
	A) 1
	B) 2
	C) 3
	D) 4

---

Razmatramo unaprijednu slojevitu potpuno povezanu neuronsku mrežu arhitekture "3x6x5x2".
Svi neuroni kao prijenosnu funkciju koriste sigmoidalnu funkciju.

15.) Ako težine te mreže učimo genetskim algoritmom koji kao reprezentaciju koristi polje decimalnih brojeva (tj. broj elemenata)
	A) 59
	B) 16
	C) 71
	D) 48

---

Skup uzoraka za učenje sastoji se od 4 točke u 2D; {(1,1), (2,1), (4,3), (4,4)}.
Razmatramo postupak neizrazitog grupiranja (fuzzy c-means) koji koristi dva centra; v1 = (2,1), v2 = (4,3)
Parametra M neka je 2.

16.) Odredite mjeru kojom (uz dane centre) uzorak (1,1) pripada centru v2
	A) 0.649
	B) 0.071
	C) 0.351
	D) 0.929

17.) Odredite za koju će se udaljenost pomaknuti centar v1 nakon prve iteracije algoritma.
	A) 0.3
	B) 0.1
	C) 0.8
	D) 0.5

18.) Što je istinito za ovaj algoritam neizrazitog grupiranja:
	A) Iz iteracije u iteraciju pokušava smanjiti iznos funkcije J(M, u)
	B) Garantira pronalazak optimalnih položaja centra
	C) Prilikom grupiranja samostalno može otkriti ispravan broj razreda u skupu koji grupira.
	D) Složenost mu je linearna

19.) Razmotrimo matricu M1 koja predstavlja rezultat klasičnog grupiranja te matricu M2 koja predstavlja rezultat neizrazitog grupiranja algoritmom fuzzy c-means (retci-uzorci, stupci-centri/grupe), uz pretpostavku da nismo zapeli u lokalnom optimumu.
Označimo s r_i sumu elemenata retka i, a s c_i sumu elemenata u stupcu i.
Što je od ponuđenog točno?
	A) r_i matrice M1 ne mora biti jednak r_i matrice M2
	B) c_i matrice M1 uvijek je jednak c_i matrice M2 za svaki i
	C) u matrici M1 c_i ne može biti 0
	D) r_i matrice M1 može poprimiti bilo koju vrijednost iz diskretnog skupa {0,1}

20.) U neizrazitoj logici modifikator kontrastne intenzifikacije mjeru pripadnosti 0.4 preslikava u mjeru pripadnosti:
	A) 0.4
	B) 0.32
	C) 0.6
	D) 0.16


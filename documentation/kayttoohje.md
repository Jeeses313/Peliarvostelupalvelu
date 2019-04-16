## Käyttöohje

### Ohjelman käynnistäminen

#### Paikallinen versio

1. Mene komentokehotteella kansioon, jossa sijaitsee *peliarvostelupalvelu.py*

2. Käynnistä ohjelma komennolla "python peliarvostelupalvelu.py"

3. Mene selaimessasi osoitteeseen [http://localhost:5000/](http://localhost:5000/)

4. Paikallinen versio on nyt käynnissä

#### Herokussa oleva versio

1. Mene osoitteeseen [https://peliarvostelupalvelu.herokuapp.com/](https://peliarvostelupalvelu.herokuapp.com/) tai vastaavaan osoitteeseen, jonka löydät Herokusta omalta käyttäjätililtäsi ohjelman tietojen yhteydestä

2. Herokussa oleva versio on nyt käynnissä

### Ohjelman toimintoja

Huomio! Admin voi tehdä suurimman osan asioista, joita tavallisena kirjautuneena käyttäjänä voi.

#### Navigointipalkki

##### Kaikille

* Klikkaamalla sovelluksen nimeä, ohjaudut etusivulle, joka on tyhjä

* Klikkaamalla *Pelilistaa*, ohjaudut sivulle, josta näet listan peleistä

* Klikkaamalla *Arvostelulistaa*, ohjaudut sivulle, josta näet listan arvosteluista

* Klikkaamalla *Kirjaudu*, ohjaudut kirjautumissivulle

##### Kirjautuneena

* *Kirjaudu* tilalla on käyttäjänimesi, josta ohjaudut profiilisi sivulle, ja *Kirjaudu ulos*, jolla kirjaudut ulos

#### Kirjautumissivu

* Voit kirjoittaa käyttäjätunnuksesi ja salasanasi ja kirjautua sisään

* Voit painaa *rekisteröidy*, josta ohjaudut rekisteröitymis sivulle

#### Rekisteröitymissivu ja tietojen muokkausssivu

* Voit kirjoittaa käyttäjänimesi ja kahteen kertaan salasanasi ja rekisteröityä tai muokata tietojasi sivusta riippuen 

#### Pelilista

##### Kaikille

* Voit järjestää listaa eri tavoin klikkaamalla nuolia sarakkeiden otsikoiden vieressä

* Klikkaamalla *Listaa arvostelut* pelin tietojen vieressä, ohjaudut sivulle, josta näet listan kyseiseen peliin liityvistä arvosteluista

##### Kirjautuneena

* Klikkaamalla *Lisää peli*, ohjaudut pelin lisäys sivulle

* Klikkaamalla *Arvostele* pelin tietojen vieressä, ohjaudut arvostelun teko sivulle

* Klikkaamalla *Merkitse virheelliseksi*, merkitset pelin niin, että admin tietää, että sen tiedoissa on jotain vialla

##### Adminina

* Klikkaamalla *Kaikki pelit*, listataan kaikki pelit

* Klikkaamalla *Virheelliseksi merkityt*, listataan vain virheelliseksi merkityt pelit

* Klikkaamalla *Muokkaa* pelin tietojen vieressä, ohjaudut pelin tietojen muokkaus sivulle

* Klikkaamalla *Poista* pelin tietojen vieressä, poistat pelin ja kaikki siihen liittyvät arvostelut*

#### Pelin lisäys ja muokkaus sivut

* Voit kirjoittaa pelin nimen, tunnuksen ja julkaisupäivän lisätä pelin tai muokata sen tietoja sivusta riippuen

#### Arvostelun teko ja muokkaus sivu

* Voit kirjoittaa aiemmin valitsemallesi pelille arvosanan 0-5 ja arvostelun ja lisätä sen pelille tai muokata aiemmin tekemää arvostelua sivusta riippuen

#### Arvostelulista

##### Kaikille 

* Voit järjestää listaa eri tavoin klikkaamalla nuolia sarakkeiden otsikoiden vieressä

* Klikkaamalla pelin nimeä, ohjaudut sivulle, josta näet kyseiseen peliin liittyvät arvostelut

* Klikkaamalla käyttäjän nimeä, ohjaudut kyseisen käyttäjän profiilisivulle

##### Kirjautuneena

* Omien arvostluiden vieressä on napit *Mokkaa*, joka ohjaa arvotelun muokkaus sivulle, ja *Poista*, joka poistaa arvostelun

* Muiden arvosteluiden vieressä nappi *Merkitse asiattomaksi*, joka merkitsee arvostelun niin, että admin tietää, että siinä on jotain asiatonta

* Muiden arvosteluiden vieressä nappi *Tykkää* tai *Poista tykkäys*, joka lisää/poistaa tykkäykseni arvostelulle

##### Adminina

* Klikkaamalla *Kaikki arvostelut*, listataan kaikki arvostelut

* Klikkaamalla *Asiattomiksi merkityt*, listataan vain asiattomaksi merkityt arvostelut

* Arvosteluiden vieressä on napit *Merkitse asialliseksi*, joka poistaa merkinnän asiattomaksi, ja *Poista*, joka poistaa arvostelun

#### Peliin liittyvien arvosteluiden listaa

* Samoja toimintoja kuin arvostelulistassa

#### Käyttäjän profiili sivu

* Samoja toimintoja kuin arvostelulistassa

##### Käyttäjänä

* Omalla profiilisivulla omien tietojen alla on nappi *Muokkaa tietoja*, joka ohjaa tietojen muokkaussivulle
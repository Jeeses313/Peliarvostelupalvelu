## User storyt ja niiden SQL-kyselyt

SQL-kyselyt ovat ohjelman koodissa käytettyjen kyselyiden mukaisia, minkä takia nimet ovat englanniksi ja näin eroavat tietorakenteen kuvauksen esityksestä.

Käyttäjänä voin rekisteröityä.  
`INSERT INTO Account (name, password, admin) VALUES (?, ?, False)`

Käyttäjänä voin kirjautua sisään ja ulos.  
`SELECT * FROM Account WHERE name = ? AND password = ?`

Käyttäjänä voin vaihtaa nimeni ja salasanani.  
`UPDATE Account SET name = ?, password = ? WHERE VALUES id = ?`

Käyttäjänä voin poistaa tilini.  
`DELETE FROM Account WHERE id = ?`

Käyttäjänä voin nähdä profiilini ja muidenkin profiilit.  
`SELECT * FROM Account WHERE id = ?`

Käyttäjänä voin saada esille listan peleistä, jotka ovat tietokannassa.  
`SELECT * FROM Game`

Käyttäjänä voin lisätä pelin tietokantaan, jos sitä ei jo siellä ole.  
`SELECT * FROM Game WHERE name = ?`  
`INSERT INTO Game (name, tag, publication, flag) VALUES (?, ?, ?, False)`

Käyttäjänä voin saada listan peleistä järjestettynä nimen, tunnisteen, julkaisupäivän tai arvosteluiden määrän mukaan.  
```
SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average  
FROM Game LEFT JOIN Review ON Game.id = Review.game_id  
GROUP BY Game.id ORDER BY Game.name/Game.tag/Game.publication/review_average/review_count (DESC)
```

Käyttäjänä voin tehdä arvostelun pelille, jolle en ole jo tehnyt arvostelua.  
`INSERT INTO Review (user_id, game_id, grade, text, flag) VALUES (?, ?, ?, ?, False)`

Käyttäjänä voin muokata ja poistaa arvostelujani.  
```
UPDATE Review SET grade = ?, text = ? WHERE VALUES id = ?;  

DELETE FROM Review WHERE id = ?;  
```

Käyttäjänä voin nähdä omat ja muiden tekemät arvostelut järjestettynä eri tavoin.  
```
SELECT Review.id, Game.name, Account.username, Review.grade, Review.text,  
COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN ? THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id  
FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id  
LEFT JOIN Liking ON Review.id = Liking.review_id  
GROUP BY Review.id ORDER BY Game.name/Review.grade/like_count/Account.username (DESC)
```

Käyttäjänä voin tykätä arvostelusta.  
`INSERT INTO Liking (user_id, review_id) VALUES (?, ?)`

Käyttäjänä voin poistaa tykkäykseni arvostelusta.  
`DELETE FROM Liking WHERE user_id = ? AND review_id = ?`

Käyttäjänä voin nähdä peliin liittyvät arvostelut järjestettynä eri tavoin.  
```
SELECT Review.id, Game.name, Account.username, Review.grade, Review.text,  
COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN ? THEN 1 ELSE 0 END) AS is_liked, Account.id  
FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id  
LEFT JOIN Liking ON Review.id = Liking.review_id  
WHERE Game.id = ? GROUP BY Review.id ORDER BY Game.name/Review.grade/like_count/Account.username (DESC)
```

Käyttäjänä voin merkitä asiattoman sisällön ja pelit, joiden tiedot ovat virheellisiä.  
`UPDATE Game SET flag = True WHERE VALUES name = ?`  
`UPDATE Review SET flag = True WHERE VALUES user_id = ? AND game_id = ?`

Adminina voin poistaa asiatonta sisältöä.  
`DELETE FROM Game WHERE id = ?`  
`DELETE FROM Review WHERE id = ?`

Adminina voin poistaa muiden käyttäjien tilejä.  
`DELETE FROM Account WHERE id = ?`

Adminina voin muuttaa pelien tietoja.  
`UPDATE Game SET name = ?, tag = ?, publication = ?, flag = False WHERE VALUES name = ?`

Adminina voin saada listan peleistä ja arvosteluista, jotka on merkitty virheellisiksi tai asiattomiksi.  
```
SELECT Game.id, Game.name, Game.tag, Game.publication, COUNT(Review.id) AS review_count, AVG(Review.grade) AS review_average, Game.flag  
FROM Game LEFT JOIN Review ON Game.id = Review.game_id  
WHERE Game.flag = True GROUP BY Game.id ORDER BY Game.name;  

SELECT Review.id, Game.name, Account.username, Review.grade, Review.text,  
COUNT(Liking.id) AS like_count, SUM(CASE Liking.user_id WHEN :user_id THEN 1 ELSE 0 END) AS is_liked, Account.id, Game.id  
FROM Review LEFT JOIN Game ON Review.game_id = Game.id LEFT JOIN Account ON Review.user_id = Account.id  
LEFT JOIN Liking ON Review.id = Liking.review_id  
WHERE Review.flag = True GROUP BY Review.id, Game.name, Account.username, Account.id, Game.id ORDER BY Game.name;
```  
## Tietokantarakenteen kuvaus

### Tietokantakaavio

![alt text](https://github.com/Jeeses313/Peliarvostelupalvelu/blob/master/documentation/Peliarvostelupalvelu%20tietokantakaavio.png "Tietokantakaavio")

### CREATE TABLE-lauseet

SQL-kyselyt ovat ohjelman koodissa käytettyjen kyselyiden mukaisia, minkä takia nimet ovat englanniksi ja näin eroavat tietokantakaaviosta.

Käyttäjä  
```
  CREATE TABLE Account (  
  id INTEGER PRIMARY KEY,  
  username VARCHAR(50),  
  password VARCHAR(50),  
  admin BOOLEAN  
)
```

Arvostelu  
```
CREATE TABLE Review (  
  id INTEGER PRIMARY KEY,  
  user_id INTEGER,  
  game_id INTEGER,  
  grade INTEGER,  
  text VARCHAR(300),  
  flag BOOLEAN,  
  FOREIGN KEY (user_id) REFERENCES Account(id),  
  FOREIGN KEY (game_id) REFERENCES Game(id)  
)
```

Peli  
```
CREATE TABLE Game (  
  id INTEGER PRIMARY KEY,  
  name VARCHAR(150),  
  tag VARCHAR(150),  
  publication DATE,  
  flag BOOLEAN  
)
```

Tykkäys  
```
CREATE TABLE Liking (  
  id INTEGER PRIMARY KEY,  
  user_id INTEGER,  
  review_id INTEGER,  
  FOREIGN KEY (user_id) REFERENCES Account(id),  
  FOREIGN KEY (review_id) REFERENCES Review(id)  
)
```

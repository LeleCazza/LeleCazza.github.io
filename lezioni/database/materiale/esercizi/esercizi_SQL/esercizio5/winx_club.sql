-- Creazione del database
CREATE DATABASE winx_club;
USE winx_club;

-- Tabella delle Fate
CREATE TABLE Fate (
    id_fata INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    potere VARCHAR(50) NOT NULL,
    forza INT NOT NULL DEFAULT 50,
    velocita INT NOT NULL DEFAULT 50,
    magia INT NOT NULL DEFAULT 50
);
-- Tabella delle Scuole di Magia
CREATE TABLE Scuole (
    id_scuola INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    luogo VARCHAR(50) NOT NULL
);

-- Tabella dei Nemici
CREATE TABLE Nemici (
    id_nemico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    livello_pericolo INT NOT NULL
);

-- Tabella delle Missioni
CREATE TABLE Missioni (
    id_missione INT AUTO_INCREMENT PRIMARY KEY,
    descrizione TEXT NOT NULL,
    id_fata INT,
    id_scuola INT,
    FOREIGN KEY (id_fata) REFERENCES Fate(id_fata) ON DELETE SET NULL,
    FOREIGN KEY (id_scuola) REFERENCES Scuole(id_scuola) ON DELETE SET NULL
);

-- Tabella di collegamento molti a molti tra Fate e Nemici
CREATE TABLE Fata_Nemico (
    id_fata INT,
    id_nemico INT,
    PRIMARY KEY (id_fata, id_nemico),
    FOREIGN KEY (id_fata) REFERENCES Fate(id_fata) ON DELETE CASCADE,
    FOREIGN KEY (id_nemico) REFERENCES Nemici(id_nemico) ON DELETE CASCADE
);

-- Inserimento dati nelle Fate
INSERT INTO Fate (nome, potere, forza, velocita, magia) VALUES ('Bloom', 'Fiamma del Drago', 75, 70, 90);
INSERT INTO Fate (nome, potere, forza, velocita, magia) VALUES ('Stella', 'Luce del Sole', 60, 80, 85);
INSERT INTO Fate (nome, potere, forza, velocita, magia) VALUES ('Flora', 'Natura', 55, 65, 95);
INSERT INTO Fate (nome, potere, forza, velocita, magia) VALUES ('Musa', 'Musica', 50, 75, 90);
INSERT INTO Fate (nome, potere, forza, velocita, magia) VALUES ('Tecna', 'Tecnologia', 60, 70, 80);
INSERT INTO Fate (nome, potere, forza, velocita, magia) VALUES ('Aisha', 'Fluidità', 65, 85, 75);
-- Inserimento dati nelle Scuole
INSERT INTO Scuole (nome, luogo) VALUES ('Alfea', 'Magix');
INSERT INTO Scuole (nome, luogo) VALUES ('Fonterossa', 'Regno delle Pixie');
INSERT INTO Scuole (nome, luogo) VALUES ('Torre Nebulosa', 'Regno delle Streghe');
INSERT INTO Scuole (nome, luogo) VALUES ('Andros', 'Regno Acquatico');
INSERT INTO Scuole (nome, luogo) VALUES ('Eraklyon', 'Regno Guerriero');
INSERT INTO Scuole (nome, luogo) VALUES ('Zentopia', 'Regno Perduto');

-- Inserimento dati nei Nemici
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Lord Darkar', 9);
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Le Trix', 8);
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Valtor', 10);
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Tritannus', 7);
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Acheron', 9);
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Selina', 6);
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Kalimdor', 5);
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Oblivion', 10);
INSERT INTO Nemici (nome, livello_pericolo) VALUES ('Lamia', 7);

-- Inserimento dati nelle Missioni
INSERT INTO Missioni (descrizione, id_fata, id_scuola) VALUES ('Recuperare il Cuore di Magix', 1, 1);
INSERT INTO Missioni (descrizione, id_fata, id_scuola) VALUES ('Difendere il regno delle Pixie', 2, 2);
INSERT INTO Missioni (descrizione, id_fata, id_scuola) VALUES ('Sconfiggere Valtor', 3, 1);
INSERT INTO Missioni (descrizione, id_fata, id_scuola) VALUES ('Recuperare la Spada di Cristallo', 6, 3);
INSERT INTO Missioni (descrizione, id_fata, id_scuola) VALUES ('Fermare il Caos di Acheron', 1, 4);
INSERT INTO Missioni (descrizione, id_fata, id_scuola) VALUES ('Proteggere il Regno di Eraklyon', 4, 5);
INSERT INTO Missioni (descrizione, id_fata, id_scuola) VALUES ('Esplorare Zentopia', 5, 6);

-- Associazioni tra Fate e Nemici
INSERT INTO Fata_Nemico (id_fata, id_nemico) VALUES
    ((SELECT id_fata FROM Fate WHERE nome = 'Bloom'), (SELECT id_nemico FROM Nemici WHERE nome = 'Lord Darkar')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Stella'), (SELECT id_nemico FROM Nemici WHERE nome = 'Le Trix')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Flora'), (SELECT id_nemico FROM Nemici WHERE nome = 'Valtor')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Musa'), (SELECT id_nemico FROM Nemici WHERE nome = 'Tritannus')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Tecna'), (SELECT id_nemico FROM Nemici WHERE nome = 'Acheron')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Aisha'), (SELECT id_nemico FROM Nemici WHERE nome = 'Selina')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Bloom'), (SELECT id_nemico FROM Nemici WHERE nome = 'Kalimdor')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Stella'), (SELECT id_nemico FROM Nemici WHERE nome = 'Oblivion')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Flora'), (SELECT id_nemico FROM Nemici WHERE nome = 'Lamia')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Musa'), (SELECT id_nemico FROM Nemici WHERE nome = 'Lord Darkar')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Tecna'), (SELECT id_nemico FROM Nemici WHERE nome = 'Le Trix')),
    ((SELECT id_fata FROM Fate WHERE nome = 'Aisha'), (SELECT id_nemico FROM Nemici WHERE nome = 'Valtor'));


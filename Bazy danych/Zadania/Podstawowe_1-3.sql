CREATE TABLE Trainings (
    id        INTEGER  PRIMARY KEY,
    name      TEXT     NOT NULL,
    price     INTEGER  NOT NULL,
    duration  TEXT     NOT NULL
);

CREATE TABLE TrainingsHistory (
    id           INTEGER  PRIMARY KEY,
    date         DATE     NOT NULL,
    training_id  INTEGER  NOT NULL,

  FOREIGN KEY (training_id) REFERENCES Trainings(id)
);

CREATE TABLE TrainingsMaterials (
    id           INTEGER  PRIMARY KEY,
    content      TEXT     NOT NULL,
    training_id  INTEGER  NOT NULL,

  FOREIGN KEY (training_id) REFERENCES Trainings(id)
);

CREATE TABLE Departments (
    city  VARCHAR(255)  PRIMARY KEY
);

CREATE TABLE Mentors (
    id               INTEGER       PRIMARY KEY,
    name             TEXT          NOT NULL,
    department_city  VARCHAR(255)  NOT NULL,

  FOREIGN KEY (department_city) REFERENCES Departments(city)
);

CREATE TABLE Customers (
    id              INTEGER  PRIMARY KEY,
    name            TEXT     NOT NULL,
    surname         TEXT     NOT NULL,
    gender          TEXT     NOT NULL,
    date_joined     DATE     NOT NULL,
    training_id     INTEGER  NOT NULL,
    mentor_id       INTEGER  NOT NULL,

  FOREIGN KEY (training_id) REFERENCES Trainings(id),
  FOREIGN KEY (mentor_id) REFERENCES Mentors(id)
);

CREATE TABLE Notes (
    id           INTEGER  PRIMARY KEY,
    content      TEXT     NOT NULL,
    mentor_id    INTEGER  NOT NULL,
    customer_id  INTEGER  NOT NULL,

  FOREIGN KEY (mentor_id) REFERENCES Mentors(id),
  FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

CREATE TABLE Invoices (
    id           INTEGER  PRIMARY KEY,
    customer_id  INTEGER  NOT NULL,

  FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

CREATE TABLE Payments (
    id           INTEGER  PRIMARY KEY,
    date         DATE     NOT NULL,
    amount       INTEGER  NOT NULL,
    customer_id  INTEGER  NOT NULL,

  FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

CREATE TABLE Payroll (
    id         INTEGER  PRIMARY KEY,
    amount     INTEGER  NOT NULL,
    mentor_id  INTEGER  NOT NULL,

  FOREIGN KEY (mentor_id) REFERENCES Mentors(id)
);



/* A) Wskaż tabele, który połączone są relacjami 1:n, m:n, 1:1
   Odnalazłem takie coś: */

SELECT
  TABLE_NAME,
  COLUMN_NAME,
  CONSTRAINT_NAME,
  REFERENCED_TABLE_NAME,
  REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE;

SELECT *
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS;


/* B) Każdą z tabel uzupełnij dowolnymi informacjami, zapewnij spójność między tabelami i ich relacjami
   Dane wygenerowane przez GPT */

-- Dane do tabeli Trainings
INSERT INTO Trainings (id, name, price, duration) VALUES
(1, 'Kurs Java', 1500, '30 godzin'),
(2, 'Kurs Python', 1200, '25 godzin'),
(3, 'Kurs SQL', 1000, '20 godzin'),
(4, 'Kurs Web Development', 1800, '40 godzin');

-- Dane do tabeli TrainingsHistory
INSERT INTO TrainingsHistory (id, date, training_id) VALUES
(1, '2021-01-10', 1),
(2, '2022-02-15', 2),
(3, '2023-03-20', 3),
(4, '2024-04-25', 4);

-- Dane do tabeli TrainingsMaterials
INSERT INTO TrainingsMaterials (id, content, training_id) VALUES
(1, 'Materiały do kursu Java', 1),
(2, 'Materiały do kursu Python', 2),
(3, 'Materiały do kursu SQL', 3),
(4, 'Materiały do kursu Web Development', 4);

-- Dane do tabeli Departments
INSERT INTO Departments (city) VALUES
('Warszawa'),
('Kraków'),
('Wrocław'),
('Gdańsk');

-- Dane do tabeli Mentors
INSERT INTO Mentors (id, name, department_city) VALUES
(1, 'Jan Kowalski', 'Warszawa'),
(2, 'Anna Nowak', 'Kraków'),
(3, 'Piotr Wiśniewski', 'Wrocław'),
(4, 'Magdalena Zielińska', 'Gdańsk');

-- Dane do tabeli Customers
INSERT INTO Customers (id, name, surname, gender, date_joined, training_id, mentor_id) VALUES
(1, 'Tomasz', 'Bąk', 'male', '2021-03-12', 4, 4),
(2, 'Ewa', 'Kowalczyk', 'female', '2021-01-18', 3, 3),
(3, 'Marek', 'Wojciechowski', 'male', '2023-06-22', 2, 2),
(4, 'Katarzyna', 'Kaczmarek', 'female', '2024-01-09', 1, 1);

-- Dane do tabeli Notes
INSERT INTO Notes (id, content, mentor_id, customer_id) VALUES
(1, 'Notatki do kursu Java', 1, 1),
(2, 'Notatki do kursu Python', 2, 2),
(3, 'Notatki do kursu SQL', 3, 3),
(4, 'Notatki do kursu Web Development', 4, 4);

-- Dane do tabeli Invoices
INSERT INTO Invoices (id, customer_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

-- Dane do tabeli Payments
INSERT INTO Payments (id, date, amount, customer_id) VALUES
(1, '2024-01-15', 1500, 1),
(2, '2024-02-20', 1200, 2),
(3, '2024-03-25', 1000, 3),
(4, '2024-04-30', 1800, 4),
(5, '2024-05-27', 1100, 3);

-- Dane do tabeli Payroll
INSERT INTO Payroll (id, amount, mentor_id) VALUES
(1, 3000, 1),
(2, 2500, 2),
(3, 2000, 3),
(4, 3500, 4);


/* C) Wyświetl tylko tych uczniów, którzy dołączyli do mentoringu w 2021 roku oraz oddzielnie tych uczniów,
   którzy dołączyli między czerwcem a grudniem ubiegłego roku
   (w celu pobrania aktualnego roku, wykorzystaj odpowiednią funkcję SQL). */

SELECT *
FROM Customers
WHERE EXTRACT(YEAR FROM date_joined) = 2021;

SELECT *
FROM Customers
WHERE (EXTRACT(MONTH FROM date_joined) BETWEEN 6 AND 12)
AND
EXTRACT(YEAR FROM date_joined) = EXTRACT(YEAR FROM NOW());


/* D) Wyświetl wszystkie informacje o uczniach płci żeńskiej posortowanych rosnąco według imienia
   > Dodałem osobną kolumnę do Customers z wyróżnieniem płci */

SELECT *
FROM Customers
WHERE gender = 'female'
ORDER BY name;


/* E) Wybierz dowolny rekord z tabeli Customers i wyświetl przydzielonego do niego mentora. */

/* 1. Wykorzystaj JOIN */
SELECT Customers.id AS customer_id, Mentors.id AS assigned_mentor_id
FROM Customers
RIGHT JOIN Mentors ON Customers.mentor_id=Mentors.id;


/* 2. Zaimplementuj tę samą funkcjonalność, nie wykorzystując JOINa */

SELECT id as customer_id, mentor_id as assigned_mentor_id
FROM Customers;


/* F. Wyświetl imię, nazwisko oraz staż nauki każdego ucznia. Wyświetlaj dodatkowo napis: “Klient specjalny”,
   jeśli staż ucznia jest większy równy niż 12 miesięcy, “Normalny klient”, jeśli jest krótszy niż 12 miesięcy.
   Wykorzystaj CASE. */

SELECT
  name,
  surname,
  TIMESTAMPDIFF(MONTH, date_joined, NOW()) AS seniority_months,
CASE
  WHEN
    TIMESTAMPDIFF(YEAR, date_joined, NOW()) >= 1
  THEN
    'Klient specjalny'
  ELSE
    'Normalny klient'
END AS customer_type
FROM Customers;


/* G. Wyświetl podsumowanie w formie tabeli składającej się z imienia, nazwiska oraz sumy wszystkich uiszczonych
   przez ucznia opłat pod kolumną “Całkowita zapłata”. */

SELECT name, surname, SUM(amount) as total_amount
FROM Customers
INNER JOIN Payments ON Payments.customer_id = Customers.id
GROUP BY name, surname;


/* H. Oblicz średnią arytmetyczną wszystkich uiszczonych wpłat z tabeli Payments dla wybranego ucznia */

SELECT AVG(amount)
FROM Payments
WHERE customer_id = 3;


/* I. Wykonaj SELECT dla 3 dowolnych tabel i wyświetl je jako jedną tabelę przy użyciu UNION. */

SELECT name
FROM Customers
UNION
SELECT name
FROM Mentors
UNION
SELECT name
FROM Trainings;


/* J. Stwórz zapytanie, które wyłuska tabelę zestawiającą każdego klienta ze średnią wartością wszystkich płatności klientów (użyj tabeli CTE) */

WITH customer_payments_arithmetical_average AS (
  SELECT name, AVG(amount) AS customer_average
  FROM Customers
  INNER JOIN Payments ON Payments.customer_id = Customers.id
  GROUP BY name, surname
),
customers_payments_arithmetical_average AS (
  SELECT AVG(amount) AS customers_average
  FROM Payments
)
SELECT name, customer_average, customers_average
FROM customer_payments_arithmetical_average,
     customers_payments_arithmetical_average;
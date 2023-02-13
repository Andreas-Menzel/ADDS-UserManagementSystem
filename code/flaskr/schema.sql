DROP TABLE IF EXISTS users;

CREATE TABLE users (
    email               TEXT    PRIMARY KEY,
    firstname           TEXT    NOT NULL,
    lastname            TEXT    NOT NULL,
    pwd_salt            TEXT    NOT NULL,
    pwd_hash            TEXT    NOT NULL,
    created             TEXT    NOT NULL,
    activated           TEXT
);

INSERT INTO users VALUES(
    "user@mail.com",
    "John",
    "Doe",
    "i_am_a_salt",
    "i_am_a_hash",
    "2023-02-13 08:00:00",
    "2023-02-13 08:01:00"
    );

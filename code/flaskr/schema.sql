DROP TABLE IF EXISTS users;

CREATE TABLE users (
    email               TEXT    PRIMARY KEY,
    firstname           TEXT    NOT NULL,
    lastname            TEXT    NOT NULL,
    pwd_salt            TEXT    NOT NULL,
    pwd_hash            TEXT    NOT NULL,
    created             TEXT    NOT NULL,
    activation_time     TEXT,
    activation_code     TEXT
);

INSERT INTO users(email, firstname, lastname, pwd_salt, pwd_hash, created, activation_code) VALUES(
    "user@mail.com",
    "John",
    "Doe",
    "i_am_a_salt",
    "i_am_a_hash",
    "2023-02-13 08:00:00",
    "testcode"
    );

-- this script create new table
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT CHECK (id == 1),
    name VARCHAR(256)
);
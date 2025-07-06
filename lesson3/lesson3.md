## test SQL

```SQL
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_constraint,
   column2 datatype(length) column_constraint,
   ...
   table_constraints
);
```
## create student table
```student SQL
CREATE TABLE IF NOT EXISTS student(
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) UNIQUE
);
```

## KILL
```
DROP TABLE student;
```
## ADD
```
INSERT INTO student (name, major)
VALUES ('育君', '歷史'), ('信忠','英語'),('小柱','數學')
;

```
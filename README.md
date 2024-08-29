# Задание
### Необходимо создать 2 контейнера: в первом разворачивается PostgreSQL, а во втором  — Python.
#### Вот что необходимо сделать:
#### 1. Развернуть базу данных PostgreSQL ваша_фамилия и создать таблицу test_table. 
#### Таблица должна создаваться автоматически при развертывании docker compose 
#### из файла init.sql (этот файл тоже необходимо создать).
#### 2.Таблица должна содержать 4 столбца: name, surname, city, age. name — от 4 до 10
#### символов, surname — без разницы, city — без разницы, age — только
#### положительные числа, до 150. Количество строк — не менее 20. init.sql должен 
#### содержать ключевые слова CREATE и INSERT.
В файле init.sql хранится:
CREATE TABLE test_table (
    NAME  VARCHAR(40),
    SURNAME VARCHAR(40),
    CITY VARCHAR(30),
    AGE INTEGER
);

INSERT INTO test_table (NAME,SURNAME,CITY,AGE) VALUES
('Igor','Vladimir','Perm',61),
('Vladimir','Vladimir','Perm',41),
('Ivan','Vladimir','Perm',20),
('Dasha','Semenovna','Samara',32),
('Ganimed','Ganimed','Samara',21),
('Donald','Tramp','New York',89),
('Aleksey','Vladimir','Perm',57),
('Dmitriy','Ivanovich','Moskva',50),
('Lidiya','Vladimir','Samara',36),
('Eduard','Yorick','Perm',24),
('IgorKhorev','Vladimir','Perm',61),
('VladimirIvan','Vladimir','Perm',41),
('Yan','Gillan','London',19),
('Dashka','Semenovna','Samara',34),
('Ganimedus','Ganimeds','Samara',22),
('Donalds','Trampus','New York',18),
('Alekseyka','Vladimirov','Perm',53),
('Dmitriyev','Ivanovichy','Moskva',29),
('Lidiyas','Vladimirov','Samara',31),
('Eduards','Yoricks','Perm',38);
#### 3. Выполнить запрос к таблице на Python (используйте psycopg2), который покажет   
#### максимальный и минимальный возраст для имен, длина которых меньше 6 символов
## 

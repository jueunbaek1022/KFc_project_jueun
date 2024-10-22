-- database 생성
CREATE DATABASE price_predict_db;

-- 사용할 database 지정
USE price_predict_db;

-- cabbage table 생성
CREATE TABLE cabbage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(255),
    data INT
);

-- utf 관련 오류 방지 
SET NAMES 'utf8mb4';

-- cabbage 데이터 불러오기(.csv)
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/1_cabbage_last.csv'
INTO TABLE cabbage
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS (date, data);

-- table 생성 확인
SHOW TABLES;

-- dried_pepper table 생성
CREATE TABLE dried_pepper (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(255),
    data INT
);

-- dried_pepper 데이터 불러오기(.csv)
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/2_dried_pepper_last.csv'
INTO TABLE dried_pepper
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS (date, data);

-- garlic table 생성
CREATE TABLE garlic (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(255),
    data INT
);

-- garlic 데이터 불러오기(.csv)
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/3_garlic_last.csv'
INTO TABLE garlic
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS (date, data);

-- ginger table 생성
CREATE TABLE ginger (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(255),
    data INT
);

-- ginger 데이터 불러오기(.csv)
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/4_ginger_last.csv'
INTO TABLE ginger
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS (date, data);

-- red_pepper table 생성
CREATE TABLE red_pepper (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(255),
    data INT
);

-- red_pepper 데이터 불러오기(.csv)
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/5_red_pepper_last.csv'
INTO TABLE red_pepper
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS (date, data);

-- green_onions table 생성
CREATE TABLE green_onions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(255),
    data INT
);

-- green_onions 데이터 불러오기(.csv)
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/6_green_onions_last.csv'
INTO TABLE green_onions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS (date, data);


-- 상위 table 생성: item table
CREATE TABLE item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL
);

-- item table에 데이터 넣기
INSERT INTO item (item_name) VALUES
('Cabbage'),
('Dried Pepper'),
('Garlic'),
('Ginger'),
('Green Onions'),
('Red Pepper');

-- 외래키생성
ALTER TABLE cabbage
ADD CONSTRAINT fk_cabbage_item
FOREIGN KEY (item_id) REFERENCES item(id);

ALTER TABLE dried_pepper
ADD COLUMN item_id INT,
ADD CONSTRAINT fk_dried_pepper_item
FOREIGN KEY (item_id) REFERENCES item(id);

ALTER TABLE garlic
ADD COLUMN item_id INT,
ADD CONSTRAINT fk_garlic_item
FOREIGN KEY (item_id) REFERENCES item(id);

ALTER TABLE ginger
ADD COLUMN item_id INT,
ADD CONSTRAINT fk_ginger_item
FOREIGN KEY (item_id) REFERENCES item(id);

ALTER TABLE green_onions
ADD COLUMN item_id INT,
ADD CONSTRAINT fk_green_onions_item
FOREIGN KEY (item_id) REFERENCES item(id);

ALTER TABLE red_pepper
ADD COLUMN item_id INT,
ADD CONSTRAINT fk_red_pepper_item
FOREIGN KEY (item_id) REFERENCES item(id);


-- 개발자 계정 생성
-- CREATE USER '개발자'@'%' IDENTIFIED BY 'your_password';
CREATE USER 'futures'@'%' IDENTIFIED BY '1234';

-- db에 권한을 부여하기
GRANT ALL PRIVILEGES ON price_predict_db.* TO 'futures'@'%';

-- 추가된 코드 전체 실행
FLUSH PRIVILEGES;
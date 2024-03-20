-- task 0 -- 
sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57
-- task 1 -- 
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
--- task 2 ---
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250)
);

INSERT INTO nexus6 (name) VALUES(
    ('mahmoud')
);
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
-- task 3 -- 
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION SLAVE  ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
GRANT REPLICATION CLIENT ON *.* TO 'replica_user'@'%';

FLUSH PRIVILEGES;
--- task 4
STOP SLAVE;

CHANGE MASTER TO MASTER_HOST='54.157.170.194', MASTER_USER='replica_user', MASTER_PASSWORD='projectcorrection280hbtn', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=101;

START SLAVE;

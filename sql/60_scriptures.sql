CREATE DATABASE bible;
USE bible;

CREATE TABLE `60_scriptures` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `place` varchar(64) NOT NULL,
    `text` varchar(256) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

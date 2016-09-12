CREATE DATABASE IF NOT EXISTS `friendships` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `friendships`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
	`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `first_name` varchar(45) NOT NULL,
	`last_name` varchar(45) NOT NULL,
    `created_at` datetime NOT NULL DEFAULT NOW(),
    `updated_at` datetime NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `friendships`;
CREATE TABLE `friendships` (
	`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `user_id` smallint(5) unsigned NOT NULL,
    `friend_id` smallint(5) unsigned NOT NULL,
    `created_at` datetime NOT NULL DEFAULT NOW(),
    `updated_at` datetime NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`)
);

INSERT INTO `users` VALUES (1, 'Chris', 'Baker', NOW(), NOW()),(2, 'Diana', 'Smith', NOW(), NOW()),(3, 'James', 'Johnson', NOW(), NOW()),(4, 'Jessica', 'Davidson', NOW(), NOW());
INSERT INTO `friendships` VALUES (1, 1, 4, NOW(), NOW()),(2, 1, 3, NOW(), NOW()),(3, 1, 2, NOW(), NOW()),(4, 2, 1, NOW(), NOW()),(5, 3, 1, NOW(), NOW()),(6, 4, 1, NOW(), NOW());
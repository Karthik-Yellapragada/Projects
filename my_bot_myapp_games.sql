-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: my_bot
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `myapp_games`
--

DROP TABLE IF EXISTS `myapp_games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_games` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `desc` longtext NOT NULL,
  `link` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_games`
--

LOCK TABLES `myapp_games` WRITE;
/*!40000 ALTER TABLE `myapp_games` DISABLE KEYS */;
INSERT INTO `myapp_games` VALUES (1,'2048','images/2048_TIm6bM6.png','Join the numbers and get to the 2048 tile!','twenty'),(2,'Subway Surfers','images/sub_mOZSBJ8.jpg','Exploring the city, one subway ride at a time.','play_evowars/'),(3,'Hill Climb Racing','images/hill_B6Nm4EU.jpg','Exploring the city, one subway ride at a time','hill/'),(4,'Moto X3M','images/moto_880iJ7z.png','Time trial bike racing game','bike/'),(5,'Templ Run','images/temple_h8MDrPt.jpg','Take the idol if u dare!','temple/'),(6,'Cut The Rope','images/cut_eqi67sH.jpg','Remaster your brain!','cut/'),(7,'Bubble Shooter','images/bubble_51UAyho.jpg','Pop colored collections of bubbles','bubble/');
/*!40000 ALTER TABLE `myapp_games` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-16 11:25:23

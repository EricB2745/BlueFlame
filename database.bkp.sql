-- MySQL dump 10.13  Distrib 5.5.53, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: BlueFlame
-- ------------------------------------------------------
-- Server version	5.5.53-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Activity`
--

DROP TABLE IF EXISTS `Activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_item_id` int(11) NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `event_datetime` datetime DEFAULT NULL,
  `user` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_Activity_Order_Item1_idx` (`order_item_id`),
  CONSTRAINT `fk_Activity_Order_Item1` FOREIGN KEY (`order_item_id`) REFERENCES `Order_Item` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Activity`
--

LOCK TABLES `Activity` WRITE;
/*!40000 ALTER TABLE `Activity` DISABLE KEYS */;
/*!40000 ALTER TABLE `Activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cart_Type`
--

DROP TABLE IF EXISTS `Cart_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cart_Type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(25) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cart_Type`
--

LOCK TABLES `Cart_Type` WRITE;
/*!40000 ALTER TABLE `Cart_Type` DISABLE KEYS */;
INSERT INTO `Cart_Type` VALUES (1,'new','2 x 4 foot carts','Active');
/*!40000 ALTER TABLE `Cart_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Color`
--

DROP TABLE IF EXISTS `Color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Color` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(45) DEFAULT NULL,
  `description` varchar(255) NOT NULL,
  `hex_code` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `order_num_UNIQUE` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Color`
--

LOCK TABLES `Color` WRITE;
/*!40000 ALTER TABLE `Color` DISABLE KEYS */;
INSERT INTO `Color` VALUES (1,'Blue','Long Descriptions','12345','Active'),(2,'Red','Description of Red','54321','Active');
/*!40000 ALTER TABLE `Color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Color_Activity`
--

DROP TABLE IF EXISTS `Color_Activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Color_Activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `event_datetime` datetime DEFAULT NULL,
  `user` varchar(45) DEFAULT NULL,
  `Color_id` int(11) NOT NULL,
  `Order_Item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_Color_Activity_Color1_idx` (`Color_id`),
  KEY `fk_Color_Activity_Order_Item1_idx` (`Order_Item_id`),
  CONSTRAINT `fk_Color_Activity_Color1` FOREIGN KEY (`Color_id`) REFERENCES `Color` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Color_Activity_Order_Item1` FOREIGN KEY (`Order_Item_id`) REFERENCES `Order_Item` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Color_Activity`
--

LOCK TABLES `Color_Activity` WRITE;
/*!40000 ALTER TABLE `Color_Activity` DISABLE KEYS */;
/*!40000 ALTER TABLE `Color_Activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Color_Time`
--

DROP TABLE IF EXISTS `Color_Time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Color_Time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Color_id` int(11) NOT NULL,
  `start_datetime` datetime DEFAULT NULL,
  `end_datetime` datetime DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_Color_Time_Color1_idx` (`Color_id`),
  CONSTRAINT `fk_Color_Time_Color1` FOREIGN KEY (`Color_id`) REFERENCES `Color` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Color_Time`
--

LOCK TABLES `Color_Time` WRITE;
/*!40000 ALTER TABLE `Color_Time` DISABLE KEYS */;
/*!40000 ALTER TABLE `Color_Time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `Customer_Type_id` int(11) NOT NULL,
  `priority` char(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_Customer_Customer_Type1_idx` (`Customer_Type_id`),
  CONSTRAINT `fk_Customer_Customer_Type1` FOREIGN KEY (`Customer_Type_id`) REFERENCES `Customer_Type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'MOVING PROS',2,'N'),(2,'ALAN HEIDEL ',2,'Y'),(12,'Eric Thomas',2,'Y');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_Type`
--

DROP TABLE IF EXISTS `Customer_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer_Type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_Type`
--

LOCK TABLES `Customer_Type` WRITE;
/*!40000 ALTER TABLE `Customer_Type` DISABLE KEYS */;
INSERT INTO `Customer_Type` VALUES (1,'Retail','Active'),(2,'Standard Fabricator','Active'),(3,'Special','Active');
/*!40000 ALTER TABLE `Customer_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Daily_Priority`
--

DROP TABLE IF EXISTS `Daily_Priority`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Daily_Priority` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `work_date` datetime DEFAULT NULL,
  `order_item_id` int(11) NOT NULL,
  `sort_order` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_Daily_Prioity_Order_Item1_idx` (`order_item_id`),
  CONSTRAINT `fk_Daily_Prioity_Order_Item1` FOREIGN KEY (`order_item_id`) REFERENCES `Order_Item` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Daily_Priority`
--

LOCK TABLES `Daily_Priority` WRITE;
/*!40000 ALTER TABLE `Daily_Priority` DISABLE KEYS */;
/*!40000 ALTER TABLE `Daily_Priority` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order`
--

DROP TABLE IF EXISTS `Order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_num` varchar(45) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `order_status_id` int(11) NOT NULL,
  `order_date` datetime DEFAULT NULL,
  `due_date` datetime DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `order_num_UNIQUE` (`order_num`),
  KEY `fk_Orders_Order_Status_idx` (`order_status_id`),
  KEY `fk_Order_Customer1_idx` (`customer_id`),
  CONSTRAINT `fk_Orders_Order_Status` FOREIGN KEY (`order_status_id`) REFERENCES `Order_Status` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Customer1` FOREIGN KEY (`customer_id`) REFERENCES `Customer` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order`
--

LOCK TABLES `Order` WRITE;
/*!40000 ALTER TABLE `Order` DISABLE KEYS */;
INSERT INTO `Order` VALUES (1,'1234',2,1,'2017-01-02 00:00:00','2017-01-02 00:00:00','2017-02-01 04:31:54',10.23),(2,'12345',1,2,'2017-02-05 09:35:49','2017-02-05 09:35:49','2017-02-05 09:35:49',123.45);
/*!40000 ALTER TABLE `Order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order_Item`
--

DROP TABLE IF EXISTS `Order_Item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Order_Item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `description` varchar(767) NOT NULL,
  `special_instructions` varchar(767) DEFAULT NULL,
  `color_id` int(11) NOT NULL,
  `order_item_status_id` int(11) NOT NULL,
  `cart_type_id` int(11) NOT NULL,
  `qty_of_carts` int(11) DEFAULT NULL,
  `oversize` char(1) NOT NULL,
  `priority` char(1) NOT NULL,
  `requires_mask_or_plug` char(1) NOT NULL,
  `requires_sandblasting` char(1) NOT NULL,
  `sandblasting_activity_id` int(11) NOT NULL,
  `prep_activity_id` int(11) NOT NULL,
  `mask_plug_activity_id` int(11) NOT NULL,
  `paint_activity_id` int(11) NOT NULL,
  `invoiced_activity_id` int(11) NOT NULL,
  `cust_notified_activity_id` int(11) NOT NULL,
  `price_per` float DEFAULT NULL,
  `create_date` datetime NOT NULL,
  `sub_total` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `order_num_UNIQUE` (`description`),
  KEY `fk_Order_Items_Orders1_idx` (`order_id`),
  KEY `fk_Order_Item_Color1_idx` (`color_id`),
  KEY `fk_Order_Item_Cart_Type1_idx` (`cart_type_id`),
  KEY `fk_Order_Item_Activity1_idx` (`mask_plug_activity_id`),
  KEY `fk_Order_Item_Activity2_idx` (`prep_activity_id`),
  KEY `fk_Order_Item_Activity3_idx` (`paint_activity_id`),
  KEY `fk_Order_Item_Activity4_idx` (`invoiced_activity_id`),
  KEY `fk_Order_Item_Activity5_idx` (`cust_notified_activity_id`),
  KEY `fk_Order_Item_Activity6_idx` (`sandblasting_activity_id`),
  KEY `fk_Order_Item_Status1_idx` (`order_item_status_id`),
  CONSTRAINT `fk_Order_Items_Orders1` FOREIGN KEY (`order_id`) REFERENCES `Order` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Activity1` FOREIGN KEY (`mask_plug_activity_id`) REFERENCES `Activity` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Activity2` FOREIGN KEY (`prep_activity_id`) REFERENCES `Activity` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Activity3` FOREIGN KEY (`paint_activity_id`) REFERENCES `Activity` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Activity4` FOREIGN KEY (`invoiced_activity_id`) REFERENCES `Activity` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Activity5` FOREIGN KEY (`cust_notified_activity_id`) REFERENCES `Activity` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Activity6` FOREIGN KEY (`sandblasting_activity_id`) REFERENCES `Activity` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Cart_Type1` FOREIGN KEY (`cart_type_id`) REFERENCES `Cart_Type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Color1` FOREIGN KEY (`color_id`) REFERENCES `Color` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Item_Status1` FOREIGN KEY (`order_item_status_id`) REFERENCES `Order_Item_Status` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order_Item`
--

LOCK TABLES `Order_Item` WRITE;
/*!40000 ALTER TABLE `Order_Item` DISABLE KEYS */;
/*!40000 ALTER TABLE `Order_Item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order_Item_Status`
--

DROP TABLE IF EXISTS `Order_Item_Status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Order_Item_Status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `order_num_UNIQUE` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order_Item_Status`
--

LOCK TABLES `Order_Item_Status` WRITE;
/*!40000 ALTER TABLE `Order_Item_Status` DISABLE KEYS */;
INSERT INTO `Order_Item_Status` VALUES (1,'Not yet received','Active'),(2,'Waiting to be Sand Blasted','Active'),(3,'Waiting to be Prepped','Active'),(4,'Waiting to be Masked/Plugged','Active'),(5,'Waiting to be Painted','Active'),(6,'Complete','Active');
/*!40000 ALTER TABLE `Order_Item_Status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order_Status`
--

DROP TABLE IF EXISTS `Order_Status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Order_Status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `order_num_UNIQUE` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order_Status`
--

LOCK TABLES `Order_Status` WRITE;
/*!40000 ALTER TABLE `Order_Status` DISABLE KEYS */;
INSERT INTO `Order_Status` VALUES (1,'Open','Active'),(2,'Notified','Active'),(3,'Work Complete','Active'),(4,'Invoiced','Active');
/*!40000 ALTER TABLE `Order_Status` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-22 18:20:59

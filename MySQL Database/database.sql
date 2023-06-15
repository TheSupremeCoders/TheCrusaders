-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: sync_notion
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `scholar_number` int NOT NULL,
  `page_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`scholar_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (222105102,'77c6b4ca48b946959b7a20dffaef15c0'),(222120001,'4e397e3021ca461a9bab98adf9d5c955'),(222120006,'fbd6b035552140d2828fe834bfa7a875'),(222120007,'0f638d4565ff43b4b9d41b36181fdc71'),(222120008,'83e681b2f3824ab287e4253d7f0d6b10'),(222120009,'5996b8bc662e4cc2a65c24c7d6fae8d6'),(222120014,'056ff417fd8a4030ab6a72153ec20722'),(222120021,'0d5037bb04224bbb82e973a0567178db'),(222120022,'3009ef4edd4a44aab2b8e22afa9e864d'),(222120023,'4972de04430f48a8aece8df305024213'),(222120025,'5e9f3ec19a91450f88d5c884722ecc26'),(222120029,'e301ac3c723140e392887f13c8336298'),(222120031,'89c8a5fcf02b4c5f87a649de08176359'),(222120033,'603cca5be7de45e99c4207e59e17539b'),(222120034,'491794e0325448e2b5b102b98bcc1d9f'),(222120036,'76325808350b42868178d41fd5cdce50'),(222120038,'df0a86352af942a7bdf9ee33c6c6a8a4'),(222120040,'16a891497bfa4728a1e7a894ccf06515'),(222120041,'59ad026ef7704eefa947c7fd82482447'),(222120042,'b893ce1a91864a6ab6fff2569d6b2b53'),(222120047,'7ba22de89fe74ba0aa207c701c24410d'),(222120051,'9846fa1cbb2148638fb4e6b95957e012'),(222120056,'e851fa5a35fa424a8cf2835fbfbbdd60'),(222120101,'7e2bd5b759a846518dd49a15bfdad7f9'),(222120104,'82a2bf2c3e5c4713ba0866737f2ad95e'),(222120105,'80a8db5119ce49f0af7806975e643ac3'),(222120108,'853598b7224541f787030f655aeb1a80'),(222120112,'7d8b9f071e524fdab4c82bd143d36390'),(222120113,'04e4db022eec44e28ca469b273733186'),(222120115,'1ed89e34ce2b4bd5a468b08977e63cae'),(222120121,'fc53c3c4c8764a1aadce8aa0ba001a99'),(222120122,'2448d7c5a8eb4c0ea185844f1dfa980e'),(222120123,'dc6ad61c29824f56a31716141c9c6479'),(222120127,'283e36767374477cba4105ac0f43bb32'),(222120131,'c27b6788d688436c9555a29a881ee73f'),(222120139,'2ccdd1c4e99d47aaa9a9e4f59fd20099'),(222120141,'21b2f460a3854300b2e694bac861c325'),(222120145,'5999ff4f006b40f4bd9e49b3277785ac'),(222120150,'646f14762bb8438dbad03e81d6a93ef3'),(222130105,'d1a03e58513740eea50f763f0617b1fe');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problems`
--

DROP TABLE IF EXISTS `problems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `problems` (
  `name` varchar(255) NOT NULL,
  `page_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problems`
--

LOCK TABLES `problems` WRITE;
/*!40000 ALTER TABLE `problems` DISABLE KEYS */;
INSERT INTO `problems` VALUES ('3Sum','dee05cb0-da71-4fd5-afc1-bbaa1e7778b1'),('A - Game with Board','aac8d6cd-c3db-4f2f-be4c-8869a077b4f8'),('A - Multiplication Table','e96f22e7-d4d4-41d1-b1ce-617b2c8a4cd4'),('ACCURACY','15d96be0-7f3f-4d98-bfc9-0566e0c5dde9'),('Arithmetic Subarrays','b08a7306-7b7c-416b-a1dd-616ccb4efab0'),('AVGPERM','918c84bd-7e5d-461e-86ac-c50c54817344'),('B - Binary Cafe','d5d814c7-8249-4309-87c2-c3d73e8caf7d'),('B - Phoenix and Puzzle','9826567c-90b2-4387-98ba-8c46ded2dd76'),('B - Pipeline','4db8675b-b95f-47c5-8f0f-e29b7ea795fa'),('B - Two-gram','89f5b46f-35d4-4044-aae0-3c465f4fe34f'),('Best Time to Buy and Sell Stock','80c883a6-5bcc-4e0c-b520-973ad4f04df9'),('BIRDFARM','61ec2161-7727-4b18-98d4-b07c66c7dc06'),('Check If Two String Arrays are Equivalent','79d2bad2-7607-4881-969e-a08c8164c047'),('Climbing Stairs','c56733c7-d8ca-47e6-8772-80f21efef578'),('CNTWRD','8eda8fd2-b6b1-423b-ad38-53eb2d7e005e'),('Count Items Matching a Rule','c96fcc01-6b1d-468f-a991-9a2dae719f6e'),('CS2023_GIFT','36734c03-5b44-455b-a14d-78eafacba558'),('CS2023_GYM','096b1db7-7d83-4059-8e09-8cd40d2c49fb'),('CS2023_PON','88208453-98cf-4809-925b-189e81cdc493'),('CS2023_STK','200c88b1-3e28-4606-982a-a96a360a00d4'),('D1 - Magic Powder - 1','0a96e929-e950-42e2-906d-5746147de22e'),('Decrypt String from Alphabet to Integer Mapping','bea27827-5f94-4047-ad30-88f9ecf45276'),('Delete Greatest Value in Each Row','dac62e70-705a-46af-a69d-e863c904f92d'),('Determine if String Halves Are Alike','0dad22bd-ca98-4b1b-af70-aeb9c0d6ab9e'),('DISTANCECOLO','c7aa7f30-5fd0-4bc7-adbd-4c95b170792a'),('Equal Row and Column Pairs','cd9eea96-e2bb-4b1e-a85f-482a0082da0d'),('EVALMAS','34d85758-fa1b-48fd-a54f-ef37b7d56482'),('Find All Numbers Disappeared in an Array','b761ce9b-c06a-4728-8585-ca440080833a'),('Find Peak Element','4ee912ea-18fc-49cd-a646-d650373557d5'),('Find Smallest Letter Greater Than Target','2ef82669-4d7d-46c9-92d8-3fdfa006bba9'),('Find the Student that Will Replace the Chalk','2997803f-dc37-476c-8e59-22dcafea0197'),('FLIPCARDS','a26734ca-b0ee-4608-8e57-a78ebfb4850b'),('Four Divisors','d331c997-b9c6-4c5a-a36a-bf984e01e621'),('FOURTICKETS','9bd695f5-f305-475e-b378-570c6ca480f2'),('Gray Code','8bb3d65c-224e-4234-bc31-bb4e7a133352'),('Happy Number','660bc96c-6f12-4caf-bfb8-96cdda53d430'),('Intersection of Two Arrays II','84bb099b-7acc-41a0-84a2-4c94ff6efa30'),('Is Subsequence','57058f6f-fc68-485e-b7b5-a119fbd24a11'),('JENGA','bfb018cf-9f84-4963-a43e-93392241a867'),('Keyboard Row','d82044ad-ab3a-473e-b184-abad208df355'),('Kth Largest Element in a Stream','dfd5233c-082a-42d3-b662-f4cc52f0dffa'),('LEARNSQL','aca24963-ec50-4dd4-bf74-e66950dc3c77'),('LUCKYSTR','cb32ac2e-80b5-48c8-8b77-46a71f0a9bde'),('Majority Element','78c27f78-d910-4160-a744-efed4769af8c'),('Majority Element II','31e238d7-1b64-4132-af8f-93774c83eec8'),('Minimum Distance to the Target Element','232f77e7-bd07-420e-b23f-fe1ce41a8dfb'),('MOVIE2X','8516b114-f47b-4e73-a36f-23ee55a21209'),('MXEVNSUB','010c1e26-a017-475c-b681-297adfd92439'),('N-Repeated Element in Size 2N Array','c21855fd-6036-44a3-b8b2-f763bd75c173'),('NEWPIECE','72213097-5d3a-4e2a-8432-6fa9bb7518b7'),('Number of Strings That Appear as Substrings in Word','3be718f0-62f7-494f-a560-ab076100e3fd'),('PAR2','2f2f9ae9-05ac-42d2-bdc0-5ae727af45ef'),('Peak Index in a Mountain Array','be100565-b3a4-4c56-ba95-19caca4d0f42'),('Power of Three','e3972144-4a39-4b2b-8526-c0d06315c3b1'),('PRACTICEPERF','de064ec0-8f24-446f-80ff-abd95600a305'),('PRIZEPOOL','e5ca2f4f-9a23-42b0-b7c3-090e6a25c673'),('RANKLISTPAGE','1954de96-0089-43ff-b0b1-14ee7c71e764'),('Rearrange Array Elements by Sign','f173e55e-a7d2-4274-8eb7-4e7fb3a3cf88'),('REMOSET','fa11f31c-439e-460c-b223-b6886cece25d'),('Remove Duplicates from Sorted Array II','9e90d6ac-2488-41f4-80d2-709311b72f6a'),('Replace All Digits with Characters','c5d2e99d-2cde-4d04-a655-cd941e03f44d'),('Replace Elements in an Array','d649fa03-b4ef-43c7-8339-ca24424e5c02'),('Reshape the Matrix','bb9a0bee-aed5-4f84-875a-f037d50caced'),('Reverse Prefix of Word','6f731ee6-a70a-4ecb-8116-2639ff7b3963'),('Reverse Words in a String III','001c98ad-82ea-4045-94f9-d68414fac85d'),('Rotate Image','701eed06-44e6-4386-a1a4-2524a55c0605'),('Search a 2D Matrix II','4a73ff63-54ec-4ef8-82b4-1b6b9088e8e6'),('Set Matrix Zeroes','dc902955-d09b-4c8f-97d2-57783c9bb6d9'),('SIXFRIENDS','86a98042-56fe-4a22-b8d7-c372977e7683'),('Sort an Array','13772c78-eaa7-4517-b365-b002712774a7'),('Sorting the Sentence','69b5eacf-23d8-47c8-84c6-5ef8aa1fa9d5'),('Sqrt(x)','cff069e1-54dd-4665-8a70-dbaf62e587c7'),('Subrectangle Queries','eaef8335-fec5-4b96-8675-163720ff5832'),('Summary Ranges','2210360a-9073-4f28-9821-f0ec8c433370'),('To Lower Case','0539d9b3-23cd-4f35-a372-ab7718f3ef16'),('TODOLIST','25d8ff7d-91fb-4be3-8a1c-8e6a2ef6bb48'),('Top K Frequent Elements','158f668e-e3a9-4d6b-84e8-a4ecda7d518c'),('Valid Palindrome','5c2c7e18-f67d-4334-a912-ac941b0024f0'),('VOWMTRX','899907a0-65bc-4071-8257-d7df76d74d4c');
/*!40000 ALTER TABLE `problems` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-15  7:09:22

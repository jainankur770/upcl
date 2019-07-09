-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 09, 2019 at 08:51 AM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `upcl`
--

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `Chat_id` int(3) NOT NULL,
  `Data` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`Chat_id`, `Data`) VALUES
(1, 'Please enter your customer id number(1 to 15)'),
(2, 'Have you received your electricity consumption bill'),
(3, 'If you have not received the electricity consumption bill, you can avail a copy of bill from the concerned Sub Division Office. You may also download the duplicate bill from the UPCL\'s website. You can also deposit payment within the due date specified in the bill at the Electricity Business/Billing Centre.'),
(4, 'You can deposit payment within the due date specified in the bill at the Electricity Business/Billing Centre.'),
(5, 'The consumption depends on the capacity of appliance and period for which it is in use.'),
(6, 'Please see the Electricity Tariff details provided on the home page of UPCL’s Website.'),
(7, 'If meter is not read for whatever reason, provisional bill is raised which subjected to adjustment on receipt of actual meter reading in the subsequent months. Provisional bills are required to be paid within the due dates like normal bills raised on actual consumption.'),
(8, 'Thank you for using UPCL'),
(9, 'For increasing the sanctioned load the consumers should apply to the concerned Sub-divisional Officer. The HT consumers should apply to the Executive Engineer and after confirming the feasibility, the load is sanctioned.'),
(10, 'Submit application to the concerned Sub Divisional Officer on plain paper enclosing therewith a copy of last paid bill. Be present on scheduled date/time when inspection will be carried out by UPCL. Make payment against the bill to be handed over to you by UPCL at the earliest.'),
(11, 'Please select your query from the below mentioned options'),
(12, 'Welcome to UPCL'),
(13, 'Please elaborate your concern'),
(14, 'After installation, the billing section is supplied with data containing Meter details, initial meter reading. As per the predetermined cyclic order the first bill is issued. The bills are issued monthly, bimonthly for different categories of consumers . Domestic, Non-Domestic, Industrial consumers. The payment of bills is to be made as per the last due date shown on the bill.'),
(15, 'Please enter your registered mobile number'),
(16, 'Please select your preferred time from below options'),
(17, 'Our executive will reach out to you on your preferred time');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

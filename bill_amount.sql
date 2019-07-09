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
-- Table structure for table `bill_amount`
--

CREATE TABLE `bill_amount` (
  `Customer_id` int(4) NOT NULL,
  `Unit_Consumed` int(4) NOT NULL,
  `Rates` float NOT NULL,
  `Amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill_amount`
--

INSERT INTO `bill_amount` (`Customer_id`, `Unit_Consumed`, `Rates`, `Amount`) VALUES
(1, 300, 4.5, 1140),
(2, 100, 3.3, 330),
(3, 225, 4.5, 802.5),
(4, 67, 2.5, 212.5),
(5, 127, 3.3, 409.1),
(6, 55, 2.5, 182.5),
(7, 125, 3.3, 402.5),
(8, 78, 2.5, 240),
(9, 325, 4.5, 1252.5),
(10, 350, 4.5, 1365),
(11, 299, 4.5, 1140.5),
(12, 241, 4.5, 874.5),
(13, 400, 4.5, 1590),
(14, 78, 2.5, 240),
(15, 150, 3.3, 485);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill_amount`
--
ALTER TABLE `bill_amount`
  ADD PRIMARY KEY (`Customer_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

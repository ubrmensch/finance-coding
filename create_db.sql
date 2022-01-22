DROP DATABASE IF EXISTS `financial_app`;
CREATE DATABASE `financial_app` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `financial_app`;

CREATE TABLE `stock_symbols` (
  `Symbol` char(6) NOT NULL,
  `Name` char(255) DEFAULT NULL,
  `Market_Cap` double DEFAULT NULL,
  `Country` char(25) DEFAULT NULL,
  `IPO_Year` char(10) DEFAULT NULL,
  `Volume` double DEFAULT NULL,
  `Sector` char(100) DEFAULT NULL,
  `Industry` char(100) DEFAULT NULL,
  `Last_Refresh` datetime DEFAULT NULL,
  PRIMARY KEY (`Symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `stock_history` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Symbol` char(6) DEFAULT NULL,
  `Name` char(100) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `High` float DEFAULT NULL,
  `Low` float DEFAULT NULL,
  `Close` float DEFAULT NULL,
  `Volume` bigint(20) DEFAULT NULL,
  `Dividends` float DEFAULT NULL,
  `Stock Splits` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

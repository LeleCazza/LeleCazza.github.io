-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versione server:              5.1.72-community - MySQL Community Server (GPL)
-- S.O. server:                  Win32
-- HeidiSQL Versione:            10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dump della struttura del database teatribase
CREATE DATABASE IF NOT EXISTS `teatribase` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `teatribase`;

-- Dump della struttura di tabella teatribase.citta
CREATE TABLE IF NOT EXISTS `citta` (
  `cap` varchar(5) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `comune` varchar(30) NOT NULL,
  PRIMARY KEY (`cap`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella teatribase.proietta
CREATE TABLE IF NOT EXISTS `proietta` (
  `idT` int(11) NOT NULL,
  `idS` int(11) NOT NULL,
  `data` date NOT NULL,
  `sala` int(10) unsigned NOT NULL,
  PRIMARY KEY (`idT`,`idS`),
  KEY `FK_proietta_spettacolo` (`idS`),
  CONSTRAINT `FK_proietta_teatro` FOREIGN KEY (`idT`) REFERENCES `teatro` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_proietta_spettacolo` FOREIGN KEY (`idS`) REFERENCES `spettacolo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella teatribase.spettacolo
CREATE TABLE IF NOT EXISTS `spettacolo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(16) NOT NULL,
  `prezzo` float NOT NULL,
  `nome` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella teatribase.teatro
CREATE TABLE IF NOT EXISTS `teatro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `capienza` int(10) unsigned NOT NULL,
  `n_sale` int(10) unsigned NOT NULL,
  `nome` varchar(30) NOT NULL,
  `indirizzo` varchar(50) NOT NULL,
  `capC` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_teatro_citta` (`capC`),
  CONSTRAINT `FK_teatro_citta` FOREIGN KEY (`capC`) REFERENCES `citta` (`cap`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- L’esportazione dei dati non era selezionata.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

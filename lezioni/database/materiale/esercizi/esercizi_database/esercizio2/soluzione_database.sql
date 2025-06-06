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


-- Dump della struttura del database squidbase
CREATE DATABASE IF NOT EXISTS `squidbase` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `squidbase`;

-- Dump della struttura di tabella squidbase.affronta
CREATE TABLE IF NOT EXISTS `affronta` (
  `idL` int(11) NOT NULL,
  `numeroP` int(11) unsigned NOT NULL,
  `superato` int(11) NOT NULL,
  PRIMARY KEY (`idL`),
  KEY `FK_affronta_personaggio` (`numeroP`),
  CONSTRAINT `FK_affronta_livello` FOREIGN KEY (`idL`) REFERENCES `livello` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_affronta_personaggio` FOREIGN KEY (`numeroP`) REFERENCES `personaggio` (`numero`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella squidbase.livello
CREATE TABLE IF NOT EXISTS `livello` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `difficolta` varchar(10) NOT NULL,
  `tema` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella squidbase.personaggio
CREATE TABLE IF NOT EXISTS `personaggio` (
  `numero` int(10) unsigned NOT NULL,
  `nome` varchar(20) NOT NULL,
  `nazionalita` varchar(2) NOT NULL,
  `nomeQ` varchar(20) NOT NULL,
  PRIMARY KEY (`numero`),
  KEY `FK_personaggio_quartiere` (`nomeQ`),
  CONSTRAINT `FK_personaggio_quartiere` FOREIGN KEY (`nomeQ`) REFERENCES `quartiere` (`nome`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella squidbase.quartiere
CREATE TABLE IF NOT EXISTS `quartiere` (
  `nome` varchar(20) NOT NULL,
  `numero_abitanti` int(10) unsigned NOT NULL,
  `dimensione` int(10) unsigned NOT NULL,
  PRIMARY KEY (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- L’esportazione dei dati non era selezionata.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

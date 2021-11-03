SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema foundbypets
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `foundbypets2` DEFAULT CHARACTER SET utf8 ;
USE `foundbypets` ;

-- -----------------------------------------------------
-- Table `foundbypets`.`M_encontrada`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foundbypets2`.`M_encontrada` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(20) NOT NULL,
  `Correo` VARCHAR (1000) NOT NULL,
  `Region` VARCHAR(20) NOT NULL,
  `Comuna` VARCHAR(20) NULL,
  `Celular` VARCHAR(20) NULL,
  `foto_id` VARCHAR (1000) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Table `foundbypets`.`M_perdidas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foundbypets2`.`M_perdidas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(20) NOT NULL,
  `Correo` VARCHAR (1000) NOT NULL,
  `Region` VARCHAR(20) NOT NULL,
  `Comuna` VARCHAR(20) NULL,
  `Celular` VARCHAR(20) NULL,
  `foto_id` VARCHAR (1000) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Table `ejercicio4`.`archivos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foundbypets2`.`archivos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `path` VARCHAR(500) NOT NULL,
  `filename` VARCHAR (500) NOT NULL,
  `peso` int(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
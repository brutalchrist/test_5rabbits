SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `colegio` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `colegio` ;

-- -----------------------------------------------------
-- Table `colegio`.`COLEGIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`COLEGIO` (
  `X_COLE` INT NOT NULL AUTO_INCREMENT,
  `T_RUT` VARCHAR(10) NOT NULL,
  `T_NOMBRE` VARCHAR(255) NOT NULL,
  `T_DIRECCION` VARCHAR(255) NULL,
  PRIMARY KEY (`X_COLE`),
  UNIQUE INDEX `X_COLE_UNIQUE` (`X_COLE` ASC),
  UNIQUE INDEX `T_RUT_UNIQUE` (`T_RUT` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`PERSONA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`PERSONA` (
  `X_PERS` INT NOT NULL AUTO_INCREMENT,
  `C_RUN` VARCHAR(10) NOT NULL,
  `T_NOMBRE` VARCHAR(150) NOT NULL,
  `T_APELLIDO1` VARCHAR(150) NOT NULL,
  `T_APELLIDO2` VARCHAR(150) NULL,
  `T_CORREO_ELECTRONICO` VARCHAR(255) NULL,
  `F_NACIMIENTO` DATE NULL,
  `L_ACTIVO` VARCHAR(1) NOT NULL DEFAULT 'S',
  PRIMARY KEY (`X_PERS`),
  UNIQUE INDEX `T_RUN_UNIQUE` (`C_RUN` ASC),
  UNIQUE INDEX `X_PERS_UNIQUE` (`X_PERS` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`PROFESOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`PROFESOR` (
  `X_PERS` INT NOT NULL,
  `T_TITULO` VARCHAR(150) NULL,
  `N_SUELDO` INT NULL,
  PRIMARY KEY (`X_PERS`),
  INDEX `fk_PROFESOR_PERSONA1_idx` (`X_PERS` ASC),
  CONSTRAINT `fk_PROFESOR_PERSONA1`
    FOREIGN KEY (`X_PERS`)
    REFERENCES `colegio`.`PERSONA` (`X_PERS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`CURSO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`CURSO` (
  `X_CURS` INT NOT NULL AUTO_INCREMENT,
  `COLE_X_COLE` INT NOT NULL,
  `PERS_X_PERS` INT NOT NULL,
  `T_NOMBRE` VARCHAR(150) NOT NULL,
  `T_DESCRIPCION` VARCHAR(255) NULL,
  `L_ACTIVO` VARCHAR(1) NOT NULL DEFAULT 'S',
  PRIMARY KEY (`X_CURS`),
  INDEX `fk_CURSO_COLEGIO_idx` (`COLE_X_COLE` ASC),
  UNIQUE INDEX `X_CURS_UNIQUE` (`X_CURS` ASC),
  INDEX `fk_CURSO_PROFESOR1_idx` (`PERS_X_PERS` ASC),
  CONSTRAINT `fk_CURSO_COLEGIO`
    FOREIGN KEY (`COLE_X_COLE`)
    REFERENCES `colegio`.`COLEGIO` (`X_COLE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CURSO_PROFESOR1`
    FOREIGN KEY (`PERS_X_PERS`)
    REFERENCES `colegio`.`PROFESOR` (`X_PERS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`ALUMNO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`ALUMNO` (
  `X_PERS` INT NOT NULL,
  `L_BECADO` VARCHAR(1) NULL DEFAULT 'N',
  PRIMARY KEY (`X_PERS`),
  INDEX `fk_ALUMNO_PERSONA1_idx` (`X_PERS` ASC),
  CONSTRAINT `fk_ALUMNO_PERSONA1`
    FOREIGN KEY (`X_PERS`)
    REFERENCES `colegio`.`PERSONA` (`X_PERS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`CURSO_X_ALUMNO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`CURSO_X_ALUMNO` (
  `CURS_X_CURS` INT NOT NULL,
  `PERS_X_PERS` INT NOT NULL,
  PRIMARY KEY (`CURS_X_CURS`, `PERS_X_PERS`),
  INDEX `fk_CURSO_has_ALUMNO_ALUMNO1_idx` (`PERS_X_PERS` ASC),
  INDEX `fk_CURSO_has_ALUMNO_CURSO1_idx` (`CURS_X_CURS` ASC),
  CONSTRAINT `fk_CURSO_has_ALUMNO_CURSO1`
    FOREIGN KEY (`CURS_X_CURS`)
    REFERENCES `colegio`.`CURSO` (`X_CURS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CURSO_has_ALUMNO_ALUMNO1`
    FOREIGN KEY (`PERS_X_PERS`)
    REFERENCES `colegio`.`ALUMNO` (`X_PERS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`PRUEBA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`PRUEBA` (
  `X_PRUE` INT NOT NULL AUTO_INCREMENT,
  `CURS_X_CURS` INT NOT NULL,
  `T_NOMBRE` VARCHAR(150) NOT NULL,
  `F_RENDICION` DATETIME NOT NULL,
  `F_DURACION` TIME NULL,
  PRIMARY KEY (`X_PRUE`),
  INDEX `fk_PRUEBA_CURSO1_idx` (`CURS_X_CURS` ASC),
  UNIQUE INDEX `X_PRUE_UNIQUE` (`X_PRUE` ASC),
  CONSTRAINT `fk_PRUEBA_CURSO1`
    FOREIGN KEY (`CURS_X_CURS`)
    REFERENCES `colegio`.`CURSO` (`X_CURS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`PRUEBA_X_ALUMNO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`PRUEBA_X_ALUMNO` (
  `PRUE_X_PRUE` INT NOT NULL,
  `PERS_X_PERS` INT NOT NULL,
  `N_NOTA` DECIMAL(2,1) NULL,
  PRIMARY KEY (`PRUE_X_PRUE`, `PERS_X_PERS`),
  INDEX `fk_PRUEBA_has_ALUMNO_ALUMNO1_idx` (`PERS_X_PERS` ASC),
  INDEX `fk_PRUEBA_has_ALUMNO_PRUEBA1_idx` (`PRUE_X_PRUE` ASC),
  CONSTRAINT `fk_PRUEBA_has_ALUMNO_PRUEBA1`
    FOREIGN KEY (`PRUE_X_PRUE`)
    REFERENCES `colegio`.`PRUEBA` (`X_PRUE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_PRUEBA_has_ALUMNO_ALUMNO1`
    FOREIGN KEY (`PERS_X_PERS`)
    REFERENCES `colegio`.`ALUMNO` (`X_PERS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`CURSO_X_ALUMNO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`CURSO_X_ALUMNO` (
  `CURS_X_CURS` INT NOT NULL,
  `PERS_X_PERS` INT NOT NULL,
  PRIMARY KEY (`CURS_X_CURS`, `PERS_X_PERS`),
  INDEX `fk_CURSO_has_ALUMNO_ALUMNO1_idx` (`PERS_X_PERS` ASC),
  INDEX `fk_CURSO_has_ALUMNO_CURSO1_idx` (`CURS_X_CURS` ASC),
  CONSTRAINT `fk_CURSO_has_ALUMNO_CURSO1`
    FOREIGN KEY (`CURS_X_CURS`)
    REFERENCES `colegio`.`CURSO` (`X_CURS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CURSO_has_ALUMNO_ALUMNO1`
    FOREIGN KEY (`PERS_X_PERS`)
    REFERENCES `colegio`.`ALUMNO` (`X_PERS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`PRUEBA_X_ALUMNO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`PRUEBA_X_ALUMNO` (
  `PRUE_X_PRUE` INT NOT NULL,
  `PERS_X_PERS` INT NOT NULL,
  `N_NOTA` DECIMAL(2,1) NULL,
  PRIMARY KEY (`PRUE_X_PRUE`, `PERS_X_PERS`),
  INDEX `fk_PRUEBA_has_ALUMNO_ALUMNO1_idx` (`PERS_X_PERS` ASC),
  INDEX `fk_PRUEBA_has_ALUMNO_PRUEBA1_idx` (`PRUE_X_PRUE` ASC),
  CONSTRAINT `fk_PRUEBA_has_ALUMNO_PRUEBA1`
    FOREIGN KEY (`PRUE_X_PRUE`)
    REFERENCES `colegio`.`PRUEBA` (`X_PRUE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_PRUEBA_has_ALUMNO_ALUMNO1`
    FOREIGN KEY (`PERS_X_PERS`)
    REFERENCES `colegio`.`ALUMNO` (`X_PERS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `colegio`.`COLEGIO`
-- -----------------------------------------------------
START TRANSACTION;
USE `colegio`;
INSERT INTO `colegio`.`COLEGIO` (`X_COLE`, `T_RUT`, `T_NOMBRE`, `T_DIRECCION`) VALUES (1, '16727053-0', 'SKOOL', 'La tierra');

COMMIT;


-- -----------------------------------------------------
-- Data for table `colegio`.`PERSONA`
-- -----------------------------------------------------
START TRANSACTION;
USE `colegio`;
INSERT INTO `colegio`.`PERSONA` (`X_PERS`, `C_RUN`, `T_NOMBRE`, `T_APELLIDO1`, `T_APELLIDO2`, `T_CORREO_ELECTRONICO`, `F_NACIMIENTO`, `L_ACTIVO`) VALUES (1, '12345678-9', 'Bitters', 'Señorita', '', NULL, '1920-04-18', 'S');
INSERT INTO `colegio`.`PERSONA` (`X_PERS`, `C_RUN`, `T_NOMBRE`, `T_APELLIDO1`, `T_APELLIDO2`, `T_CORREO_ELECTRONICO`, `F_NACIMIENTO`, `L_ACTIVO`) VALUES (2, '9876543-2', 'Zim', 'El invasor', NULL, NULL, '1890-04-20', 'S');
INSERT INTO `colegio`.`PERSONA` (`X_PERS`, `C_RUN`, `T_NOMBRE`, `T_APELLIDO1`, `T_APELLIDO2`, `T_CORREO_ELECTRONICO`, `F_NACIMIENTO`, `L_ACTIVO`) VALUES (3, '23456789-2', 'Dib', ' ', NULL, NULL, '2000-08-10', 'S');
INSERT INTO `colegio`.`PERSONA` (`X_PERS`, `C_RUN`, `T_NOMBRE`, `T_APELLIDO1`, `T_APELLIDO2`, `T_CORREO_ELECTRONICO`, `F_NACIMIENTO`, `L_ACTIVO`) VALUES (4, '0000000-0', 'G.I.R.', 'Robot', NULL, NULL, '0001-01-01', 'S');

COMMIT;


-- -----------------------------------------------------
-- Data for table `colegio`.`PROFESOR`
-- -----------------------------------------------------
START TRANSACTION;
USE `colegio`;
INSERT INTO `colegio`.`PROFESOR` (`X_PERS`, `T_TITULO`, `N_SUELDO`) VALUES (1, 'Maestra Maligna', 1000000);

COMMIT;


-- -----------------------------------------------------
-- Data for table `colegio`.`CURSO`
-- -----------------------------------------------------
START TRANSACTION;
USE `colegio`;
INSERT INTO `colegio`.`CURSO` (`X_CURS`, `COLE_X_COLE`, `PERS_X_PERS`, `T_NOMBRE`, `T_DESCRIPCION`, `L_ACTIVO`) VALUES (1, 1, 1, 'Defensa contra alienígenas', '', 'S');
INSERT INTO `colegio`.`CURSO` (`X_CURS`, `COLE_X_COLE`, `PERS_X_PERS`, `T_NOMBRE`, `T_DESCRIPCION`, `L_ACTIVO`) VALUES (2, 1, 1, 'programación', 'Curso para el ejercicio 1', 'S');

COMMIT;


-- -----------------------------------------------------
-- Data for table `colegio`.`ALUMNO`
-- -----------------------------------------------------
START TRANSACTION;
USE `colegio`;
INSERT INTO `colegio`.`ALUMNO` (`X_PERS`, `L_BECADO`) VALUES (2, 'S');
INSERT INTO `colegio`.`ALUMNO` (`X_PERS`, `L_BECADO`) VALUES (3, 'N');

COMMIT;


-- -----------------------------------------------------
-- Data for table `colegio`.`PRUEBA`
-- -----------------------------------------------------
START TRANSACTION;
USE `colegio`;
INSERT INTO `colegio`.`PRUEBA` (`X_PRUE`, `CURS_X_CURS`, `T_NOMBRE`, `F_RENDICION`, `F_DURACION`) VALUES (1, 1, 'Defensa básica', '2015-08-27 16:00:00', '1:00:00');
INSERT INTO `colegio`.`PRUEBA` (`X_PRUE`, `CURS_X_CURS`, `T_NOMBRE`, `F_RENDICION`, `F_DURACION`) VALUES (2, 1, 'Defensa avanzada', '2015-10-27 16:00:00', '1:00:00');
INSERT INTO `colegio`.`PRUEBA` (`X_PRUE`, `CURS_X_CURS`, `T_NOMBRE`, `F_RENDICION`, `F_DURACION`) VALUES (3, 2, 'Programación 1', '2015-08-27 16:00:00', '1:00:00');
INSERT INTO `colegio`.`PRUEBA` (`X_PRUE`, `CURS_X_CURS`, `T_NOMBRE`, `F_RENDICION`, `F_DURACION`) VALUES (4, 2, 'Programación 2', '2015-08-27 16:00:00', '1:00:00');

COMMIT;


-- -----------------------------------------------------
-- Data for table `colegio`.`CURSO_X_ALUMNO`
-- -----------------------------------------------------
START TRANSACTION;
USE `colegio`;
INSERT INTO `colegio`.`CURSO_X_ALUMNO` (`CURS_X_CURS`, `PERS_X_PERS`) VALUES (2, 2);
INSERT INTO `colegio`.`CURSO_X_ALUMNO` (`CURS_X_CURS`, `PERS_X_PERS`) VALUES (2, 3);
INSERT INTO `colegio`.`CURSO_X_ALUMNO` (`CURS_X_CURS`, `PERS_X_PERS`) VALUES (1, 2);
INSERT INTO `colegio`.`CURSO_X_ALUMNO` (`CURS_X_CURS`, `PERS_X_PERS`) VALUES (1, 3);

COMMIT;


-- -----------------------------------------------------
-- Data for table `colegio`.`PRUEBA_X_ALUMNO`
-- -----------------------------------------------------
START TRANSACTION;
USE `colegio`;
INSERT INTO `colegio`.`PRUEBA_X_ALUMNO` (`PRUE_X_PRUE`, `PERS_X_PERS`, `N_NOTA`) VALUES (1, 2, 6.0);
INSERT INTO `colegio`.`PRUEBA_X_ALUMNO` (`PRUE_X_PRUE`, `PERS_X_PERS`, `N_NOTA`) VALUES (1, 3, 5.5);
INSERT INTO `colegio`.`PRUEBA_X_ALUMNO` (`PRUE_X_PRUE`, `PERS_X_PERS`, `N_NOTA`) VALUES (2, 2, 6.0);
INSERT INTO `colegio`.`PRUEBA_X_ALUMNO` (`PRUE_X_PRUE`, `PERS_X_PERS`, `N_NOTA`) VALUES (2, 3, 5.8);
INSERT INTO `colegio`.`PRUEBA_X_ALUMNO` (`PRUE_X_PRUE`, `PERS_X_PERS`, `N_NOTA`) VALUES (3, 2, 5.0);
INSERT INTO `colegio`.`PRUEBA_X_ALUMNO` (`PRUE_X_PRUE`, `PERS_X_PERS`, `N_NOTA`) VALUES (3, 3, 2.0);
INSERT INTO `colegio`.`PRUEBA_X_ALUMNO` (`PRUE_X_PRUE`, `PERS_X_PERS`, `N_NOTA`) VALUES (4, 2, 2.8);
INSERT INTO `colegio`.`PRUEBA_X_ALUMNO` (`PRUE_X_PRUE`, `PERS_X_PERS`, `N_NOTA`) VALUES (4, 3, 1.9);

COMMIT;


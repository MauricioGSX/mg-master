-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-09-2024 a las 15:58:59
-- Versión del servidor: 10.4.28-MariaDB-log
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `marcaslogo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculo_marcas`
--

CREATE TABLE `vehiculo_marcas` (
  `IdMarca` int(11) NOT NULL,
  `NombreMarca` varchar(255) NOT NULL,
  `EstadoMarca` tinyint(1) NOT NULL DEFAULT 0,
  `logo` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `vehiculo_marcas`
--

INSERT INTO `vehiculo_marcas` (`IdMarca`, `NombreMarca`, `EstadoMarca`, `logo`) VALUES
(1, 'ALFA ROMEO', 0, 'alfa-romeo-1.svg'),
(2, 'AUDI', 0, 'audi-13.svg'),
(3, 'BAIC', 0, 'baic-seeklogo.svg'),
(4, 'BEIJING', 0, 'baic-seeklogo.svg'),
(5, 'BMW', 0, 'bmw-2.svg'),
(6, 'BRILLIANCE', 0, 'brilliance-seeklogo.svg'),
(7, 'BYD', 0, 'byd-auto-logo.svg'),
(8, 'CHANGAN', 0, 'changan-automobile-logo-1.svg'),
(9, 'CHERY', 0, 'chery-3.svg'),
(10, 'CHEVROLET', 0, 'chevrolet.svg'),
(11, 'CHRYSLER', 0, 'chrysler-2.svg'),
(12, 'CITROEN', 0, 'citroen-1.svg'),
(13, 'CORSA', 0, 'corsa-seeklogo.svg'),
(14, 'DAEWOO', 0, 'daewoo-1.svg'),
(15, 'DAIHATSU', 0, 'daihatsu-1.svg'),
(16, 'DFM', 0, 'dfm-seeklogo.svg'),
(17, 'DFSK', 0, 'dfsk-seeklogo.svg'),
(18, 'DODGE', 0, 'dodge-4.svg'),
(19, 'DONGFENG', 0, 'dongfeng-seeklogo.svg'),
(20, 'DS', 0, 'ds-automobiles-logo.svg'),
(21, 'EXEED', 0, 'exceed.png'),
(22, 'FAW', 0, 'faw-seeklogo.svg'),
(23, 'FIAT', 0, 'fiat-logo-1.svg'),
(24, 'FIERRO', 0, 'ferro.svg'),
(25, 'FORD', 0, 'ford-1.svg'),
(26, 'FOTON', 0, 'foton-seeklogo.svg'),
(27, 'GAC', 0, 'gac-motor-seeklogo.svg'),
(28, 'GEELY', 0, 'geely-logo-2.svg'),
(29, 'GMC', 0, 'gmc-1.svg'),
(30, 'GREAT WALL', 0, 'great-wall-automotive.svg'),
(31, 'HAVAL', 0, 'haval-seeklogo.svg'),
(32, 'HONDA', 0, 'honda-automobiles-1.svg'),
(33, 'HYUNDAI', 0, 'hyundai-automobiles-1.svg'),
(34, 'INFINITI', 0, 'infiniti-logo-1.svg'),
(35, 'JAC', 0, 'jac-motors-seeklogo.svg'),
(36, 'JAGUAR', 0, 'jaguar-cars.svg'),
(37, 'JEEP', 0, 'jeep-5.svg'),
(38, 'JETOUR', 0, 'jetour-seeklogo.svg'),
(39, 'JINBEI', 0, 'Jinbei-Logo.jpg'),
(40, 'JMC', 0, 'jmc-seeklogo.svg'),
(41, 'KIA', 0, 'kia-4.svg'),
(42, 'LAND ROVER', 0, 'land-rover-1.svg'),
(43, 'LEXUS', 0, 'lexus.svg'),
(44, 'LIFAN', 0, 'lifan-seeklogo.svg'),
(45, 'MAHINDRA', 0, 'mahindra-mahindra-logo.svg'),
(46, 'MAXUS', 0, 'Maxus-Logo-500x281.png'),
(47, 'MAZDA', 0, 'mazda-2.svg'),
(48, 'MERCEDES BENZ', 0, 'mercedes-benz-2.svg'),
(49, 'MG', 0, 'mg.svg'),
(50, 'MINI', 0, 'bmw-mini-1.svg'),
(51, 'MITSUBISHI', 0, 'mitsubishi.svg'),
(52, 'NISSAN', 0, 'nissan-6.svg'),
(53, 'OPEL', 0, 'opel-6.svg'),
(54, 'PEUGEOT', 0, 'peugeot-7.svg'),
(55, 'PORSCHE', 0, 'porsche-6.svg'),
(56, 'RAM', 0, 'dodge-ram.svg'),
(57, 'RENAULT', 0, 'renault-seeklogo.svg'),
(58, 'SAMSUNG', 0, 'samsung-6.svg'),
(59, 'SEAT', 0, 'seat-1.svg'),
(60, 'SKODA', 0, 'skoda-6.svg'),
(61, 'SSANGYONG', 0, 'ssangyong.svg'),
(62, 'SUBARU', 0, 'subaru-12.svg'),
(63, 'SUZUKI', 0, 'suzuki.svg'),
(64, 'TOYOTA', 0, 'toyota-7.svg'),
(65, 'VOLKSWAGEN', 0, 'volkswagen-10.svg'),
(66, 'VOLVO', 0, 'volvo.svg'),
(71, 'TESLA', 0, 'tesla-motors.svg'),
(72, 'MASERATI', 0, 'maserati-2.svg'),
(73, 'LAMBORGHINI', 0, 'lamborghini.svg'),
(74, 'FERRARI', 0, 'ferrari-4.svg'),
(75, 'ROLLS-ROYCE\r\n', 0, 'logo-rolls-royce-por-hernando.svg'),
(76, 'BENTLEY', 0, 'bentley.svg'),
(77, 'MCLAREN', 0, 'mclaren-10.svg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculo_modelos`
--

CREATE TABLE `vehiculo_modelos` (
  `IdModelo` int(11) NOT NULL,
  `NombreModelo` varchar(255) NOT NULL,
  `IdMarca` int(11) NOT NULL,
  `EstadoModelo` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `vehiculo_modelos`
--

INSERT INTO `vehiculo_modelos` (`IdModelo`, `NombreModelo`, `IdMarca`, `EstadoModelo`) VALUES
(1, 'GIULIETTA', 1, 0),
(2, 'GIULIETTA SPORT', 1, 0),
(3, 'MITO', 1, 0),
(4, 'STELVIO', 1, 0),
(5, 'A1', 2, 0),
(6, 'A1 SE', 2, 0),
(7, 'A3', 2, 0),
(8, 'A3 RA17', 2, 0),
(9, 'A3 S LINE', 2, 0),
(10, 'A4', 2, 0),
(11, 'A5', 2, 0),
(12, 'A6', 2, 0),
(13, 'A6 C7', 2, 0),
(14, 'A7', 2, 0),
(15, 'A8', 2, 0),
(16, 'Q2', 2, 0),
(17, 'Q3', 2, 0),
(18, 'Q3 S LINE', 2, 0),
(19, 'Q5', 2, 0),
(20, 'Q7', 2, 0),
(21, 'Q8', 2, 0),
(22, 'TT', 2, 0),
(23, 'TT MK2', 2, 0),
(24, 'PLUS', 3, 0),
(25, 'X25', 3, 0),
(26, 'X35', 3, 0),
(27, 'X5', 3, 0),
(28, 'X55', 3, 0),
(29, 'X3', 4, 0),
(30, '3', 5, 0),
(31, '5', 5, 0),
(32, '118i', 5, 0),
(33, '120i', 5, 0),
(34, '316i', 5, 0),
(35, '318', 5, 0),
(36, '320', 5, 0),
(37, '325', 5, 0),
(38, '520', 5, 0),
(39, '730', 5, 0),
(40, 'X6', 5, 0),
(41, '116i', 5, 0),
(42, '118i', 5, 0),
(43, '135i', 5, 0),
(44, '235i', 5, 0),
(45, '320 I GRAN TURISIMO', 5, 0),
(46, '320 LINE SPORT', 5, 0),
(47, '320D', 5, 0),
(48, '320i', 5, 0),
(49, '328i', 5, 0),
(50, '428i - F32 - F36', 5, 0),
(51, '5 SEDAN', 5, 0),
(52, '520-530', 5, 0),
(53, '520D', 5, 0),
(54, '528 - 530', 5, 0),
(55, '528i', 5, 0),
(56, '620D', 5, 0),
(57, '740I 740IL', 5, 0),
(58, '750i', 5, 0),
(59, 'CABRIOLET', 5, 0),
(60, 'E32 - E34', 5, 0),
(61, 'E36', 5, 0),
(62, 'E90 318 330', 5, 0),
(63, 'E92 E93', 5, 0),
(64, 'F10', 5, 0),
(65, 'F20', 5, 0),
(66, 'F20 SERIE 1', 5, 0),
(67, 'F20 - F22 - F23 - F87', 5, 0),
(68, 'F20 - F21', 5, 0),
(69, 'F30', 5, 0),
(70, 'F30 F30i', 5, 0),
(71, 'F30 - F31', 5, 0),
(72, 'G30', 5, 0),
(73, 'M3', 5, 0),
(74, 'M4', 5, 0),
(75, 'M5', 5, 0),
(76, 'R1200', 5, 0),
(77, 'SERIE 1', 5, 0),
(78, 'SERIE 1 116D', 5, 0),
(79, 'SERIE 1 E90-E91', 5, 0),
(80, 'SERIE 1 F20', 5, 0),
(81, 'SERIE 1 F20 118i', 5, 0),
(82, 'SERIE 1 F20 180i', 5, 0),
(83, 'SERIE 1 F20 M SPORT', 5, 0),
(84, 'SERIE 1 F20 - F21', 5, 0),
(85, 'SERIE 1 F30 - F31', 5, 0),
(86, 'SERIE 1 M SPORT F20', 5, 0),
(87, 'SERIE 2  228i XDRIVE', 5, 0),
(88, 'SERIE 3', 5, 0),
(89, 'SERIE 3 E46 320', 5, 0),
(90, 'SERIE 3 E90 - E91', 5, 0),
(91, 'SERIE 3 E92', 5, 0),
(92, 'SERIE 3 F30', 5, 0),
(93, 'SERIE 3 F30 - F31', 5, 0),
(94, 'SERIE 3 F30 - F80', 5, 0),
(95, 'SERIE 4 F32 - F33 - F34', 5, 0),
(96, 'SERIE 5', 5, 0),
(97, 'SERIE 5 E60', 5, 0),
(98, 'SERIE 5 E90 - E91', 5, 0),
(99, 'SERIE 5 F10 - F11', 5, 0),
(100, 'SERIE 5 TOURING', 5, 0),
(101, 'SERIE 6 F06', 5, 0),
(102, 'SERIE 7', 5, 0),
(103, 'SERIE M 120i', 5, 0),
(104, 'W169 W245', 5, 0),
(105, 'X1', 5, 0),
(106, 'X1 F48', 5, 0),
(107, 'X1 F48 - F49', 5, 0),
(108, 'X3', 5, 0),
(109, 'X3 - X4', 5, 0),
(110, 'X3 - X4 - G01 - G02', 5, 0),
(111, 'X4', 5, 0),
(112, 'X5', 5, 0),
(113, 'X5 E70', 5, 0),
(114, 'X5 XDRIVE', 5, 0),
(115, 'X5M', 5, 0),
(116, 'Z4', 5, 0),
(117, '428i - F32 - F36', 5, 0),
(118, 'H220', 6, 0),
(119, 'H230', 6, 0),
(120, 'KONECT', 6, 0),
(121, 'T30', 6, 0),
(122, 'V3', 6, 0),
(123, 'BM5', 6, 0),
(124, 'F0', 7, 0),
(125, 'F3', 7, 0),
(126, 'F3R', 7, 0),
(127, 'F5 SURI', 7, 0),
(128, 'S6', 7, 0),
(129, 'A 500', 8, 0),
(130, 'ALSVIN', 8, 0),
(131, 'CS15', 8, 0),
(132, 'CS35', 8, 0),
(133, 'CS35 PLUS', 8, 0),
(134, 'CS55', 8, 0),
(135, 'CS75', 8, 0),
(136, 'CV1', 8, 0),
(137, 'CV2', 8, 0),
(138, 'CX20', 8, 0),
(139, 'CX70', 8, 0),
(140, 'HUNTER', 8, 0),
(141, 'M201', 8, 0),
(142, 'MD01', 8, 0),
(143, 'MD201', 8, 0),
(144, 'M201 - MD201', 8, 0),
(145, 'UNI-T', 8, 0),
(146, 'V', 8, 0),
(147, 'CS1 CROSS', 8, 0),
(148, 'TIGGO 2', 9, 0),
(149, 'TIGGO 4', 9, 0),
(150, 'ARRIZO', 9, 0),
(151, 'ARRIZO 3', 9, 0),
(152, 'ARRIZO 5', 9, 0),
(153, 'ARRIZO 5 - TIGGO 7 Y 8', 9, 0),
(154, 'ARRIZO 7', 9, 0),
(155, 'DESTINY', 9, 0),
(156, 'DESTINY V-5', 9, 0),
(157, 'EXEED', 9, 0),
(158, 'EXEED LX', 9, 0),
(159, 'EXEED TLX', 9, 0),
(160, 'FULWIN', 9, 0),
(161, 'FULWIN 2', 9, 0),
(162, 'IQ', 9, 0),
(163, 'K60', 9, 0),
(164, 'TIGGO', 9, 0),
(165, 'TIGGO 2 PRO', 9, 0),
(166, 'TIGGO 3', 9, 0),
(167, 'TIGGO 3 PRO', 9, 0),
(168, 'TIGGO 3 - 4', 9, 0),
(169, 'TIGGO 4 PRO', 9, 0),
(170, 'TIGGO 5', 9, 0),
(171, 'TIGGO 7', 9, 0),
(172, 'TIGGO 7 PRO', 9, 0),
(173, 'TIGGO 8', 9, 0),
(174, 'TIGGO 8 PRO', 9, 0),
(175, 'TIGGO 8 PRO MAX', 9, 0),
(176, 'TIGGO T11', 9, 0),
(177, 'AVEO', 10, 0),
(178, 'AVEO SEDAN', 10, 0),
(179, 'AVEO SPORT', 10, 0),
(180, 'CAMARO', 10, 0),
(181, 'CAPTIVA', 10, 0),
(182, 'COLORADO', 10, 0),
(183, 'COMBO', 10, 0),
(184, 'CORSA', 10, 0),
(185, 'CORSA 1.6 MEC S/AC', 10, 0),
(186, 'CORSA EVOLUTION ', 10, 0),
(187, 'CORSA PLUS', 10, 0),
(188, 'CRUZE', 10, 0),
(189, 'CRUZE HB', 10, 0),
(190, 'CRUZE SPORT', 10, 0),
(191, 'DMAX', 10, 0),
(192, 'DMAX MEC 2.5 4X4 ', 10, 0),
(193, 'EQUINOX', 10, 0),
(194, 'GROOVE', 10, 0),
(195, 'LUV', 10, 0),
(196, 'MONTANA', 10, 0),
(197, 'MONTANA EVOLUTION', 10, 0),
(198, 'N300', 10, 0),
(199, 'N400', 10, 0),
(200, 'NEW SAIL', 10, 0),
(201, 'ONIX', 10, 0),
(202, 'ONIX - PRISMA', 10, 0),
(203, 'OPEL ASTRA', 10, 0),
(204, 'OPTRA', 10, 0),
(205, 'ORLANDO', 10, 0),
(206, 'PRISMA', 10, 0),
(207, 'PRISMA LTZ', 10, 0),
(208, 'PRISMA - ONIX', 10, 0),
(209, 'PRISMA - ONIX LED', 10, 0),
(210, 'SAIL', 10, 0),
(211, 'SILVERADO', 10, 0),
(212, 'SONIC', 10, 0),
(213, 'SONIC SEDAN', 10, 0),
(214, 'SPARK', 10, 0),
(215, 'SPARK  SEDAN ', 10, 0),
(216, 'SPARK GT', 10, 0),
(217, 'SPARK GT 1.2', 10, 0),
(218, 'SPARK GT SEDAN', 10, 0),
(219, 'SPARK LT', 10, 0),
(220, 'SPARK LT 1.0 MEC', 10, 0),
(221, 'SPIN', 10, 0),
(222, 'SUBURBAN', 10, 0),
(223, 'TAHOE', 10, 0),
(224, 'TRACKER', 10, 0),
(225, 'TRACKER - SONIC', 10, 0),
(226, 'TRAIBLAZER - COLORADO', 10, 0),
(227, 'TRAVERSE', 10, 0),
(228, 'CARAVAN', 11, 0),
(229, 'PT CRUISER', 11, 0),
(230, 'SEBRING', 11, 0),
(231, 'TOWN', 11, 0),
(232, 'TOWN & COUNTRY', 11, 0),
(233, 'C4 CACTUS', 12, 0),
(234, 'BELINGO - PEUGEOT - PARTNER', 12, 0),
(235, 'BERLINGO', 12, 0),
(236, 'BERLINGO PASAJEROS', 12, 0),
(237, 'BERLINGO - PARTNER', 12, 0),
(238, 'BIPPER - CITY - NEMO', 12, 0),
(239, 'C1', 12, 0),
(240, 'C3', 12, 0),
(241, 'C3 AIRCROSS', 12, 0),
(242, 'C4', 12, 0),
(243, 'C4 GRAND PICASSO', 12, 0),
(244, 'C4 PICASSO', 12, 0),
(245, 'C5', 12, 0),
(246, 'C5 AIRCROSS', 12, 0),
(247, 'CACTUS', 12, 0),
(248, 'C-ELYSEE', 12, 0),
(249, 'C-ELYSEE - 301', 12, 0),
(250, 'DS3', 12, 0),
(251, 'DS4', 12, 0),
(252, 'DS3 - DS4', 12, 0),
(253, 'DS5', 12, 0),
(254, 'DS7 CROSSBACK', 12, 0),
(255, 'GRAND C4 PICASSO', 12, 0),
(256, 'JUMPY', 12, 0),
(257, 'NEMO', 12, 0),
(258, 'SPACE', 12, 0),
(259, 'XSARA', 12, 0),
(260, 'XSARA PICASSO', 12, 0),
(261, 'XSARA STATION', 12, 0),
(262, 'OPEL', 13, 0),
(263, 'LANOS', 14, 0),
(264, 'CHARADE', 15, 0),
(265, 'A30', 19, 0),
(266, 'JOYEAR SX5', 19, 0),
(267, 'S500', 19, 0),
(268, 'SX6', 19, 0),
(269, '500', 17, 0),
(270, '560', 17, 0),
(271, '580', 17, 0),
(272, '500 ACTIVE', 17, 0),
(273, 'C21', 17, 0),
(274, 'C21 - C22', 17, 0),
(275, 'C25 TRUCK', 17, 0),
(276, 'C31', 17, 0),
(277, 'C32', 17, 0),
(278, 'C35', 17, 0),
(279, 'C37', 17, 0),
(280, 'CARGO BOX', 17, 0),
(281, 'CARGO CS21 - CS22 - C525', 17, 0),
(282, 'CARGO TRUCK  BOX', 17, 0),
(283, 'CARGO VAN', 17, 0),
(284, 'CARGO VAN - BOX', 17, 0),
(285, 'GLORY 500', 17, 0),
(286, 'GLORY 560', 17, 0),
(287, 'GLORY 580', 17, 0),
(288, 'H3O CROSS', 17, 0),
(289, 'K05 CARGO VAN', 17, 0),
(290, 'MINITRUCK SERIE K', 17, 0),
(291, 'SUV 500', 17, 0),
(292, 'SX6', 17, 0),
(293, 'V27', 17, 0),
(294, 'CALIBER', 18, 0),
(295, 'CHALLENGER', 18, 0),
(296, 'CHARGER', 18, 0),
(297, 'CHARGER SXT', 18, 0),
(298, 'COLIVER', 18, 0),
(299, 'DAKOTA', 18, 0),
(300, 'DURANGO', 18, 0),
(301, 'GRAND CARAVAN', 18, 0),
(302, 'JOURNEY', 18, 0),
(303, 'NITRO ', 18, 0),
(304, 'RAM 1000', 18, 0),
(305, 'RAM 1000 - FIAT TORO', 18, 0),
(306, 'RAM 1500', 18, 0),
(307, 'RAM 1500 4X4', 18, 0),
(308, 'RAM 1500 LIMITED', 18, 0),
(309, 'RAM 1501', 18, 0),
(310, 'RAM 2500', 18, 0),
(311, 'RAM 700', 18, 0),
(312, 'RAM 700 - FIAT STRADA', 18, 0),
(313, 'RAM PRO MASTER', 18, 0),
(314, '580', 19, 0),
(315, 'AX4', 19, 0),
(316, 'AX7', 19, 0),
(317, 'C35', 19, 0),
(318, 'CV03', 19, 0),
(319, 'DF6', 19, 0),
(320, 'DFM A30', 19, 0),
(321, 'DFM S30 ELEGANT', 19, 0),
(322, 'DFSK 580', 19, 0),
(323, 'DFSK X30', 19, 0),
(324, 'GLORY 560', 19, 0),
(325, 'GLORY 580', 19, 0),
(326, 'JOYEAR X3', 19, 0),
(327, 'RICH6', 19, 0),
(328, 'S50', 19, 0),
(329, 'SX5', 19, 0),
(330, 'SX6', 19, 0),
(331, 'B50', 22, 0),
(332, 'BESTURN B50', 22, 0),
(333, 'BESTURN X80', 22, 0),
(334, 'D60', 22, 0),
(335, 'F80', 22, 0),
(336, 'FOISON VAN', 22, 0),
(337, 'LUXURY R7', 22, 0),
(338, 'OLEY', 22, 0),
(339, 'OLEY HATCHBACK', 22, 0),
(340, 'OLEY HB', 22, 0),
(341, 'OLEY SPORT', 22, 0),
(342, 'R7 LUXURY', 22, 0),
(343, 'R7', 22, 0),
(344, 'T80', 22, 0),
(345, 'V2', 22, 0),
(346, 'V5', 22, 0),
(347, 'X7', 22, 0),
(348, 'X80', 22, 0),
(349, '500', 23, 0),
(350, '500X', 23, 0),
(351, '500X CROSSOVER', 23, 0),
(352, 'ARGO', 23, 0),
(353, 'ARGO CRONOS', 23, 0),
(354, 'CITY', 23, 0),
(355, 'BIPPER - CITY - NEMO', 23, 0),
(356, 'CRONOS', 23, 0),
(357, 'DOBLO', 23, 0),
(358, 'DUCATO', 23, 0),
(359, 'ESTRADA', 23, 0),
(360, 'FIORINO', 23, 0),
(361, 'FIORINO - RAM 700', 23, 0),
(362, 'FIORINO - NEMO - BIPPER', 23, 0),
(363, 'FIORINO - CITY', 23, 0),
(364, 'FIORINO - CITY - BIPPER - NEMO', 23, 0),
(365, 'FIORINO - CITY - NEMO - BIPPER', 23, 0),
(366, 'FIORINO - CITY - RAM 700', 23, 0),
(367, 'FIORINO FIRE', 23, 0),
(368, 'FIORINO - RAM 700 RAPID', 23, 0),
(369, 'FIORINO - UNO', 23, 0),
(370, 'FULLBACK', 23, 0),
(371, 'FULLBACK - RAM 1200', 23, 0),
(372, 'GRANDE PUNTO', 23, 0),
(373, 'IDEA', 23, 0),
(374, 'LINEA', 23, 0),
(375, 'MOBI', 23, 0),
(376, 'PALIO', 23, 0),
(377, 'PALIO ADVENTURE', 23, 0),
(378, 'PULSE', 23, 0),
(379, 'PUNTO', 23, 0),
(380, 'QUBO', 23, 0),
(381, 'RAM 1000', 23, 0),
(382, 'SIENA', 23, 0),
(383, 'STRADA', 23, 0),
(384, 'STRADA 1,8', 23, 0),
(385, 'STRADA TREKKING', 23, 0),
(386, 'STRADA - ADVENTURE', 23, 0),
(387, 'STRADA - RAM 700', 23, 0),
(388, 'TIPO', 23, 0),
(389, 'TIPO SEDAN', 23, 0),
(390, 'TORO', 23, 0),
(391, 'TORO - RAM 1000', 23, 0),
(392, 'UNO', 23, 0),
(393, 'UNO - FIORINO', 23, 0),
(394, 'UNO FIRE', 23, 0),
(395, 'UNO SPORTING', 23, 0),
(396, 'UNO WAY', 23, 0),
(397, 'UNO - PUNTO', 23, 0),
(398, 'DOBLO - RAM 1000', 23, 0),
(399, 'FIORINO', 23, 0),
(400, 'FIORINO - UNO', 23, 0),
(401, 'FIERRO', 24, 0),
(402, 'BRONCO', 25, 0),
(403, 'ECOSPORT', 25, 0),
(404, 'EDGE', 25, 0),
(405, 'ESCAPE', 25, 0),
(406, 'EXPEDITION', 25, 0),
(407, 'EXPLORER', 25, 0),
(408, 'F150', 25, 0),
(409, 'F150 PLATINUM', 25, 0),
(410, 'FIESTA', 25, 0),
(411, 'FOCUS', 25, 0),
(412, 'FUSION', 25, 0),
(413, 'KA', 25, 0),
(414, 'MUSTANG', 25, 0),
(415, 'RANGER', 25, 0),
(416, 'RANGER - RAPTOR', 25, 0),
(417, 'RAPTOR', 25, 0),
(418, 'TERRITORY', 25, 0),
(419, 'MIDI', 26, 0),
(420, 'MIDI CARGO ', 26, 0),
(421, 'TERRACOTA', 26, 0),
(422, 'TM3', 26, 0),
(423, 'MIDI', 26, 0),
(424, 'GS3', 27, 0),
(425, 'GS4', 27, 0),
(426, 'GS4 - GA4', 27, 0),
(427, 'ATLAS', 28, 0),
(428, 'ATLAS PRO', 28, 0),
(429, 'AZKARRA', 28, 0),
(430, 'CK', 28, 0),
(431, 'COOLRAY', 28, 0),
(432, 'EXEED LX', 28, 0),
(433, 'GC7', 28, 0),
(434, 'GS', 28, 0),
(435, 'LC', 28, 0),
(436, 'MX', 28, 0),
(437, 'X7', 28, 0),
(438, 'SIERRA 2500', 29, 0),
(439, 'C30', 30, 0),
(440, 'DEER', 30, 0),
(441, 'FLORID', 30, 0),
(442, 'FLORID CROSS', 30, 0),
(443, 'H6', 30, 0),
(444, 'HAVAL', 30, 0),
(445, 'HAVAL DARGO', 30, 0),
(446, 'HAVAL H2', 30, 0),
(447, 'HAVAL H3', 30, 0),
(448, 'HAVAL H5', 30, 0),
(449, 'HAVAL H5 - H3', 30, 0),
(450, 'HAVAL H6', 30, 0),
(451, 'HAVAL H7', 30, 0),
(452, 'HAVAL JOLION', 30, 0),
(453, 'JOLION', 30, 0),
(454, 'M4', 30, 0),
(455, 'POER', 30, 0),
(456, 'VOLEEX C  PLUS', 30, 0),
(457, 'VOLEEX C10', 30, 0),
(458, 'VOLEEX C20', 30, 0),
(459, 'VOLEEX C30', 30, 0),
(460, 'VOLEEX C30 PLUS', 30, 0),
(461, 'VOLEEX C50', 30, 0),
(462, 'WINGLE', 30, 0),
(463, 'WINGLE 5', 30, 0),
(464, 'WINGLE 6', 30, 0),
(465, 'WINGLE 7', 30, 0),
(466, 'WINGLE 8', 30, 0),
(467, 'H2', 31, 0),
(468, 'H3', 31, 0),
(469, 'H5', 31, 0),
(470, 'H6', 31, 0),
(471, 'HAVAL H3', 31, 0),
(472, 'JOLION', 31, 0),
(473, 'ACCORD', 32, 0),
(474, 'ACCORD COUPE', 32, 0),
(475, 'ACCORD SEDAN', 32, 0),
(476, 'ACURA', 32, 0),
(477, 'CITY', 32, 0),
(478, 'CIVIC', 32, 0),
(479, 'CIVIC COUPE', 32, 0),
(480, 'CIVIC SEDAN', 32, 0),
(481, 'CRV', 32, 0),
(482, 'CRV TURBO', 32, 0),
(483, 'FIT', 32, 0),
(484, 'FIT  JAZZ', 32, 0),
(485, 'FIT - CITY', 32, 0),
(486, 'HR-V', 32, 0),
(487, 'IO', 32, 0),
(488, 'PILOT', 32, 0),
(489, 'RIDGELINE', 32, 0),
(490, 'STREAM', 32, 0),
(491, 'WRV', 32, 0),
(492, 'ACCENT', 33, 0),
(493, 'i10', 33, 0),
(494, 'ACCENT HB', 33, 0),
(495, 'ACCENT HC', 33, 0),
(496, 'ACCENT HCI PLUS', 33, 0),
(497, 'ACCENT PLUS', 33, 0),
(498, 'ACCENT PRIME', 33, 0),
(499, 'ACCENT RB', 33, 0),
(500, 'ACCENT SEDAN', 33, 0),
(501, 'ATOS', 33, 0),
(502, 'AZERA', 33, 0),
(503, 'CRETA', 33, 0),
(504, 'ELANTRA', 33, 0),
(505, 'ELANTRA GT', 33, 0),
(506, 'EON', 33, 0),
(507, 'GENESIS', 33, 0),
(508, 'GETZ', 33, 0),
(509, 'GRAND i10', 33, 0),
(510, 'GRAND i10 HB', 33, 0),
(511, 'GRAND i10 SEDAN', 33, 0),
(512, 'GRAND i10 SPORT', 33, 0),
(513, 'GRAND i20', 33, 0),
(514, 'GRAND i20 SEDAN', 33, 0),
(515, 'GRAND SANTA FE', 33, 0),
(516, 'H1', 33, 0),
(517, 'H100', 33, 0),
(518, 'H100 PORTER', 33, 0),
(519, 'i10 ACTIVE', 33, 0),
(520, 'i20', 33, 0),
(521, 'i30', 33, 0),
(522, 'IONIQ', 33, 0),
(523, 'KONA', 33, 0),
(524, 'PALISADE', 33, 0),
(525, 'PORTER', 33, 0),
(526, 'PORTER - H100', 33, 0),
(527, 'RIO ACCENT RB', 33, 0),
(528, 'SANTA FE', 33, 0),
(529, 'SANTA FE SPORT', 33, 0),
(530, 'SANTA FE - KIA SORENTO', 33, 0),
(531, 'SANTA FE - TUCSON', 33, 0),
(532, 'SONATA', 33, 0),
(533, 'TERRACAN', 33, 0),
(534, 'TUCSON', 33, 0),
(535, 'VELOSTER', 33, 0),
(536, 'VENUE', 33, 0),
(537, 'VERACRUZ', 33, 0),
(538, 'VERNA', 33, 0),
(539, 'VERNA i20', 33, 0),
(540, 'Q30', 34, 0),
(541, 'Q50', 34, 0),
(542, 'QX30', 34, 0),
(543, 'QX50', 34, 0),
(544, 'QX70', 34, 0),
(545, '137', 35, 0),
(546, 'GRAND S3', 35, 0),
(547, 'J2', 35, 0),
(548, 'J3', 35, 0),
(549, 'J3 SPORT', 35, 0),
(550, 'J4', 35, 0),
(551, 'J5', 35, 0),
(552, 'JS2', 35, 0),
(553, 'JS3', 35, 0),
(554, 'JS4', 35, 0),
(555, 'REFINE', 35, 0),
(556, 'S1', 35, 0),
(557, 'S2', 35, 0),
(558, 'S2 - JS2', 35, 0),
(559, 'S3', 35, 0),
(560, 'S3 - JS3', 35, 0),
(561, 'S4', 35, 0),
(562, 'S5', 35, 0),
(563, 'S8', 35, 0),
(564, 'T6', 35, 0),
(565, 'T8', 35, 0),
(566, 'X200', 35, 0),
(567, 'F-PACE', 36, 0),
(568, 'SERIE XK', 36, 0),
(569, 'XF', 36, 0),
(570, 'XJ', 36, 0),
(571, 'CHEROKEE', 37, 0),
(572, 'CHEROKEE LIBERTY', 37, 0),
(573, 'CHEROKEE LIMITED', 37, 0),
(574, 'CHEROKEE OVERLAND', 37, 0),
(575, 'COMPASS', 37, 0),
(576, 'COMPASS-PATRIOT', 37, 0),
(577, 'DURANGO', 37, 0),
(578, 'GRAND CHEROKEE', 37, 0),
(579, 'LIBERTY', 37, 0),
(580, 'PATRIOT', 37, 0),
(581, 'RENEGADE', 37, 0),
(582, 'RENEGADE - COMPASS', 37, 0),
(583, 'RENEGADE - COMPASS', 37, 0),
(584, 'RENEGADE - CHEROKEE', 37, 0),
(585, 'WRANGLER', 37, 0),
(586, 'WRANGLER LIBERTY', 37, 0),
(587, 'X70', 38, 0),
(588, 'VIGUS', 40, 0),
(589, 'VIGUS PLUS', 40, 0),
(590, 'VIGUS WORK', 40, 0),
(591, '4 5', 41, 0),
(592, 'CARENS', 41, 0),
(593, 'CARNIVAL', 41, 0),
(594, 'CELERIO', 41, 0),
(595, 'CERATO', 41, 0),
(596, 'CERATO GT SPORT', 41, 0),
(597, 'FRONTIER', 41, 0),
(598, 'GRAND CARNIVAL', 41, 0),
(599, 'KIA', 41, 0),
(600, 'L200', 41, 0),
(601, 'MORNING', 41, 0),
(602, 'MORNING GT', 41, 0),
(603, 'NEW CRETA GRAND', 33, 0),
(604, 'OPTIMA', 41, 0),
(605, 'RIO', 41, 0),
(606, 'RIO 3', 41, 0),
(607, 'RIO 3 - 4 - 5', 41, 0),
(608, 'RIO 3 - 5', 41, 0),
(609, 'RIO 3 SPORT', 41, 0),
(610, 'RIO 4', 41, 0),
(611, 'RIO 4 - 5', 41, 0),
(612, 'RIO 4 SEDAN ', 41, 0),
(613, 'RIO 5', 41, 0),
(614, 'RIO 5 SPORT', 41, 0),
(615, 'RIO - CARNIVAL', 41, 0),
(616, 'RIO JB', 41, 0),
(617, 'RIO - ACCENT RB', 41, 0),
(618, 'SELTOS', 41, 0),
(619, 'SOLUTO', 41, 0),
(620, 'SONET', 41, 0),
(621, 'SORENTO', 41, 0),
(622, 'SOUL', 41, 0),
(623, 'SPECTRA', 41, 0),
(624, 'SPORTAGE', 41, 0),
(625, 'TUCSON', 41, 0),
(626, 'DISCOVERY SPORT', 42, 0),
(627, '800', 42, 0),
(628, 'DISCOVERY', 42, 0),
(629, 'EVOQUE', 42, 0),
(630, 'FREELANDER', 42, 0),
(631, 'RANGE EVOQUE', 42, 0),
(632, 'RANGE ROVER SPORT', 42, 0),
(633, 'RANGER ROVER EVOQUE', 42, 0),
(634, 'RANGER ROVER SPORT', 42, 0),
(635, 'ROVER SPORT', 42, 0),
(636, '570 LX', 43, 0),
(637, 'H3', 43, 0),
(638, 'NX', 43, 0),
(639, 'RX 350', 43, 0),
(640, '320', 44, 0),
(641, '520', 44, 0),
(642, '530', 44, 0),
(643, '520 HB', 44, 0),
(644, '520 SEDAN', 44, 0),
(645, '620 SOLANO', 44, 0),
(646, 'BREZZ 520', 44, 0),
(647, 'FOISON', 44, 0),
(648, 'FOISON ONE', 44, 0),
(649, 'FOISON VAN', 44, 0),
(650, 'SMILY', 44, 0),
(651, 'X60', 44, 0),
(652, 'X7', 44, 0),
(653, 'X7 MYWAY', 44, 0),
(654, 'XUV 500', 45, 0),
(655, 'GENIO', 45, 0),
(656, 'KUV 100', 45, 0),
(657, 'PICK UP', 45, 0),
(658, 'PICKUP - SCORPIO', 45, 0),
(659, 'SCORPIO', 45, 0),
(660, 'XUV', 45, 0),
(661, 'XUV 100', 45, 0),
(662, 'T60', 46, 0),
(663, '2', 47, 0),
(664, '3', 47, 0),
(665, '5', 47, 0),
(666, '6', 47, 0),
(667, '323', 47, 0),
(668, '626', 47, 0),
(669, '929', 47, 0),
(670, '2 SEDAN', 47, 0),
(671, '2 SPORT', 47, 0),
(672, '3 SEDAN', 47, 0),
(673, '3 SPORT', 47, 0),
(674, '3 SPORT PORTALON', 47, 0),
(675, '3 Y 6', 47, 0),
(676, '6 SPORT', 47, 0),
(677, 'APV', 47, 0),
(678, 'BT50', 47, 0),
(679, 'BT50 - RANGER', 47, 0),
(680, 'CX 30', 47, 0),
(681, 'CX 7', 47, 0),
(682, 'CX 9', 47, 0),
(683, 'CX 3', 47, 0),
(684, 'CX 5', 47, 0),
(685, 'CX 6', 47, 0),
(686, 'CX 70', 47, 0),
(687, 'MAZDA3', 47, 0),
(688, 'MIATA MX5', 47, 0),
(689, 'MX 5', 47, 0),
(690, 'MX 5 - MIATA', 47, 0),
(691, '220', 48, 0),
(692, 'A-150', 48, 0),
(693, 'A200 D', 48, 0),
(694, 'A200 - A250', 48, 0),
(695, 'BENZ A200', 48, 0),
(696, 'C CLASS C200', 48, 0),
(697, 'C CLASS W205', 48, 0),
(698, 'C CLASS W205 C200', 48, 0),
(699, 'C180', 48, 0),
(700, 'C200', 48, 0),
(701, 'C240', 48, 0),
(702, 'C240 B180', 48, 0),
(703, 'C300 - W205', 48, 0),
(704, 'C63', 48, 0),
(705, 'CITAN', 48, 0),
(706, 'CLA 220', 48, 0),
(707, 'CLA C117', 48, 0),
(708, 'CLASE A', 48, 0),
(709, 'CLASS SE', 48, 0),
(710, 'CLASS W212', 48, 0),
(711, 'CLASSE X', 48, 0),
(712, 'CLS550', 48, 0),
(713, 'E350', 48, 0),
(714, 'E250', 48, 0),
(715, 'E300 - E350', 48, 0),
(716, 'E350 - E550', 48, 0),
(717, 'E-CLASS C180', 48, 0),
(718, 'GL 3500', 48, 0),
(719, 'GLA', 48, 0),
(720, 'GLA 200', 48, 0),
(721, 'GLA 220', 48, 0),
(722, 'GLA 250', 48, 0),
(723, 'GLC X253', 48, 0),
(724, 'GLE', 48, 0),
(725, 'GLE 400', 48, 0),
(726, 'GLK 250', 48, 0),
(727, 'GLS 450', 48, 0),
(728, 'ML 350', 48, 0),
(729, 'ML 350 - 450 - 550 - GL550 - SLK350 - 280', 48, 0),
(730, 'ML400', 48, 0),
(731, 'R272', 48, 0),
(732, 'SPRINTER', 48, 0),
(733, 'VITO', 48, 0),
(734, 'W156 GLA CLASS', 48, 0),
(735, 'W176', 48, 0),
(736, 'W176 CLASS', 48, 0),
(737, 'W177 CLA', 48, 0),
(738, 'W204', 48, 0),
(739, 'W207', 48, 0),
(740, 'W212', 48, 0),
(741, 'W213', 48, 0),
(742, 'W220', 48, 0),
(743, 'W246', 48, 0),
(744, 'W246 - W242 ', 48, 0),
(745, 'X CLASS', 48, 0),
(746, 'X250 D', 48, 0),
(747, 'C CLASS W204', 48, 0),
(748, 'W117 CLASS', 48, 0),
(749, 'W176 M CLASS', 48, 0),
(750, '117', 48, 0),
(751, 'A CLASS', 48, 0),
(752, 'A200', 48, 0),
(753, 'GLE 350B', 48, 0),
(754, '3', 49, 0),
(755, '4', 49, 0),
(756, '5', 49, 0),
(757, '6', 49, 0),
(758, '350', 49, 0),
(759, 'EXTENDER', 49, 0),
(760, 'GS', 49, 0),
(761, 'GT', 49, 0),
(762, 'HS', 49, 0),
(763, 'MG 6', 49, 0),
(764, 'MG3', 49, 0),
(765, 'RX5', 49, 0),
(766, 'ZR', 49, 0),
(767, 'ZS', 49, 0),
(768, 'ZS EV', 49, 0),
(769, 'ZS - ZX', 49, 0),
(770, 'ZX', 49, 0),
(771, 'COOPER', 50, 0),
(772, 'COOPER COUNTRYMAN', 50, 0),
(773, 'COOPER COUNTRYMAN F60', 50, 0),
(774, 'COOPER S', 50, 0),
(775, 'COOPER SR 56', 50, 0),
(776, 'COOPER WORKS', 50, 0),
(777, 'MONTERO SPORT', 51, 0),
(778, 'ASX', 51, 0),
(779, 'CROSS', 51, 0),
(780, 'DAKAR', 51, 0),
(781, 'ECLIPSE', 51, 0),
(782, 'ECLIPSE CROSS', 51, 0),
(783, 'GALANT', 51, 0),
(784, 'L200', 51, 0),
(785, 'L200 DAKAR', 51, 0),
(786, 'L200 KATANA', 51, 0),
(787, 'L200 WORK', 51, 0),
(788, 'L200 WORK - KATANA', 51, 0),
(789, 'L200 - MONTERO', 51, 0),
(790, 'L300', 51, 0),
(791, 'LANCER', 51, 0),
(792, 'MIRAGE', 51, 0),
(793, 'MONTERO', 51, 0),
(794, 'MONTERO IV', 51, 0),
(795, 'OULANDER', 51, 0),
(796, 'OUTBACK', 51, 0),
(797, 'OUTLANDER', 51, 0),
(798, 'OUTLANDER - LANCER', 51, 0),
(799, 'OUTLANDER SPORT', 51, 0),
(800, 'ALTIMA', 52, 0),
(801, 'D21', 52, 0),
(802, 'JUKE', 52, 0),
(803, 'KICKS', 52, 0),
(804, 'L200', 52, 0),
(805, 'LEAF', 52, 0),
(806, 'MARCH', 52, 0),
(807, 'MARCH 1.6 FONDO ROJO ', 52, 0),
(808, 'MURANO', 52, 0),
(809, 'NAVARA', 52, 0),
(810, 'NAVARA NP300', 52, 0),
(811, 'NOTE', 52, 0),
(812, 'NP300', 52, 0),
(813, 'NP300 4X2', 52, 0),
(814, 'NP300 4X4', 52, 0),
(815, 'NV350', 52, 0),
(816, 'PATHFINDER', 52, 0),
(817, 'PLATINA', 52, 0),
(818, 'PRIMERA', 52, 0),
(819, 'QASHQAI', 52, 0),
(820, 'QASHQAI 1.6', 52, 0),
(821, 'SENTRA', 52, 0),
(822, 'TERRANO', 52, 0),
(823, 'TIIDA', 52, 0),
(824, 'TIIDA JAPONES', 52, 0),
(825, 'TIIDA SEDAN', 52, 0),
(826, 'TIIDA SPORT', 52, 0),
(827, 'V16', 52, 0),
(828, 'VERSA', 52, 0),
(829, 'VERSA 1.6', 52, 0),
(830, 'XTRAIL', 52, 0),
(831, 'XTRAIL T32', 52, 0),
(832, 'ADAM', 53, 0),
(833, 'ANTARA', 53, 0),
(834, 'ASTRA', 53, 0),
(835, 'CORSA', 53, 0),
(836, 'CROSSLAND', 53, 0),
(837, 'GRANDLAND X', 53, 0),
(838, 'INSIGNIA', 53, 0),
(839, 'INSIGNIA GRAND SPORT', 53, 0),
(840, 'MERIVA', 53, 0),
(841, 'MOKKA', 53, 0),
(842, 'VECTRA', 53, 0),
(843, '107', 54, 0),
(844, '108', 54, 0),
(845, '206', 54, 0),
(846, '207', 54, 0),
(847, '208', 54, 0),
(848, '301', 54, 0),
(849, '307', 54, 0),
(850, '308', 54, 0),
(851, '406', 54, 0),
(852, '508', 54, 0),
(853, '1007', 54, 0),
(854, '2008', 54, 0),
(855, '3008', 54, 0),
(856, '5008', 54, 0),
(857, '207 SPORT', 54, 0),
(858, '208 GT', 54, 0),
(859, '208 - 207', 54, 0),
(860, '3008 - 5008', 54, 0),
(861, '301 - CITY - C-ELYSEE', 54, 0),
(862, '301 - C-ELYSEE', 54, 0),
(863, '307 - 308 - 3008', 54, 0),
(864, '308 - CITROEN C4', 54, 0),
(865, '308 - BERLINGO C4', 54, 0),
(866, '5008 - 3008', 54, 0),
(867, 'BERLINGO', 54, 0),
(868, 'BIPPER', 54, 0),
(869, 'BIPPER - NEMO', 54, 0),
(870, 'BOXER', 54, 0),
(871, 'C-ELYSEE - 301', 54, 0),
(872, 'EXPERT', 54, 0),
(873, 'GARNISH  RIFTER', 54, 0),
(874, 'PARTNER', 54, 0),
(875, 'RCZ', 54, 0),
(876, 'RIFTER', 54, 0),
(877, 'TRAVELER', 54, 0),
(878, '911', 55, 0),
(879, '951 - 944', 55, 0),
(880, 'CARRERA', 55, 0),
(881, 'CARRERA 911', 55, 0),
(882, 'CAYENNE', 55, 0),
(883, 'CAYENNE - MACAN', 55, 0),
(884, '700', 56, 0),
(885, '1000', 56, 0),
(886, 'RAM 1000', 56, 0),
(887, 'ALASKAN', 57, 0),
(888, 'ARKANA', 57, 0),
(889, 'C3', 57, 0),
(890, 'CAPTUR', 57, 0),
(891, 'CLIO IV', 57, 0),
(892, 'CLIO', 57, 0),
(893, 'CLIO 4', 57, 0),
(894, 'CLIO - DUSTER', 57, 0),
(895, 'DOKKER', 57, 0),
(896, 'DUSTER', 57, 0),
(897, 'DUSTER - OROCH', 57, 0),
(898, 'EXPRESS', 57, 0),
(899, 'FLUENCE', 57, 0),
(900, 'KANGOO', 57, 0),
(901, 'KOLEOS', 57, 0),
(902, 'KWID', 57, 0),
(903, 'LOGAN', 57, 0),
(904, 'MASTER', 57, 0),
(905, 'MEGANE', 57, 0),
(906, 'MEGANE 2', 57, 0),
(907, 'MEGANE 3', 57, 0),
(908, 'MEGANE IV', 57, 0),
(909, 'OROCH', 57, 0),
(910, 'SANDERO', 57, 0),
(911, 'SYMBOL', 57, 0),
(912, 'KONEC 1.6', 6, 0),
(913, 'SM3', 58, 0),
(914, 'ATECA', 59, 0),
(915, 'IBIZA', 59, 0),
(916, 'FABIA', 60, 0),
(917, 'KODIAQ', 60, 0),
(918, 'OCTAVIA', 60, 0),
(919, 'RAPID', 60, 0),
(920, 'YETI', 60, 0),
(921, 'ACTYON', 61, 0),
(922, 'ACTYON - REXTON', 61, 0),
(923, 'ACTYON SPORT', 61, 0),
(924, 'ACTYON SPORT 2.0', 61, 0),
(925, 'ACTYON SPORT - ACTYON', 61, 0),
(926, 'ACYON SPORT', 61, 0),
(927, 'GRAND MUSSO', 61, 0),
(928, 'KORANDO', 61, 0),
(929, 'KORONADO', 61, 0),
(930, 'KYRON', 61, 0),
(931, 'MUSSO', 61, 0),
(932, 'MUSSO - REXTON', 61, 0),
(933, 'REXTON', 61, 0),
(934, 'REXTON - MUSSO', 61, 0),
(935, 'STAVIC', 61, 0),
(936, 'STAVIC 05', 61, 0),
(937, 'TIVOLI', 61, 0),
(938, 'TIVOLI XLV', 61, 0),
(939, 'TIVOLI XVL', 61, 0),
(940, 'ASCENT', 62, 0),
(941, 'EVOLTIS', 62, 0),
(942, 'FORESTER', 62, 0),
(943, 'FOSTER', 62, 0),
(944, 'IMPRESA SPORT GT', 62, 0),
(945, 'IMPREZA', 62, 0),
(946, 'IMPREZA  XV', 62, 0),
(947, 'IMPREZA GT', 62, 0),
(948, 'IMPREZA GT2', 62, 0),
(949, 'IMPREZA HATCHBACK', 62, 0),
(950, 'IMPREZA SEDAN', 62, 0),
(951, 'IMPREZA SPORT', 62, 0),
(952, 'IMPREZA SPORT GT', 62, 0),
(953, 'IMPREZA SPORT XV', 62, 0),
(954, 'IMPREZA - WRX', 62, 0),
(955, 'XV - IMPREZA', 62, 0),
(956, 'LECAGY - OUTBACK', 62, 0),
(957, 'LEGACY', 62, 0),
(958, 'LEGACY - OUTBACK', 62, 0),
(959, 'OUTBACK', 62, 0),
(960, 'OUTBACK - LEGACY', 62, 0),
(961, 'OUTBACK LEGASY', 62, 0),
(962, 'TRIBECA', 62, 0),
(963, 'WRX', 62, 0),
(964, 'WRX STI', 62, 0),
(965, 'XV', 62, 0),
(966, 'XV CROSSTREK', 62, 0),
(967, 'CROSSTREK', 62, 0),
(968, 'AERIO', 63, 0),
(969, 'ALTO', 63, 0),
(970, 'ALTO 800', 63, 0),
(971, 'ALTO K10', 63, 0),
(972, 'APV', 63, 0),
(973, 'BALENO', 63, 0),
(974, 'BALENO GLS', 63, 0),
(975, 'BALENO GLX', 63, 0),
(976, 'BALENO MEC 1.6', 63, 0),
(977, 'BT50', 63, 0),
(978, 'CARRY', 63, 0),
(979, 'CELERIO', 63, 0),
(980, 'CERVO', 63, 0),
(981, 'CIAZ', 63, 0),
(982, 'CIAZ - S-PRESSO - SWIT - DEZIRE', 63, 0),
(983, 'DRIVE - SWIFT', 63, 0),
(984, 'DZIRE', 63, 0),
(985, 'ERTIGA', 63, 0),
(986, 'GRAN NOMADE', 63, 0),
(987, 'GRAN VITARA', 63, 0),
(988, 'GRAN VITARA - NOMADE', 63, 0),
(989, 'GRAND NOMADE', 63, 0),
(990, 'GRAND VITARA', 63, 0),
(991, 'GRAND VITARA - GRAND NOMADE', 63, 0),
(992, 'GRAND VITARA - NOMADE', 63, 0),
(993, 'IGNIS', 63, 0),
(994, 'JIMNY', 63, 0),
(995, 'KIZASHI', 63, 0),
(996, 'MARUTI', 63, 0),
(997, 'NEW VITARA', 63, 0),
(998, 'NOMADE', 63, 0),
(999, 'NOMADE - VITARA', 63, 0),
(1000, 'SAMURAI', 63, 0),
(1001, 'S-CROSS', 63, 0),
(1002, 'S-PRESSO', 63, 0),
(1003, 'SWIFT', 63, 0),
(1004, 'SWIFT - DZIRE', 63, 0),
(1005, 'SWIFT INDIO', 63, 0),
(1006, 'SWIFT JAPONES', 63, 0),
(1007, 'SWIFT SPORT', 63, 0),
(1008, 'SX4', 63, 0),
(1009, 'SX4 1.6', 63, 0),
(1010, 'SX4 HB', 63, 0),
(1011, 'SX4 S-CROSS', 63, 0),
(1012, 'SX4 SEDAN', 63, 0),
(1013, 'SX4 SPORT', 63, 0),
(1014, 'VITARA', 63, 0),
(1015, 'VITARA - NOMADE', 63, 0),
(1016, 'VITARA 4TA G', 63, 0),
(1017, 'VITARA TURBO', 63, 0),
(1018, 'WAGON', 63, 0),
(1019, 'XL7', 63, 0),
(1020, '4RUNNER', 64, 0),
(1021, 'AURIS', 64, 0),
(1022, 'AVENSIS', 64, 0),
(1023, 'CAMRY', 64, 0),
(1024, 'COROLLA', 64, 0),
(1025, 'COROLLA SEDAN', 64, 0),
(1026, 'COROLLA SPORT', 64, 0),
(1027, 'CRESSIDA', 64, 0),
(1028, 'FJ CRUISER', 64, 0),
(1029, 'FORTUNER', 64, 0),
(1030, 'HIGHLANDER', 64, 0),
(1031, 'HILUX', 64, 0),
(1032, 'HILUX REVO', 64, 0),
(1033, 'LAND CRUISER PRADO', 64, 0),
(1034, 'NEW YARIS', 64, 0),
(1035, 'PRIUS', 64, 0),
(1036, 'RAV4', 64, 0),
(1037, 'TERIO RUSH', 64, 0),
(1038, 'TERIOS', 64, 0),
(1039, 'TUNDRA', 64, 0),
(1040, 'URBAN CRUISER', 64, 0),
(1041, 'YARIS', 64, 0),
(1042, 'YARIS HATCHBACK', 64, 0),
(1043, 'YARIS SEDAN', 64, 0),
(1044, 'YARIS SPORT', 64, 0),
(1045, 'AMAROK', 65, 0),
(1046, 'ATLAS', 65, 0),
(1047, 'BEETLE', 65, 0),
(1048, 'BORA', 65, 0),
(1049, 'CADDY', 65, 0),
(1050, 'CROSSFOX', 65, 0),
(1051, 'G5', 65, 0),
(1052, 'GO - VOYAGE - SAVEIRO', 65, 0),
(1053, 'GOL', 65, 0),
(1054, 'GOL G5', 65, 0),
(1055, 'GOL G5 SAVEIRO', 65, 0),
(1056, 'GOL G6', 65, 0),
(1057, 'GOL G6 SPORT', 65, 0),
(1058, 'GOL G7', 65, 0),
(1059, 'GOL G7 - G8', 65, 0),
(1060, 'GOL G7 VOYAGE', 65, 0),
(1061, 'GOL G8', 65, 0),
(1062, 'GOL G8 - SAVEIRO', 65, 0),
(1063, 'GOL SAVEIRO', 65, 0),
(1064, 'GOL SAVEIRO G8', 65, 0),
(1065, 'GOL SPORT', 65, 0),
(1066, 'GOL TREND', 65, 0),
(1067, 'GOL VOYAGE', 65, 0),
(1068, 'GOL VOYAGE G8', 65, 0),
(1069, 'GOL VOYAGE SAVEIRO', 65, 0),
(1070, 'GOL - SAVEIRO G8', 65, 0),
(1071, 'GOL - SEVEIRO - VIYAGE', 65, 0),
(1072, 'GOL - VOYAGE', 65, 0),
(1073, 'GOLF', 65, 0),
(1074, 'GOLF A6', 65, 0),
(1075, 'GOLF G7', 65, 0),
(1076, 'GOLF MK6', 65, 0),
(1077, 'GOLF STATION', 65, 0),
(1078, 'GOLF - JETTA', 65, 0),
(1079, 'GOL - VOYAGE - SAVEIRO', 65, 0),
(1080, 'JETTA', 65, 0),
(1081, 'JETTA 19 - 23', 65, 0),
(1082, 'JETTA CLASICO', 65, 0),
(1083, 'KOMBI', 65, 0),
(1084, 'NIVUS', 65, 0),
(1085, 'PASSAT', 65, 0),
(1086, 'POLO', 65, 0),
(1087, 'POLO SPORT', 65, 0),
(1088, 'POLO VIRTUS', 65, 0),
(1089, 'POLO - VIRTUS', 65, 0),
(1090, 'SAVEIRO', 65, 0),
(1091, 'SAVEIRO G7', 65, 0),
(1092, 'SAVEIRO GOL', 65, 0),
(1093, 'TAOS', 65, 0),
(1094, 'T-CROSS', 65, 0),
(1095, 'T-CROSS PLUS', 65, 0),
(1096, 'TIGUAN', 65, 0),
(1097, 'TOUAREG', 65, 0),
(1098, 'TRANSPORTER', 65, 0),
(1099, 'VIRTUS', 65, 0),
(1100, 'VIRTUS - POLO', 65, 0),
(1101, 'VOYAGE', 65, 0),
(1102, '580', 66, 0),
(1103, '660 CLASSIC', 66, 0),
(1104, 'C30', 66, 0),
(1105, 'C70', 66, 0),
(1106, 'S40', 66, 0),
(1107, 'S40 - V40', 66, 0),
(1108, 'S60', 66, 0),
(1109, 'S80', 66, 0),
(1110, 'S89 - C70', 66, 0),
(1111, 'V40', 66, 0),
(1112, 'V40 2.0', 66, 0),
(1113, 'V40 D2', 66, 0),
(1114, 'V40 SPORT', 66, 0),
(1115, 'V50', 66, 0),
(1116, 'V50 - S40', 66, 0),
(1117, 'V60', 66, 0),
(1118, 'V70', 66, 0),
(1119, 'V90', 66, 0),
(1120, 'XC40', 66, 0),
(1121, 'XC60', 66, 0),
(1122, 'XC70', 66, 0),
(1123, 'XC90', 66, 0),
(1124, 'RIO 5 HB', 41, 0),
(1125, 'M135', 5, 0),
(1126, 'GOL HB', 65, 0),
(1127, 'IMPREZA GH', 62, 0),
(1128, 'KARL', 53, 0),
(1129, 'XTRAIL T31', 52, 0),
(1130, '340i SPORT', 5, 0),
(1131, '500', 19, 0),
(1132, 'CS35', 17, 0),
(1133, 'LAND ROVER', 25, 0),
(1134, 'X30', 6, 0),
(1135, 'Vivaro', 53, 0),
(1136, 'XV', 62, 0),
(1137, 'KIA RIO JB 1.4', 41, 0),
(1138, 'CELERIO - SWIFT', 63, 0),
(1139, 'ALTO - AERIO - SWIFT', 63, 0),
(1140, 'ALTO - CIAZ - DZIRE', 63, 0),
(1141, 'FORTE', 41, 0),
(1142, '228-230 M', 5, 0),
(1143, 'CRAFTER', 65, 0),
(1144, 'TORRES', 61, 0),
(1145, 'LS PANDA', 28, 0),
(1146, 'PLUS', 30, 0),
(1147, 'HIACE', 64, 0),
(1148, 'K07 S', 17, 0),
(1149, 'K07 S', 17, 0),
(1150, '4008', 54, 0),
(1151, '308 active', 54, 0),
(1152, '308 active', 54, 0),
(1153, '308 active', 54, 0),
(1154, 'TRAX', 10, 0),
(1155, 'HIACE', 64, 0),
(1156, 'RUSH', 63, 0),
(1157, 'RUSH', 64, 0),
(1158, 'F55 - F56 ', 50, 0),
(1159, 'F55 - F56 ', 50, 0),
(1160, 'TLS COUPÉ', 2, 0),
(1161, 'TLS COUPÉ', 2, 0),
(1162, 'W166', 48, 0),
(1163, 'COBALT', 10, 0),
(1164, 'cross', 64, 0),
(1165, '535 GT', 5, 0),
(1166, '139I M SPORT', 5, 0),
(1167, 'CS25', 17, 0),
(1168, 'E300', 48, 0),
(1169, '330i', 5, 0),
(1170, 'E350', 5, 0),
(1171, 'E28', 5, 0),
(1172, 'TERIOS', 15, 0),
(1173, '640I COUPE', 5, 0),
(1174, 'C CLASS W203', 48, 0),
(1175, 'RAIZE', 64, 0),
(1176, 'js6', 35, 0),
(1177, 'M 245', 3, 0),
(1178, 'BRONCO', 25, 0),
(1179, 'MOHAVE', 41, 0),
(1180, 'MOHAVE', 41, 0),
(1181, '220D', 48, 0),
(1182, 'STARIA', 33, 0),
(1183, 'X1 SDRIVE 18d', 5, 0),
(1184, 'W205 C-CLASS', 48, 0),
(1185, 'X 250D', 48, 0),
(1186, 'LX', 21, 0),
(1187, 'COROLLA CROSS', 64, 0),
(1188, 'SEQUOIA', 64, 0),
(1189, 'DS7', 20, 0),
(1190, 'ONIX TURBO', 10, 0),
(1191, 'SANDERO / DUSTER / SYMBOL', 57, 0),
(1192, 'NIRO', 41, 0),
(1193, 'COLORADO Z71', 10, 0),
(1194, 'MIGTHY HD 65', 33, 0),
(1195, 'STINGER', 41, 0),
(1196, 'SERIE 1 E87 E81', 5, 0),
(1197, 'TRANSIT ', 25, 0),
(1198, 'V 1000', 56, 0),
(1199, 'TXL', 21, 0),
(1200, 'ONIX SEDAN', 10, 0),
(1201, 'EX35', 34, 0),
(1202, 'QX60', 34, 0),
(1203, 'TOURING', 40, 0),
(1204, 'FX35', 34, 0),
(1205, 'HAISE', 39, 0),
(1206, 'S-CLASS W221', 48, 0),
(1207, 'ARGO TREKKING', 23, 0),
(1208, 'SPARK SPORT', 10, 0),
(1209, 'V6', 6, 0),
(1210, 'giulia', 1, 0),
(1211, '220d', 48, 0),
(1212, 'RANGER SPORT', 42, 0),
(1213, 'v90', 46, 0),
(1214, 'SEBRING', 11, 0),
(1215, 'GRADIATOR', 37, 0),
(1216, '315', 48, 0),
(1217, 'TRAIBLAZER', 10, 0),
(1218, 'WRANGLER GLADIATOR', 37, 0),
(1219, 'SUNNY', 52, 0),
(1220, '306', 54, 0),
(1221, 'PARTNER-CITROEN-BERLINGO', 54, 0),
(1222, 'GOLF MK4', 65, 0),
(1223, 'RACER', 14, 0),
(1224, 'VX', 21, 0),
(1225, 'ACCENT LC', 33, 0),
(1226, 'SO COOL', 30, 0),
(1227, 'SPACETOURER ', 12, 0),
(1229, 'CADENZA', 41, 0),
(1230, 'SUV 560', 17, 0),
(1231, 'MODEL S', 71, 0),
(1232, 'MODEL 3', 71, 0),
(1233, 'MODEL X', 71, 0),
(1234, 'MODEL Y', 71, 0),
(1235, 'CYBERTRUCK', 71, 0),
(1236, 'ROADSTER', 71, 0),
(1237, 'GHIBLI', 72, 0),
(1238, 'LEVANTE', 72, 0),
(1239, 'QUATTROPORTE', 72, 0),
(1240, 'GRANTURISMO', 72, 0),
(1241, 'GRANCABRIO', 72, 0),
(1242, 'AVENTADOR', 73, 0),
(1243, 'HURACÁN', 73, 0),
(1244, 'URUS', 73, 0),
(1245, 'GALLARDO', 73, 0),
(1246, 'MURCIÉLAGO', 73, 0),
(1247, 'DIABLO', 73, 0),
(1248, 'SESTO ELEMENTO', 73, 0),
(1249, 'VENENO', 73, 0),
(1250, 'CENTENARIO', 73, 0),
(1251, 'REVENTÓN', 73, 0),
(1252, '488 GTB', 74, 0),
(1253, '812 SUPERFAST', 74, 0),
(1254, 'F8 TRIBUTO', 74, 0),
(1255, 'PORTOFINO', 74, 0),
(1256, 'LAFERRARI', 74, 0),
(1257, 'GTC4LUSSO', 74, 0),
(1258, 'SF90 STRADALE', 74, 0),
(1259, 'F12 BERLINETTA', 74, 0),
(1260, 'ENZO', 74, 0),
(1261, 'CALIFORNIA', 74, 0),
(1262, 'PHANTOM', 75, 0),
(1263, 'GHOST', 75, 0),
(1264, 'WRAITH', 75, 0),
(1265, 'DAWN', 75, 0),
(1266, 'CULLINAN', 75, 0),
(1267, 'SILVER SPUR', 75, 0),
(1268, 'SILVER GHOST', 75, 0),
(1269, 'CORNICHE', 75, 0),
(1270, 'SILVER SHADOW', 75, 0),
(1271, 'CONTINENTAL GT', 76, 0),
(1272, 'BENTAYGA', 76, 0),
(1273, 'FLYING SPUR', 76, 0),
(1274, 'MULSANNE', 76, 0),
(1275, 'ARNAGE', 76, 0),
(1276, 'BROOKLANDS', 76, 0),
(1277, 'AZURE', 76, 0),
(1278, '720S', 77, 0),
(1279, '600LT', 77, 0),
(1280, 'GT', 77, 0),
(1281, 'P1', 77, 0),
(1282, '570S', 77, 0),
(1283, '650S', 77, 0),
(1284, 'MP4-12C', 77, 0),
(1285, 'SENNA', 77, 0),
(1286, '765LT', 77, 0),
(1287, 'ELVA', 77, 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `vehiculo_marcas`
--
ALTER TABLE `vehiculo_marcas`
  ADD PRIMARY KEY (`IdMarca`);

--
-- Indices de la tabla `vehiculo_modelos`
--
ALTER TABLE `vehiculo_modelos`
  ADD PRIMARY KEY (`IdModelo`),
  ADD KEY `IdMarca` (`IdMarca`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `vehiculo_marcas`
--
ALTER TABLE `vehiculo_marcas`
  MODIFY `IdMarca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT de la tabla `vehiculo_modelos`
--
ALTER TABLE `vehiculo_modelos`
  MODIFY `IdModelo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1288;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `vehiculo_modelos`
--
ALTER TABLE `vehiculo_modelos`
  ADD CONSTRAINT `vehiculo_modelos_ibfk_1` FOREIGN KEY (`IdMarca`) REFERENCES `vehiculo_marcas` (`IdMarca`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 28, 2018 at 03:16 PM
-- Server version: 5.7.23-0ubuntu0.16.04.1
-- PHP Version: 7.0.32-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_rec_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `accept_list`
--

CREATE TABLE `accept_list` (
  `id` bigint(20) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `accept_list`
--

INSERT INTO `accept_list` (`id`, `user_id`, `time_stamp`) VALUES
(1, 'Q_236', '2018-09-27 06:38:33'),
(2, 'Q_80', '2018-09-27 12:25:02'),
(3, 'Q_82', '2018-09-28 01:50:57'),
(4, 'Q_82', '2018-09-28 01:50:57'),
(5, 'Q_236', '2018-09-28 06:19:06'),
(6, 'Q_102', '2018-09-28 01:24:45'),
(7, 'Q_102', '2018-09-28 01:24:45'),
(8, 'Q_121', '2018-09-28 06:53:11'),
(9, 'Q_139', '2018-09-28 07:01:18'),
(10, 'Q_141', '2018-09-28 07:01:36'),
(11, 'Q_149', '2018-09-28 07:05:43'),
(12, 'Q_173', '2018-09-28 01:42:32'),
(13, 'Q_175', '2018-09-28 01:44:51'),
(14, 'Q_178', '2018-09-28 01:54:59');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add user', 2, 'add_user'),
(6, 'Can change user', 2, 'change_user'),
(7, 'Can delete user', 2, 'delete_user'),
(8, 'Can view user', 2, 'view_user'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(4, 'auth', 'group'),
(3, 'auth', 'permission'),
(2, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-09-19 06:02:59.066899'),
(2, 'auth', '0001_initial', '2018-09-19 06:03:18.434096'),
(3, 'admin', '0001_initial', '2018-09-19 06:03:23.070745'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-09-19 06:03:23.141053'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2018-09-19 06:03:23.258671'),
(6, 'contenttypes', '0002_remove_content_type_name', '2018-09-19 06:03:25.483933'),
(7, 'auth', '0002_alter_permission_name_max_length', '2018-09-19 06:03:25.711340'),
(8, 'auth', '0003_alter_user_email_max_length', '2018-09-19 06:03:25.944313'),
(9, 'auth', '0004_alter_user_username_opts', '2018-09-19 06:03:26.056611'),
(10, 'auth', '0005_alter_user_last_login_null', '2018-09-19 06:03:27.498798'),
(11, 'auth', '0006_require_contenttypes_0002', '2018-09-19 06:03:27.572158'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2018-09-19 06:03:27.674753'),
(13, 'auth', '0008_alter_user_username_max_length', '2018-09-19 06:03:28.065928'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2018-09-19 06:03:28.359985'),
(15, 'sessions', '0001_initial', '2018-09-19 06:03:30.042810');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `reject_list`
--

CREATE TABLE `reject_list` (
  `id` bigint(20) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reject_list`
--

INSERT INTO `reject_list` (`id`, `user_id`, `time_stamp`) VALUES
(1, 'Q_1', '2018-09-27 11:38:04'),
(2, 'Q_2', '2018-09-27 11:52:29'),
(3, 'Q_3', '2018-09-27 06:39:08'),
(4, 'Q_4', '2018-09-27 06:39:08'),
(5, 'Q_5', '2018-09-27 06:39:08'),
(6, 'Q_6', '2018-09-27 06:39:09'),
(7, 'Q_7', '2018-09-27 06:39:09'),
(8, 'Q_8', '2018-09-27 06:39:10'),
(9, 'Q_9', '2018-09-27 06:39:10'),
(10, 'Q_10', '2018-09-27 06:39:11'),
(11, 'Q_11', '2018-09-27 06:39:12'),
(12, 'Q_12', '2018-09-27 06:39:14'),
(13, 'Q_13', '2018-09-27 06:39:14'),
(14, 'Q_14', '2018-09-27 06:39:15'),
(15, 'Q_15', '2018-09-27 06:39:16'),
(16, 'Q_16', '2018-09-27 06:39:16'),
(17, 'Q_17', '2018-09-27 06:39:17'),
(18, 'Q_18', '2018-09-27 06:39:17'),
(19, 'Q_19', '2018-09-27 06:39:18'),
(20, 'Q_20', '2018-09-27 06:39:18'),
(21, 'Q_21', '2018-09-27 06:39:18'),
(22, 'Q_22', '2018-09-27 06:39:19'),
(23, 'Q_23', '2018-09-27 06:39:19'),
(24, 'Q_24', '2018-09-27 06:39:21'),
(25, 'Q_25', '2018-09-27 06:39:21'),
(26, 'Q_26', '2018-09-27 06:39:22'),
(27, 'Q_27', '2018-09-27 06:39:22'),
(28, 'Q_28', '2018-09-27 06:39:23'),
(29, 'Q_29', '2018-09-27 06:39:23'),
(30, 'Q_30', '2018-09-27 06:39:24'),
(31, 'Q_31', '2018-09-27 06:39:24'),
(32, 'Q_32', '2018-09-27 06:39:25'),
(33, 'Q_33', '2018-09-27 06:39:26'),
(34, 'Q_34', '2018-09-27 06:39:26'),
(35, 'Q_35', '2018-09-27 06:39:27'),
(36, 'Q_36', '2018-09-27 06:39:27'),
(37, 'Q_37', '2018-09-27 06:39:28'),
(38, 'Q_38', '2018-09-27 06:39:28'),
(39, 'Q_39', '2018-09-27 06:39:28'),
(40, 'Q_40', '2018-09-27 06:39:30'),
(41, 'Q_41', '2018-09-27 06:39:31'),
(42, 'Q_42', '2018-09-27 06:39:32'),
(43, 'Q_43', '2018-09-27 06:39:33'),
(44, 'Q_44', '2018-09-27 06:39:33'),
(45, 'Q_45', '2018-09-27 06:39:34'),
(46, 'Q_46', '2018-09-27 06:39:34'),
(47, 'Q_47', '2018-09-27 06:39:36'),
(48, 'Q_48', '2018-09-27 06:39:36'),
(49, 'Q_49', '2018-09-27 06:39:37'),
(50, 'Q_50', '2018-09-27 06:39:37'),
(51, 'Q_51', '2018-09-27 06:39:39'),
(52, 'Q_52', '2018-09-27 06:39:40'),
(53, 'Q_53', '2018-09-27 06:39:40'),
(54, 'Q_54', '2018-09-27 06:39:41'),
(55, 'Q_55', '2018-09-27 06:39:41'),
(56, 'Q_56', '2018-09-27 06:39:42'),
(57, 'Q_57', '2018-09-27 06:39:42'),
(58, 'Q_58', '2018-09-27 06:39:43'),
(59, 'Q_59', '2018-09-27 06:39:45'),
(60, 'Q_60', '2018-09-27 06:39:46'),
(61, 'Q_61', '2018-09-27 06:39:46'),
(62, 'Q_62', '2018-09-27 06:39:47'),
(63, 'Q_63', '2018-09-27 06:39:48'),
(64, 'Q_64', '2018-09-27 06:39:48'),
(65, 'Q_65', '2018-09-27 06:39:49'),
(66, 'Q_66', '2018-09-27 06:39:49'),
(67, 'Q_67', '2018-09-27 06:39:50'),
(68, 'Q_68', '2018-09-27 06:39:50'),
(69, 'Q_69', '2018-09-27 06:39:51'),
(70, 'Q_70', '2018-09-27 06:39:52'),
(71, 'Q_71', '2018-09-27 06:39:53'),
(72, 'Q_72', '2018-09-27 06:39:54'),
(73, 'Q_73', '2018-09-27 06:39:55'),
(74, 'Q_74', '2018-09-27 06:39:56'),
(75, 'Q_75', '2018-09-27 06:39:57'),
(76, 'Q_76', '2018-09-27 06:39:58'),
(77, 'Q_77', '2018-09-27 06:40:00'),
(78, 'Q_78', '2018-09-27 06:40:00'),
(79, 'Q_79', '2018-09-27 06:40:00'),
(80, 'Q_80', '2018-09-27 06:51:54'),
(81, 'Q_81', '2018-09-27 06:51:58'),
(82, 'Q_82', '2018-09-27 06:55:41'),
(83, 'Q_83', '2018-09-27 06:55:48'),
(84, 'Q_84', '2018-09-28 00:03:35'),
(85, 'Q_85', '2018-09-28 00:03:45'),
(86, 'Q_86', '2018-09-28 00:04:52'),
(87, 'Q_87', '2018-09-28 00:05:25'),
(88, 'Q_88', '2018-09-28 00:06:10'),
(89, 'Q_89', '2018-09-28 00:06:21'),
(90, 'Q_90', '2018-09-28 00:06:22'),
(91, 'Q_91', '2018-09-28 00:06:25'),
(92, 'Q_92', '2018-09-28 00:06:33'),
(93, 'Q_93', '2018-09-28 00:06:33'),
(94, 'Q_94', '2018-09-28 00:06:34'),
(95, 'Q_95', '2018-09-28 00:06:34'),
(96, 'Q_96', '2018-09-28 00:06:35'),
(97, 'Q_97', '2018-09-28 00:06:35'),
(98, 'Q_98', '2018-09-28 00:06:36'),
(99, 'Q_99', '2018-09-28 00:06:36'),
(100, 'Q_100', '2018-09-28 00:06:37'),
(101, 'Q_101', '2018-09-28 00:06:37'),
(102, 'Q_102', '2018-09-28 01:21:09'),
(103, 'Q_103', '2018-09-28 01:21:17'),
(104, 'Q_104', '2018-09-28 01:21:21'),
(105, 'Q_105', '2018-09-28 01:21:25'),
(106, 'Q_106', '2018-09-28 01:21:28'),
(107, 'Q_107', '2018-09-28 01:21:31'),
(108, 'Q_108', '2018-09-28 01:21:35'),
(109, 'Q_109', '2018-09-28 01:21:38'),
(110, 'Q_110', '2018-09-28 01:22:04'),
(111, 'Q_111', '2018-09-28 01:22:08'),
(112, 'Q_112', '2018-09-28 01:22:12'),
(113, 'Q_113', '2018-09-28 01:22:16'),
(114, 'Q_114', '2018-09-28 01:22:23'),
(115, 'Q_115', '2018-09-28 01:22:29'),
(116, 'Q_116', '2018-09-28 01:22:32'),
(117, 'Q_117', '2018-09-28 01:22:36'),
(118, 'Q_118', '2018-09-28 01:22:39'),
(119, 'Q_119', '2018-09-28 01:22:43'),
(120, 'Q_120', '2018-09-28 01:22:46'),
(121, 'Q_121', '2018-09-28 01:22:51'),
(122, 'Q_122', '2018-09-28 01:22:54'),
(123, 'Q_123', '2018-09-28 01:23:03'),
(124, 'Q_124', '2018-09-28 01:23:14'),
(125, 'Q_125', '2018-09-28 01:23:19'),
(126, 'Q_126', '2018-09-28 01:23:23'),
(127, 'Q_127', '2018-09-28 01:23:27'),
(128, 'Q_128', '2018-09-28 01:23:32'),
(129, 'Q_129', '2018-09-28 01:23:36'),
(130, 'Q_130', '2018-09-28 01:23:43'),
(131, 'Q_131', '2018-09-28 01:23:46'),
(132, 'Q_132', '2018-09-28 01:23:49'),
(133, 'Q_133', '2018-09-28 01:23:53'),
(134, 'Q_134', '2018-09-28 01:23:57'),
(135, 'Q_135', '2018-09-28 01:24:01'),
(136, 'Q_136', '2018-09-28 01:24:04'),
(137, 'Q_137', '2018-09-28 01:24:07'),
(138, 'Q_138', '2018-09-28 01:24:12'),
(139, 'Q_139', '2018-09-28 01:31:02'),
(140, 'Q_140', '2018-09-28 01:31:05'),
(141, 'Q_141', '2018-09-28 01:31:08'),
(142, 'Q_142', '2018-09-28 01:31:12'),
(143, 'Q_143', '2018-09-28 01:31:22'),
(144, 'Q_144', '2018-09-28 01:31:25'),
(145, 'Q_145', '2018-09-28 01:31:31'),
(146, 'Q_146', '2018-09-28 01:31:35'),
(147, 'Q_147', '2018-09-28 01:31:39'),
(148, 'Q_148', '2018-09-28 01:31:42'),
(149, 'Q_149', '2018-09-28 01:35:34'),
(150, 'Q_150', '2018-09-28 01:35:38'),
(151, 'Q_151', '2018-09-28 01:35:43'),
(152, 'Q_152', '2018-09-28 01:35:53'),
(153, 'Q_153', '2018-09-28 01:36:02'),
(154, 'Q_154', '2018-09-28 01:36:06'),
(155, 'Q_155', '2018-09-28 01:36:13'),
(156, 'Q_156', '2018-09-28 01:36:17'),
(157, 'Q_157', '2018-09-28 01:36:21'),
(158, 'Q_158', '2018-09-28 01:38:22'),
(159, 'Q_159', '2018-09-28 01:38:26'),
(160, 'Q_160', '2018-09-28 01:38:30'),
(161, 'Q_161', '2018-09-28 01:38:33'),
(162, 'Q_162', '2018-09-28 01:38:37'),
(163, 'Q_163', '2018-09-28 01:38:41'),
(164, 'Q_164', '2018-09-28 01:38:44'),
(165, 'Q_165', '2018-09-28 01:38:48'),
(166, 'Q_166', '2018-09-28 01:38:51'),
(167, 'Q_167', '2018-09-28 01:38:56'),
(168, 'Q_168', '2018-09-28 01:38:59'),
(169, 'Q_169', '2018-09-28 01:39:03'),
(170, 'Q_170', '2018-09-28 01:39:10'),
(171, 'Q_171', '2018-09-28 01:39:14'),
(172, 'Q_172', '2018-09-28 01:39:17'),
(173, 'Q_173', '2018-09-28 01:39:23'),
(174, 'Q_174', '2018-09-28 01:39:27'),
(175, 'Q_175', '2018-09-28 01:42:43'),
(176, 'Q_176', '2018-09-28 01:42:47'),
(177, 'Q_177', '2018-09-28 01:42:52'),
(178, 'Q_178', '2018-09-28 01:53:21'),
(179, 'Q_179', '2018-09-28 01:53:24'),
(180, 'Q_180', '2018-09-28 01:53:28'),
(181, 'Q_181', '2018-09-28 01:53:31'),
(182, 'Q_182', '2018-09-28 01:54:31'),
(183, 'Q_183', '2018-09-28 01:54:35');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accept_list`
--
ALTER TABLE `accept_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `reject_list`
--
ALTER TABLE `reject_list`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accept_list`
--
ALTER TABLE `accept_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `reject_list`
--
ALTER TABLE `reject_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=184;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

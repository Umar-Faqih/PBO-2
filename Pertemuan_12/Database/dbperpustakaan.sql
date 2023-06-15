-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2023 at 02:29 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbperpustakaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `id_anggota` int(11) NOT NULL,
  `kode_anggota` varchar(10) NOT NULL,
  `nama_anggota` varchar(100) NOT NULL,
  `jk_anggota` enum('L','P') NOT NULL DEFAULT 'L',
  `prodi_anggota` enum('TIF','IND','PET') NOT NULL DEFAULT 'TIF',
  `alamat_anggota` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`id_anggota`, `kode_anggota`, `nama_anggota`, `jk_anggota`, `prodi_anggota`, `alamat_anggota`) VALUES
(1, '1001', 'Umar Faqih', 'L', 'TIF', 'Ds. Damarguna Kec. Ciledug Kab. Cirebon'),
(6, '1002', 'Wahyudi', 'L', 'TIF', 'Kec. Sumber Kab. Cirebon');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `id_buku` int(11) NOT NULL,
  `kode_buku` varchar(11) NOT NULL,
  `judul_buku` varchar(50) NOT NULL,
  `penulis_buku` varchar(50) NOT NULL,
  `penerbit_buku` varchar(50) NOT NULL,
  `tahun_terbit` varchar(50) NOT NULL,
  `genre` enum('komedi','pengetahuan','fantasi','sains') NOT NULL DEFAULT 'komedi'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id_buku`, `kode_buku`, `judul_buku`, `penulis_buku`, `penerbit_buku`, `tahun_terbit`, `genre`) VALUES
(1, '1000', 'Si Kancil', 'Steven Age', 'Sinar Media', '2010', 'fantasi');

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman`
--

CREATE TABLE `peminjaman` (
  `id_peminjaman` int(11) NOT NULL,
  `kode_pinjam` varchar(11) NOT NULL,
  `tgl_pinjam` varchar(10) NOT NULL,
  `tgl_kembali` varchar(10) NOT NULL,
  `kode_buku` int(11) NOT NULL,
  `kode_anggota` int(11) NOT NULL,
  `kode_petugas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `peminjaman`
--

INSERT INTO `peminjaman` (`id_peminjaman`, `kode_pinjam`, `tgl_pinjam`, `tgl_kembali`, `kode_buku`, `kode_anggota`, `kode_petugas`) VALUES
(2, '0001', '2023-06-08', '2023-06-11', 1001, 1000, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `pengembalian`
--

CREATE TABLE `pengembalian` (
  `id_pengembalian` int(11) NOT NULL,
  `kode_pengembalian` varchar(11) NOT NULL,
  `tgl_pengembalian` varchar(10) NOT NULL,
  `kode_buku` int(11) NOT NULL,
  `kode_anggota` int(11) NOT NULL,
  `kode_petugas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pengembalian`
--

INSERT INTO `pengembalian` (`id_pengembalian`, `kode_pengembalian`, `tgl_pengembalian`, `kode_buku`, `kode_anggota`, `kode_petugas`) VALUES
(1, '1001', '2023-06-11', 1001, 1000, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `petugas`
--

CREATE TABLE `petugas` (
  `id_petugas` int(11) NOT NULL,
  `kode_petugas` int(11) NOT NULL,
  `nama_petugas` varchar(50) NOT NULL,
  `jabatan_petugas` enum('Admin','Kepala Perpus','Ob','Kasir') NOT NULL DEFAULT 'Admin'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `petugas`
--

INSERT INTO `petugas` (`id_petugas`, `kode_petugas`, `nama_petugas`, `jabatan_petugas`) VALUES
(1, 1111, 'Umar Faqih', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`id_anggota`),
  ADD UNIQUE KEY `unik` (`kode_anggota`) USING BTREE;

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id_buku`),
  ADD UNIQUE KEY `unik` (`kode_buku`);

--
-- Indexes for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD PRIMARY KEY (`id_peminjaman`),
  ADD UNIQUE KEY `unik` (`kode_pinjam`),
  ADD KEY `id_buku` (`kode_buku`),
  ADD KEY `id_anggota` (`kode_anggota`),
  ADD KEY `id_petugas` (`kode_petugas`);

--
-- Indexes for table `pengembalian`
--
ALTER TABLE `pengembalian`
  ADD PRIMARY KEY (`id_pengembalian`),
  ADD UNIQUE KEY `unik` (`kode_pengembalian`),
  ADD KEY `id_buku` (`kode_buku`),
  ADD KEY `id_anggota` (`kode_anggota`),
  ADD KEY `id_petugas` (`kode_petugas`);

--
-- Indexes for table `petugas`
--
ALTER TABLE `petugas`
  ADD PRIMARY KEY (`id_petugas`),
  ADD UNIQUE KEY `unik` (`kode_petugas`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anggota`
--
ALTER TABLE `anggota`
  MODIFY `id_anggota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `id_buku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `peminjaman`
--
ALTER TABLE `peminjaman`
  MODIFY `id_peminjaman` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pengembalian`
--
ALTER TABLE `pengembalian`
  MODIFY `id_pengembalian` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `petugas`
--
ALTER TABLE `petugas`
  MODIFY `id_petugas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

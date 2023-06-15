<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $kode_pinjam = "";
    public $tgl_pinjam = "";
    public $tgl_kembali = "";
    public $kode_buku = "";
    public $kode_anggota = "";
    public $kode_petugas = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kode_pinjam(int $kode_pinjam)
    {
        $query = "SELECT * FROM $this->table WHERE kode_pinjam = $kode_pinjam";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_pinjam`,`tgl_pinjam`,`tgl_kembali`,`kode_buku`,`kode_anggota`,`kode_petugas`) VALUES ('$this->kode_pinjam','$this->tgl_pinjam','$this->tgl_kembali','$this->kode_buku','$this->kode_anggota','$this->kode_petugas')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_pinjam = '$this->kode_pinjam', tgl_pinjam = '$this->tgl_pinjam', tgl_kembali = '$this->tgl_kembali', kode_buku = '$this->kode_buku', kode_anggota = '$this->kode_anggota', kode_petugas = '$this->kode_petugas' 
        WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_pinjam($kode_pinjam): int
    {
        $query = "UPDATE $this->table SET kode_pinjam = '$this->kode_pinjam', tgl_pinjam = '$this->tgl_pinjam', tgl_kembali = '$this->tgl_kembali', kode_buku = '$this->kode_buku', kode_anggota = '$this->kode_anggota', kode_petugas = '$this->kode_petugas' 
        WHERE kode_pinjam = $kode_pinjam";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_pinjam($kode_pinjam): int
    {
        $query = "DELETE FROM $this->table WHERE kode_pinjam = $kode_pinjam";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
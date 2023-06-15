<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
$id=0;
$kode_pinjam=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_pinjam'])){
            $kode_pinjam = $_GET['kode_pinjam'];
        }
        if($id>0){    
            $result = $peminjaman->get_by_id($id);
        }elseif($kode_pinjam>0){
            $result = $peminjaman->get_by_kode_pinjam($kode_pinjam);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->kode_pinjam = $_POST['kode_pinjam'];
        $peminjaman->tgl_pinjam = $_POST['tgl_pinjam'];
        $peminjaman->tgl_kembali = $_POST['tgl_kembali'];
        $peminjaman->kode_buku = $_POST['kode_buku'];
        $peminjaman->kode_anggota = $_POST['kode_anggota'];
        $peminjaman->kode_petugas = $_POST['kode_petugas'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_pinjam'])){
            $kode_pinjam = $_GET['kode_pinjam'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $peminjaman->kode_pinjam = $_PUT['kode_pinjam'];
        $peminjaman->tgl_pinjam = $_PUT['tgl_pinjam'];
        $peminjaman->tgl_kembali = $_PUT['tgl_kembali'];
        $peminjaman->kode_buku = $_PUT['kode_buku'];
        $peminjaman->kode_anggota = $_PUT['kode_anggota'];
        $peminjaman->kode_petugas = $_PUT['kode_petugas'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($kode_pinjam<>""){
            $peminjaman->update_by_kode_pinjam($kode_pinjam);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_pinjam'])){
            $kode_pinjam = $_GET['kode_pinjam'];
        }
        if($id>0){    
            $peminjaman->delete($id);
        }elseif($kode_pinjam>0){
            $peminjaman->delete_by_kode_pinjam($kode_pinjam);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>
# List buku
buku = [
    {
        "no_isbn": "978-1234567890",
        "judul": "Pemrograman Python",
        "pengarang": "John Doe",
        "isihalaman": 350,
        "deskripsi": "Buku tentang pemrograman Python.",
        "stok": 10,
        "booked": 0
    },
    # Tambahkan buku lainnya di sini
]

# List mahasiswa
mahasiswa = [
    {
        "nama": "Alice",
        "nim": "123456",
        "nomerhp": "081234567890",
        "alamat": "Jl. Mawar No. 1"
    },
    # Tambahkan mahasiswa lainnya di sini
]

# List peminjam
peminjam = [
    {
        "nim": "123456",
        "no_isbn": "978-1234567890",
        "tanggalpinjam": "2024-05-01",
        "tanggal_kembali": "2024-05-10",
        "status": "dipinjam"
    },
    # Tambahkan peminjaman lainnya di sini
]

# Fungsi untuk menambah buku
def tambah_buku(no_isbn, judul, pengarang, isihalaman, deskripsi, stok):
    buku.append({
        "no_isbn": no_isbn,
        "judul": judul,
        "pengarang": pengarang,
        "isihalaman": isihalaman,
        "deskripsi": deskripsi,
        "stok": stok,
        "booked": 0
    })

# Fungsi untuk menambah mahasiswa
def tambah_mahasiswa(nama, nim, nomerhp, alamat):
    mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "nomerhp": nomerhp,
        "alamat": alamat
    })

# Fungsi untuk menambah peminjaman
def tambah_peminjaman(nim, no_isbn, tanggalpinjam, tanggal_kembali):
    # Cek stok buku
    for buku_item in buku:
        if buku_item["no_isbn"] == no_isbn:
            if buku_item["stok"] > buku_item["booked"]:
                buku_item["booked"] += 1
                peminjam.append({
                    "nim": nim,
                    "no_isbn": no_isbn,
                    "tanggalpinjam": tanggalpinjam,
                    "tanggal_kembali": tanggal_kembali,
                    "status": "dipinjam"
                })
                return "Peminjaman berhasil."
            else:
                return "Stok buku habis."
    return "Buku tidak ditemukan."

# Fungsi untuk mengembalikan buku
def kembalikan_buku(nim, no_isbn):
    for peminjam_item in peminjam:
        if peminjam_item["nim"] == nim and peminjam_item["no_isbn"] == no_isbn and peminjam_item["status"] == "dipinjam":
            peminjam_item["status"] = "dikembalikan"
            for buku_item in buku:
                if buku_item["no_isbn"] == no_isbn:
                    buku_item["booked"] -= 1
            return "Pengembalian berhasil."
    return "Data peminjaman tidak ditemukan."

# Fungsi untuk melihat daftar buku
def lihat_buku():
    return buku

# Fungsi untuk melihat daftar mahasiswa
def lihat_mahasiswa():
    return mahasiswa

# Fungsi untuk melihat daftar peminjaman
def lihat_peminjaman():
    return peminjam

# Contoh penggunaan
tambah_buku("978-1234567891", "Belajar Data Science", "Jane Doe", 400, "Buku tentang data science.", 5)
tambah_mahasiswa("Bob", "654321", "081298765432", "Jl. Melati No. 2")
print(tambah_peminjaman("123456", "978-1234567891", "2024-05-24", "2024-06-01"))
print(kembalikan_buku("123456", "978-1234567891"))

print("Daftar Buku:", lihat_buku())
print("Daftar Mahasiswa:", lihat_mahasiswa())
print("Daftar Peminjaman:", lihat_peminjaman())

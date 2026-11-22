from exceptions import KapasitasPenuhError
from konten import Konten, Kuis
from pengguna import Instruktur, Mahasiswa, User


def daftarkan(course, mahasiswa):
    """Mendaftarkan mahasiswa; mencatat log lalu melempar ulang (re-raise)."""
    try:
        course.daftar(mahasiswa)
    except KapasitasPenuhError as e:
        print(f"[LOG] pendaftaran {mahasiswa.nama} gagal: {e}")
        raise


if __name__ == "__main__":
    dosen = Instruktur("I01", "Dr. Sari", "sari@kampus.ac.id", "Python")
    budi = Mahasiswa("2301", "Budi", "budi@mail.com")
    ani = Mahasiswa.dari_string("2302;Ani;ani@mail.com")
    print(dosen)
    print(budi)

    course = dosen.buat_course("PBO-01", "Pemrograman Berorientasi Objek", 2)
    modul = course.tambah_modul("Dasar OOP")
    modul.tambah_video("Pengenalan Class", 12)
    modul.tambah_kuis("Kuis Class", 10, 70)
    modul.tambah_tugas("Tugas Inheritance", "2026-11-10", 75)
    for k in course.semua_konten():
        print(k)

    course.daftar(budi)
    course.daftar(ani)
    print(course)
    try:
        course.daftar(Mahasiswa("2303", "Caca", "caca@mail.com"))
    except ValueError as e:
        print("Gagal:", e)

    try:
        course.kapasitas = -5
    except ValueError as e:
        print("Gagal:", e)

    p_video, p_kuis, p_tugas = budi.daftar_progres
    p_video.selesaikan()
    p_kuis.selesaikan(85)
    try:
        p_tugas.nilai = 150
    except ValueError as e:
        print("Gagal:", e)
    p_tugas.selesaikan(60)
    for p in budi.daftar_progres:
        print(p)
    print(f"Progres Budi: {course.persentase_selesai(budi):.1f}%")

    budi_lagi = Mahasiswa.dari_string("2301;Budi;budi@mail.com")
    print(budi == budi_lagi, budi == ani)
    print("Jumlah user:", User.jumlah_user, "| Jumlah konten:", Konten.jumlah_konten)
    print([c.__name__ for c in Kuis.__mro__])
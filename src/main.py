from exceptions import KapasitasPenuhError, LMSError
from konten import Konten
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

    # ---- Skenario 1 (berhasil): buat course, daftar, selesaikan konten ----
    print("=== Skenario 1: alur normal ===")
    try:
        course = dosen.buat_course("PBO-01", "Pemrograman Berorientasi Objek", 2)
        modul = dosen.tambah_modul(course, "Dasar OOP")
        video = modul.tambah_video("Pengenalan Class", 12)
        kuis = modul.tambah_kuis("Kuis Class", 10, 70)
        tugas = modul.tambah_tugas("Tugas Inheritance", "2026-11-10", 75)
        daftarkan(course, budi)
        daftarkan(course, ani)
        course.selesaikan_konten(budi, video)
        course.selesaikan_konten(budi, kuis, 85)
    except LMSError as e:
        print("Gagal:", e)
    else:
        print(course)
        print(f"Progres Budi: {course.persentase_selesai(budi):.1f}%")
    finally:
        print("[LOG] skenario 1 selesai")
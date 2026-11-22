from exceptions import (AksesDitolakError, DataTidakValidError, KapasitasPenuhError, LMSError, NilaiDiperlukanError, SudahTerdaftarError)
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

    # ---- Skenario 2 (gagal): kapasitas penuh dan pendaftaran ganda (EAFP) ----
    print("\n=== Skenario 2: aturan pendaftaran ===")
    caca = Mahasiswa("2303", "Caca", "caca@mail.com")
    for mhs in (caca, budi):
        try:                                   # EAFP: coba dulu, tangani jika gagal
            daftarkan(course, mhs)
        except KapasitasPenuhError as e:       # paling spesifik
            print(f"Ditolak ({e.kode_course}, kapasitas {e.kapasitas}): {e}")
        except SudahTerdaftarError as e:
            print("Ditolak:", e)
        except LMSError as e:                  # paling umum
            print("Kesalahan LMS:", e)
        else:
            print(mhs.nama, "berhasil mendaftar")
        finally:
            print(f"[LOG] pemrosesan pendaftaran {mhs.nama} selesai")

    # ---- Skenario 3 (gagal): data tidak valid pada setter ----
    print("\n=== Skenario 3: validasi data ===")
    percobaan = [
        ("kapasitas -5", lambda: setattr(course, "kapasitas", -5)),
        ("nilai tugas 150", lambda: course.selesaikan_konten(budi, tugas, 150)),
        ("nilai tugas 'A'", lambda: course.selesaikan_konten(budi, tugas, "A")),
        ("format data salah", lambda: Mahasiswa.dari_string("2304;Dewi")),
    ]
    for nama, aksi in percobaan:
        try:
            aksi()
        except DataTidakValidError as e:
            sebab = f" (penyebab: {type(e.__cause__).__name__})" if e.__cause__ else ""
            print(f"[{nama}] DataTidakValidError field={e.field}: {e}{sebab}")
        except TypeError as e:
            print(f"[{nama}] TypeError: {e}")

    # ---- Skenario 4 (gagal): aturan bisnis lain ----
    print("\n=== Skenario 4: aturan bisnis lain ===")
    dosen_lain = Instruktur("I02", "Pak Adi", "adi@kampus.ac.id", "Basis Data")
    for nama, aksi in [
        ("modul oleh instruktur lain", lambda: dosen_lain.tambah_modul(course, "Modul Liar")),
        ("kuis tanpa nilai", lambda: course.selesaikan_konten(budi, kuis)),
    ]:
        try:
            aksi()
        except AksesDitolakError as e:
            print(f"[{nama}] Ditolak: {e}")
        except NilaiDiperlukanError as e:
            print(f"[{nama}] Ditolak: {e}")

    print("\nJumlah user:", User.jumlah_user, "| Jumlah konten:", Konten.jumlah_konten)
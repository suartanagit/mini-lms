class LMSError(Exception):
    """Base exception untuk seluruh kesalahan aplikasi Mini LMS."""


class DataTidakValidError(LMSError, ValueError):
    """Data yang diisikan ke atribut tidak memenuhi aturan validasi."""

    def __init__(self, field, nilai, alasan):
        self.field = field
        self.nilai = nilai
        self.alasan = alasan
        super().__init__(f"{field} tidak valid ({nilai!r}): {alasan}")


class KapasitasPenuhError(LMSError):
    """Course sudah mencapai kapasitas maksimal peserta."""

    def __init__(self, kode_course, kapasitas):
        self.kode_course = kode_course
        self.kapasitas = kapasitas
        super().__init__(f"Course {kode_course} penuh (kapasitas {kapasitas} peserta)")


class SudahTerdaftarError(LMSError):
    """Mahasiswa mencoba mendaftar ke course yang sama dua kali."""

    def __init__(self, kode_course, nim):
        self.kode_course = kode_course
        self.nim = nim
        super().__init__(f"Mahasiswa {nim} sudah terdaftar di course {kode_course}")


class BelumTerdaftarError(LMSError):
    """Mahasiswa belum terdaftar di course yang dituju."""

    def __init__(self, kode_course, nim):
        self.kode_course = kode_course
        self.nim = nim
        super().__init__(f"Mahasiswa {nim} belum terdaftar di course {kode_course}")
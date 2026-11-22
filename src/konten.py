class DapatDinilaiMixin:
    """Mixin: perilaku penilaian untuk konten yang punya nilai."""
    _nilai_lulus = 0

    @property
    def nilai_lulus(self):
        return self._nilai_lulus

    def lulus(self, nilai):
        return nilai >= self._nilai_lulus


class Konten:
    jumlah_konten = 0  # class attribute

    def __init__(self, judul):
        self.__judul = judul
        Konten.jumlah_konten += 1

    @property
    def judul(self):
        return self.__judul

    def deskripsi(self):
        return "Konten umum"

    def __str__(self):
        return f"{self.deskripsi()}: {self.judul}"


class Video(Konten):
    def __init__(self, judul, durasi_menit):
        super().__init__(judul)
        self.__durasi = 0
        self.durasi_menit = durasi_menit

    @property
    def durasi_menit(self):
        return self.__durasi

    @durasi_menit.setter
    def durasi_menit(self, nilai):
        if nilai <= 0:
            raise ValueError("Durasi video harus > 0 menit")
        self.__durasi = nilai

    def deskripsi(self):                  # override
        return f"Video ({self.durasi_menit} menit)"


class Kuis(DapatDinilaiMixin, Konten):
    def __init__(self, judul, jumlah_soal, nilai_lulus):
        super().__init__(judul)
        self._jumlah_soal = jumlah_soal
        self._nilai_lulus = nilai_lulus

    def deskripsi(self):                  # override
        return f"Kuis ({self._jumlah_soal} soal, lulus >= {self._nilai_lulus})"


class Tugas(DapatDinilaiMixin, Konten):
    def __init__(self, judul, deadline, nilai_lulus):
        super().__init__(judul)
        self._deadline = deadline
        self._nilai_lulus = nilai_lulus

    def deskripsi(self):                  # override
        return f"Tugas (deadline {self._deadline}, lulus >= {self._nilai_lulus})"
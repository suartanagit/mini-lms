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
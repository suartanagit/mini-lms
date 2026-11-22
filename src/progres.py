from konten import DapatDinilaiMixin


class Progres:
    def __init__(self, mahasiswa, konten):
        self._mahasiswa = mahasiswa               # association
        self._konten = konten                     # association
        self._status = "belum"
        self.__nilai = None

    @property
    def status(self):
        return self._status

    @property
    def konten(self):
        return self._konten

    @property
    def nilai(self):
        return self.__nilai

    @nilai.setter
    def nilai(self, nilai):
        if not 0 <= nilai <= 100:
            raise ValueError("Nilai harus 0-100")
        self.__nilai = nilai

    def selesaikan(self, nilai=None):
        if isinstance(self._konten, DapatDinilaiMixin):
            if nilai is None:
                raise ValueError("Konten ini memerlukan nilai")
            self.nilai = nilai
            self._status = "selesai" if self._konten.lulus(nilai) else "ulang"
        else:
            self._status = "selesai"

    def __str__(self):
        return f"{self._mahasiswa.nama} | {self._konten.judul} | {self._status} | nilai={self.nilai}"
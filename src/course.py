from modul import Modul
from progres import Progres


class Course:
    def __init__(self, kode, judul, kapasitas, instruktur):
        self._kode = kode
        self.__judul = judul
        self.__kapasitas = 0
        self.kapasitas = kapasitas
        self._instruktur = instruktur             # association (1)
        self._daftar_modul = [Modul("Pengantar")]  # composition: dibuat di constructor
        self._peserta = []                        # aggregation: Mahasiswa dari luar

    @property
    def kode(self):
        return self._kode

    @property
    def judul(self):
        return self.__judul

    @property
    def kapasitas(self):
        return self.__kapasitas

    @kapasitas.setter
    def kapasitas(self, nilai):
        if nilai <= 0:
            raise ValueError("Kapasitas harus > 0")
        if nilai < len(getattr(self, "_peserta", [])):
            raise ValueError("Kapasitas kurang dari jumlah peserta")
        self.__kapasitas = nilai

    @property
    def peserta(self):
        return list(self._peserta)

    def tambah_modul(self, judul):
        modul = Modul(judul)
        self._daftar_modul.append(modul)
        return modul

    def semua_konten(self):
        return [k for m in self._daftar_modul for k in m.daftar_konten]
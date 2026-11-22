from exceptions import (BelumTerdaftarError, DataTidakValidError, KapasitasPenuhError, KontenTidakDitemukanError, SudahTerdaftarError)
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
        if not isinstance(nilai, int):
            raise TypeError("Kapasitas harus berupa bilangan bulat")
        if nilai <= 0:
            raise DataTidakValidError("kapasitas", nilai, "harus lebih dari 0")
        if nilai < len(getattr(self, "_peserta", [])):
            raise DataTidakValidError("kapasitas", nilai, "kurang dari jumlah peserta saat ini")
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

    def daftar(self, mahasiswa):
        if mahasiswa in self._peserta:            # memakai __eq__
            raise SudahTerdaftarError(self._kode, mahasiswa.nim)
        if len(self._peserta) >= self.__kapasitas:
            raise KapasitasPenuhError(self._kode, self.__kapasitas)
        self._peserta.append(mahasiswa)
        for konten in self.semua_konten():
            mahasiswa.tambah_progres(Progres(mahasiswa, konten))

    def selesaikan_konten(self, mahasiswa, konten, nilai=None):
        if mahasiswa not in self._peserta:
            raise BelumTerdaftarError(self._kode, mahasiswa.nim)
        for progres in mahasiswa.daftar_progres:
            if progres.konten is konten:
                progres.selesaikan(nilai)
                return progres
        raise KontenTidakDitemukanError(self._kode, konten.judul)

    def persentase_selesai(self, mahasiswa):
        if mahasiswa not in self._peserta:
            raise BelumTerdaftarError(self._kode, mahasiswa.nim)
        total = len(self.semua_konten())
        selesai = sum(1 for p in mahasiswa.daftar_progres if p.status == "selesai")
        return 100 * selesai / total if total else 0

    def __eq__(self, lain):
        return isinstance(lain, Course) and self._kode == lain._kode

    def __hash__(self):
        return hash(self._kode)

    def __str__(self):
        return f"Course {self._kode} - {self.judul} ({len(self._peserta)}/{self.kapasitas})"
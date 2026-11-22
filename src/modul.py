from konten import Video, Kuis, Tugas


class Modul:
    def __init__(self, judul):
        self.__judul = judul
        self._daftar_konten = []          # composition: Konten dibuat di dalam Modul

    @property
    def judul(self):
        return self.__judul

    @property
    def daftar_konten(self):
        return list(self._daftar_konten)

    def tambah_video(self, judul, durasi):
        konten = Video(judul, durasi)
        self._daftar_konten.append(konten)
        return konten

    def tambah_kuis(self, judul, jumlah_soal, nilai_lulus):
        konten = Kuis(judul, jumlah_soal, nilai_lulus)
        self._daftar_konten.append(konten)
        return konten

    def tambah_tugas(self, judul, deadline, nilai_lulus):
        konten = Tugas(judul, deadline, nilai_lulus)
        self._daftar_konten.append(konten)
        return konten
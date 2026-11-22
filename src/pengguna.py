from course import Course

class User:
    jumlah_user = 0  # class attribute: penghitung seluruh user

    def __init__(self, id_user, nama, email):
        self._id_user = id_user
        self.__nama = None
        self.__email = None
        self.nama = nama      # lewat setter (validasi)
        self.email = email    # lewat setter (validasi)
        User.jumlah_user += 1

    @property
    def id_user(self):
        return self._id_user

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nilai):
        if not nilai or not nilai.strip():
            raise ValueError("Nama tidak boleh kosong")
        self.__nama = nilai.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nilai):
        if not User.validasi_email(nilai):
            raise ValueError(f"Email tidak valid: {nilai}")
        self.__email = nilai

    @staticmethod
    def validasi_email(email):
        return "@" in email and "." in email.split("@")[-1]

    def peran(self):
        return "User"

    def __str__(self):
        return f"[{self.peran()}] {self.nama} <{self.email}>"


class Instruktur(User):
    def __init__(self, id_user, nama, email, keahlian):
        super().__init__(id_user, nama, email)
        self._keahlian = keahlian
        self._daftar_course = []          # association ke Course

    def peran(self):                      # override
        return "Instruktur"

    def buat_course(self, kode, judul, kapasitas):
        course = Course(kode, judul, kapasitas, self)
        self._daftar_course.append(course)
        return course


class Mahasiswa(User):
    def __init__(self, nim, nama, email):
        super().__init__(nim, nama, email)
        self._daftar_progres = []         # association ke Progres

    @property
    def nim(self):
        return self._id_user

    @property
    def daftar_progres(self):
        return list(self._daftar_progres)

    def peran(self):                      # override
        return "Mahasiswa"

    @classmethod
    def dari_string(cls, data):           # alternative constructor
        nim, nama, email = data.split(";")
        return cls(nim, nama, email)

    def tambah_progres(self, progres):
        self._daftar_progres.append(progres)

    def __eq__(self, lain):
        return isinstance(lain, Mahasiswa) and self.nim == lain.nim

    def __hash__(self):
        return hash(self.nim)

    def __repr__(self):
        return f"Mahasiswa(nim={self.nim!r}, nama={self.nama!r})"
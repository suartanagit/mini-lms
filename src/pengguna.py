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
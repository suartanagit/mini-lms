class LMSError(Exception):
    """Base exception untuk seluruh kesalahan aplikasi Mini LMS."""


class DataTidakValidError(LMSError, ValueError):
    """Data yang diisikan ke atribut tidak memenuhi aturan validasi."""

    def __init__(self, field, nilai, alasan):
        self.field = field
        self.nilai = nilai
        self.alasan = alasan
        super().__init__(f"{field} tidak valid ({nilai!r}): {alasan}")
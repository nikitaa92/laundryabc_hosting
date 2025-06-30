from django.db import models

class PaketLaundry(models.Model):
    kode_paket = models.CharField(max_length=5)  # A, B, C
    nama_paket = models.CharField(max_length=100)
    layanan = models.TextField()
    harga = models.IntegerField()

    def __str__(self):
        return f"{self.kode_paket} - {self.nama_paket}"

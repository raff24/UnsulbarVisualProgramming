class Mahasiswa:
  def __init__(self, nama, umur, alamat):
      self.nama = nama
      self.umur = umur
      self.alamat = alamat
p1 = Mahasiswa('Rafli','21','Majene')
#Untuk Mengakses class diatas caranya sebagai berikut:
print(p1.nama)
print(p1.umur)
print(p1.alamat)
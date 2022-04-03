class data():
    __barang = 500 # private
 
    def __init__(self, nama_barang):
        self.nama = nama_barang
 
    def harga_barang(self,harga_barang):
       hasil = self.__barang * harga_barang
       return hasil
 
produk = data("Tiket Chelsea Vs Manchester United")
print(produk.__dict__)
print(produk.harga_barang(90000))

# src/data/preprocess.py
import pandas as pd

def preprocess_data(self):
    """Fungsi untuk memproses data sebelum digunakan dalam model."""
    
    
    # Sesuaikan dengan kolom yang ingin digunakan untuk model
    columns_to_drop = ['id', 'lokasi', 'sertifikat', 'tipeProperti', 'garasi', 'aksesJalan', 'fasilitasUmum',]
    self = self.drop(columns=columns_to_drop, errors='ignore')

    # Menghapus satuan (seperti "m²") dan mengkonversi menjadi angka
    self['luasTanah'] = self['luasTanah'].replace({r'[^\d.]': ''}, regex=True).astype(float)
    self['kamarTidur'] = self['kamarTidur'].astype(float)
    self['jumlahKamarMandi'] = self['jumlahKamarMandi'].astype(float)
    self['lantai'] = self['lantai'].astype(float)
    self['jarakkePusatKota'] = self['jarakkePusatKota'].replace({r'[^\d.]': ''}, regex=True).astype(float)
    self['dayaListrik'] = self['dayaListrik'].replace({r'[^\d.]': ''}, regex=True).astype(float)
    self['tahunBangun'] = self['tahunBangun'].astype(float)
    self['harga'] = self['harga'].replace({r'[^\d.]': '', r'\.': ''}, regex=True).astype(float)

    # Menghapus baris dengan nilai kosong
    self = self.dropna()

    # Misalnya, kita ingin harga properti yang realistis antara 100 juta sampai 10 miliar
    self = self[(self['harga'] >= 100000000) & (self['harga'] <= 10000000000)]


    return self


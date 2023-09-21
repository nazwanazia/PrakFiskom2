#Cahaya merambat dengan kelajuan c = 3*10^8 m/s, berapa waktu yang dibutuhkan cahaya untuk bergerak dari matahari ke bumi yang berjarak 1,5*10^11 m? 
#jarak dari matahari ke bumi dalam satuan meter
s = 1.5e11 #1,5*10^11 meter
#kecepatan cahaya dalam m/s
c = 3e8
#waktu yang dibutuhkan untuk cahaya untuk mencapai bumi dari matahari
t = s / c

#konversi satuan detik ke menit
menit = t / 60

#konversi satuan detik ke jam
jam = t / 3600

#menampilkan hasil perhitungan
print(f"Waktu yang dibutuhkan cahaya dari Matahari ke Bumi adalah {t} detik")
print(f"Atau sekitar {menit} menit")
print(f"Atau sekitar {jam} jam")

#berapa waktu yang dibutuhkan cahaya untuk bergerak dari bulan ke bumi yang berjarak 3,84*10^8 m?

#jarak dari bulan ke bumi dalam satuan meter
s_1 = 3.84e8
#waktu yang dibutuhkan cahaya untuk mencapai bumi dari bulan
t_1 = s_1 / c

#konversi satuan detik ke menit
menit_1 = t_1 / 60

#konversi satuan detik ke jam
jam_1 = t_1 / 3600

#menampilkan hasil perhitungan
print(f"Waktu yang dibutuhkan cahaya dari Bulan ke Bumi adalah {t_1} detik")
print(f"Atau sekitar {menit_1} menit")
print(f"Atau sekitar {jam_1} jam")

print("sumber https://rosyidadrianto.files.wordpress.com/2009/10/solusi-bab-iv-dan-bab-v1.pdf")

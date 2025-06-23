# Impor library yang dibutuhkan: Flask, render_template (untuk HTML), request (untuk form)
from flask import Flask, render_template, request

app = Flask(__name__)

# =======================================================
# KRITERIA 4: FUNCTIONAL (FUNGSI)
# Kita membuat fungsi khusus untuk logika konversi agar kode lebih rapi dan bisa dipakai ulang.
# =======================================================
def konversi_suhu(nilai, unit_asal):
    """Fungsi ini menerima nilai suhu dan unit asalnya, lalu mengembalikan hasil konversi."""
    
    # =======================================================
    # KRITERIA 2: SELECTION (SELEKSI / KONDISIONAL)
    # Menggunakan if/elif untuk menentukan rumus mana yang harus dijalankan.
    # =======================================================
    if unit_asal == 'celsius':
        # Rumus Celsius ke Fahrenheit
        hasil_konversi = (nilai * 9/5) + 32
        return f"{nilai}°C sama dengan {round(hasil_konversi, 2)}°F"
    elif unit_asal == 'fahrenheit':
        # Rumus Fahrenheit ke Celsius
        hasil_konversi = (nilai - 32) * 5/9
        return f"{nilai}°F sama dengan {round(hasil_konversi, 2)}°C"
    else:
        return "Unit tidak valid"

# Rute utama untuk halaman web kita
@app.route('/', methods=['GET', 'POST'])
def halaman_utama():
    hasil_akhir = None
    
    # =======================================================
    # KRITERIA 1: SEQUENCE (URUTAN)
    # Urutan eksekusi jika pengguna mengirimkan form (method POST).
    # =======================================================
    if request.method == 'POST':
        # 1. Ambil data dari form
        try:
            nilai_suhu = float(request.form['suhu'])
            unit = request.form['unit']
            
            # 2. Proses data dengan memanggil fungsi yang sudah kita buat
            hasil_akhir = konversi_suhu(nilai_suhu, unit)
        except ValueError:
            # Seleksi sederhana untuk error handling jika input bukan angka
            hasil_akhir = "Input tidak valid. Harap masukkan hanya angka."
            
    # 3. Tampilkan halaman HTML, kirim hasil konversi jika ada
    return render_template('index.html', hasil=hasil_akhir)


# =======================================================
# KRITERIA 3: ITERATION (PERULANGAN)
# Kita membuat halaman baru khusus untuk menunjukkan contoh perulangan (loop).
# =======================================================
@app.route('/tabel')
def halaman_tabel():
    data_tabel = []
    # Menggunakan for loop untuk membuat data dari 0 sampai 10
    for c in range(11):
        f = (c * 9/5) + 32
        data_tabel.append({'celsius': c, 'fahrenheit': round(f, 2)})
        
    return render_template('tabel.html', data=data_tabel)


# File HTML untuk halaman tabel
# Buat file baru bernama `tabel.html` di dalam folder `templates`
if __name__ == '__main__':
    app.run(debug=True)
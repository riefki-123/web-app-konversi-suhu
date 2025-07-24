# Impor library yang dibutuhkan: Flask, render_template (untuk HTML), request (untuk form)
from flask import Flask, render_template, request

app = Flask(__name__)

def konversi_suhu(nilai, unit_asal):
    """Fungsi ini menerima nilai suhu dan unit asalnya, lalu mengembalikan hasil konversi."""
    
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
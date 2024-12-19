from flask import Flask, render_template, request

app = Flask(__name__)

# Örnek sözlük (key-value yapısı)
ogrenci_verisi = {
    "123": {"ad": "Ahmet", "soyad": "Yılmaz", "yas": 20, "bolum": "Bilgisayar Mühendisliği"},
    "124": {"ad": "Mehmet", "soyad": "Kara", "yas": 22, "bolum": "Elektrik Mühendisliği"},
    "125": {"ad": "Ayşe", "soyad": "Demir", "yas": 19, "bolum": "Makine Mühendisliği"},
}

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Öğrenci bilgilerini arama sayfası
@app.route('/ara', methods=['POST'])
def ara():
    numara = request.form['numara']  # Kullanıcıdan gelen öğrenci numarası

    # Sözlükte anahtar var mı kontrol et
    if numara in ogrenci_verisi:
        ogrenci = ogrenci_verisi[numara]  # Anahtara karşılık gelen değeri al
        return render_template('sonuc.html', ogrenci=ogrenci, numara=numara)
    else:
        return render_template('sonuc.html', mesaj="Öğrenci bulunamadı.")

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

# Örnek kullanıcı verisi (gerçek uygulamada veritabanından veya oturumdan alınmalı)
kullanici_bilgisi = {'ad_soyad': 'Kullanıcı Adı Soyadı', 'email': 'kullanici@example.com', 'telefon': '05xx xxx xx xx'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin/giris')
def admin_giris():
    return render_template('admin_giris.html')

@app.route('/admin/panel')
def admin_paneli():
    return render_template('admin_paneli.html')

@app.route('/arac/ekle')
def arac_ekle():
    return render_template('arac_ekle.html')

@app.route('/arac/liste')
def arac_liste():
    return render_template('arac_liste.html')

@app.route('/ayarlar')
def ayarlar():
    return render_template('ayarlar.html')

@app.route('/giris')
def giris():
    return render_template('giris.html')

@app.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html')

@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

@app.route('/kayit')
def kayit():
    return render_template('kayit.html')

@app.route('/profil')
def profil():
    return render_template('profil.html', kullanici=kullanici_bilgisi)

@app.route('/rezervasyon/yap')
def rezervasyon():
    return render_template('rezervasyon.html')

@app.route('/rezervasyonlarim')
def rezervasyonlarim():
    return render_template('rezervasyonlarim.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

# Membuat instance Flask
app = Flask(__name__)

# Rute utama (/) yang menampilkan teks "Hello, Flask!"
@app.route("/")
def home():
    return "Hello, Flask!"

# Rute baru (/info) yang menampilkan teks "Ini adalah aplikasi Flask dasar."
@app.route("/info")
def info():
    return "Ini adalah aplikasi Flask dasar."

# Menjalankan aplikasi Flask
if __name__ == "__main__":
    app.run(debug=True)

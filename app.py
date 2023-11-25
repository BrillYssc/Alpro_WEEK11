from flask import Flask, request, jsonify
import random

app = Flask(__name__)

pesan_default = {
    "Spongebob":"Makan patty itu",
    "Patrick":"Berdansalah",
    "Squidward":"Ayo bermain",
    "Plankton":"Jangan bergerak",
    "Garfield":"Jangan minum dingin",
    "Sandy":"Berlatih karate",
    "Tuan Crabs":"Menghitung uang",
    "Pearl":"Jangan rakus",
    "Larry":"Nikmati liburan",
    "Garry":"Jangan nakal"
}

@app.route('/puja_kerang_ajaib', methods=['GET', 'POST'])
def puja_kerang_ajaib():
    if request.method == 'GET':
        nama = request.args.get('nama')
        if nama:
            pesan = f"{nama}, {pesan_default.get(random.choice(list(pesan_default.keys())), '')}"
        else:
            kunci_acak = random.choice(list(pesan_default.keys()))
            pesan = f"{pesan_default[kunci_acak]}, {kunci_acak}"

        return jsonify({'pesan': pesan})
    elif request.method == 'POST':
        nama = request.json.get('nama')
        if nama:
            pesan = f"Selamat datang, {nama}, anda berhasil masuk ke Puja Kerang Ajaib"
            return jsonify({'pesan': pesan})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)


db_config = {
    "host": "sansur.us-east-2.rds.amazonaws.com",
    "user": "admin",
    "password": "sifre"
}

def get_db_connection():
    try:
        return mysql.connector.connect(**db_config, database="personel_db")
    except mysql.connector.Error:
        return mysql.connector.connect(**db_config)


@app.route('/init-db', methods=['GET'])
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS personel_db")
    cursor.execute("USE personel_db")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personeller (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ad VARCHAR(100),
            soyad VARCHAR(100),
            departman VARCHAR(100)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mesaj": "AWS RDS uzerinde veritabani ve tablo basariyla olusturuldu!"})



@app.route('/', methods=['GET'])
def baslangic():
    return jsonify({"mesaj": "Backend API basariyla AWS RDS'e baglandi!", "durum": "aktif"})


@app.route('/personel', methods=['GET'])
def get_personel():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM personeller")
    personeller = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(personeller)


@app.route('/personel', methods=['POST'])
def add_personel():
    yeni_personel = request.get_json()
    ad = yeni_personel.get('ad')
    soyad = yeni_personel.get('soyad')
    departman = yeni_personel.get('departman')

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO personeller (ad, soyad, departman) VALUES (%s, %s, %s)"
    val = (ad, soyad, departman)
    cursor.execute(sql, val)
    conn.commit()
    
    yeni_id = cursor.lastrowid 
    cursor.close()
    conn.close()

    yeni_personel['id'] = yeni_id
    return jsonify({"mesaj": "Personel AWS veritabanına eklendi", "personel": yeni_personel}), 201


@app.route('/personel/<int:id>', methods=['DELETE'])
def delete_personel(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM personeller WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mesaj": f"ID {id} olan personel silindi"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

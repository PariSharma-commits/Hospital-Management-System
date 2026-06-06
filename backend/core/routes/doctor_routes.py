from flask import Blueprint, jsonify
from core.utils.db import get_db_connection

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/doctors', methods=['GET'])
def get_doctors():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM doctors;")
    doctors = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(doctors)
from flask import Blueprint, request, jsonify
from core.utils.db import get_db_connection

appointment_bp = Blueprint('appointment', __name__)


# BOOK APPOINTMENT
@appointment_bp.route('/book', methods=['POST'])
def book_appointment():
    data = request.json

    patient_id = data.get('patient_id')
    doctor_id = data.get('doctor_id')
    date = data.get('date')
    time = data.get('time')

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time)
            VALUES (%s, %s, %s, %s)
        """, (patient_id, doctor_id, date, time))

        conn.commit()

        return jsonify({"message": "Appointment booked ✅"})

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)})

    finally:
        cur.close()
        conn.close()


# GET ALL APPOINTMENTS (FIXED)
@appointment_bp.route('/appointments', methods=['GET'])
def get_appointments():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT a.id, p.name, d.name, a.appointment_date, a.appointment_time, a.status
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
        ORDER BY a.appointment_date, a.appointment_time;
    """)

    rows = cur.fetchall()

    # 🔥 FIX: convert date/time to string
    data = []
    for row in rows:
        data.append([
            row[0],              # id
            row[1],              # patient name
            row[2],              # doctor name
            str(row[3]),         # date → string
            str(row[4]),         # time → string
            row[5]               # status
        ])

    cur.close()
    conn.close()

    return jsonify(data)
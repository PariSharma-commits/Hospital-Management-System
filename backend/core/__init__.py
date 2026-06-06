from flask import Flask
from flask_cors import CORS
from core.routes.doctor_routes import doctor_bp
from core.routes.appointment_routes import appointment_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(appointment_bp)

    @app.route("/")
    def home():
        return {"message": "Backend running 🚀"}

    return app
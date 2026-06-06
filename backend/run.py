from core import create_app
from core.utils.db import get_db_connection

app = create_app()

if __name__ == "__main__":
    try:
        conn = get_db_connection()
        print("DB Connected ✅")
        conn.close()
    except Exception as e:
        print("DB Connection Failed ❌", e)

    app.run(debug=True)
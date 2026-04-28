import os
import psycopg2
import mysql.connector

# -----------------------------
# SWITCH MODE HERE
# -----------------------------
USE_CLOUD = False  # True = Supabase (online), False = XAMPP (local)

# -----------------------------
# LOCAL XAMPP CONFIG (MySQL)
# -----------------------------
LOCAL_DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "qr_attendance_db"
}

# -----------------------------
# CLOUD SUPABASE CONFIG (PostgreSQL)
# -----------------------------
DATABASE_URL = os.getenv("postgresql://postgres:JAJIcute_088@db.sukicuobulnensiggljg.supabase.co:5432/postgres")


# -----------------------------
# GET DATABASE CONNECTION
# -----------------------------
def get_db():
    if USE_CLOUD:
        # 🌐 CLOUD (Supabase / Render)
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    else:
        # 🏠 LOCAL (XAMPP)
        conn = mysql.connector.connect(**LOCAL_DB_CONFIG)
        return conn
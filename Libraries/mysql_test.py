import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="face_user",
    password="face123",
    database="face_attendance_system_2026"
)

print("✅ MySQL connected successfully via Python")
db.close()



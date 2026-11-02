import sqlite3
import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect('school.db')
    conn.row_factory = sqlite3.Row  # Чтобы обращаться к полям по именам, а не индексам
    return conn


def init_db():
    if os.path.exists("schema.sql"):
        with open("schema.sql", "r", encoding="utf-8") as f:
            sql_script = f.read()
        with get_db() as conn:
            conn.executescript(sql_script)


# --- МАРШРУТЫ ДЛЯ СТРАНИЦ ---
@app.route("/")
@app.route("/students")
def students_page():
    return render_template("students.html")


@app.route("/grades")
def grades_page():
    return render_template("grades.html")


@app.route("/stats")
def stats_page():
    with get_db() as conn:
        # 1. Средняя оценка каждого ученика за все время
        students_avg = conn.execute('''
            SELECT s.first_name, s.last_name, ROUND(AVG(g.grade), 2) as avg_grade
            FROM students s LEFT JOIN grades g ON s.id = g.student_id
            GROUP BY s.id
        ''').fetchall()

        # 2. Средняя недельная оценка каждого ученика
        # strftime('%W', ...) возвращает номер недели в году
        student_weekly = conn.execute('''
            SELECT s.first_name, s.last_name, strftime('%W', datetime(g.created_at, 'localtime')) as week, ROUND(AVG(g.grade), 2) as avg_grade
            FROM students s JOIN grades g ON s.id = g.student_id
            GROUP BY s.id, week ORDER BY week DESC
        ''').fetchall()

        # 3. Средняя оценка класса по неделям
        class_weekly = conn.execute('''
            SELECT strftime('%W', datetime(created_at, 'localtime')) as week, ROUND(AVG(grade), 2) as avg_grade
            FROM grades GROUP BY week ORDER BY week DESC
        ''').fetchall()

    return render_template("stats.html", students_avg=students_avg, student_weekly=student_weekly, class_weekly=class_weekly)


# --- API ЭНДПОИНТЫ ДЛЯ VUE.JS ---
@app.route("/api/students", methods=["GET", "POST"])
def api_students():
    conn = get_db()
    if request.method == "POST":
        data = request.json
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name) VALUES (?, ?)", (data['first_name'], data['last_name']))
        conn.commit()
        return jsonify({"id": cursor.lastrowid}), 201
    
    students = conn.execute("SELECT id, first_name, last_name FROM students").fetchall()

    return jsonify([dict(row) for row in students])


@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def api_delete_student(student_id):
    with get_db() as conn:
        conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.execute("DELETE FROM grades WHERE student_id = ?", (student_id,)) # Каскадное удаление оценок
    return jsonify({"success": True})


@app.route("/api/grades", methods=["POST"])
def api_add_grade():
    data = request.json
    with get_db() as conn:
        conn.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (data['student_id'], data['grade']))
    return jsonify({"success": True}), 201


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8000)

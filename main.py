# simple api with flask
from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "John Doe",
    },
    {
        "id": 2,
        "name": "Jane Doe",
    }
]

student_id_counter = len(students)

student_grades = [
    {
        "student_id": 1,
        "subject": "Math",
        "grade": 90
    },
    {
        "student_id": 2,
        "subject": "Science",
        "grade": 85
    },
    {
        "student_id": 2,
        "subject": "Math",
        "grade": 95
    }
]

def validate_student(data):
    if "name" not in data:
        return False, "Missing name"
    return True, None

def validate_grade(data):
    if "student_id" not in data or "subject" not in data or "grade" not in data:
        return False, "Missing student_id, subject, or grade"
    return True, None



# main entry point to api
@app.route("/", methods=["GET"])
def get():
    return jsonify({"message": "Welcome to the Student Grades API!"})

# get all students
@app.route("/students", methods=["GET"])
def get_students():
    result = []
    for student in students:
        grades = [
            {
                "subject": grade["subject"],
                "grade": grade["grade"]
            }
            for grade in student_grades
            if grade["student_id"] == student["id"]
        ]
        result.append({
            "id": student["id"],
            "name": student["name"],
            "grades": grades
        })

    return jsonify({"students": students, "grades": student_grades})

# get a student by id
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

# create a new student
@app.route("/students", methods=["POST"])
def add_student():
    global student_id_counter

    data = request.get_json()
    print(f"This is the data: {data}")

    if not data:
        return jsonify({"error": "No data provided"})

    valid, message = validate_student(data)
    if not valid:
        return jsonify({"error": message}), 400

    new_student = {
        "id": student_id_counter + 1,
        "name": data["name"]
    }

    students.append(new_student)
    student_id_counter += 1

    return jsonify(new_student), 201


# add a grade
@app.route("/student-grades", methods=["POST"])
def add_student_grade():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    valid, message = validate_grade(data)
    if not valid: 
        return jsonify({"error": message}), 400

    student_exists = any(student["id"] == data["student_id"] for student in students)
    if not student_exists:
        return jsonify({"error": "Student not found"}), 404

    new_grade = {
        "student_id": data["student_id"],
        "subject": data['subject'],
        "grade": data["grade"] 
    }

    student_grades.append(new_grade)

    return jsonify(new_grade), 201

if __name__ == "__main__":
    app.run(debug=True)
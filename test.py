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

]

def validate_student(data):
    if "name" not in data:
        return False, "Missing name"
    return True, None

def validate_student_grade(data):
    if "subject" not in data or "grade" not in data:
        return False, "Missing subject or grade"
    return True, None

def validate_grade(data):
    if "grade" not in data:
        return False, "Missing grade"
    return True, None

# main entry point to api
@app.route("/", methods=["GET"])
def get():
    return jsonify({"message": "Welcome to the Student Grades API!"})

# get all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify({"students": students})

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


if __name__ == "__main__":
    app.run(debug=True)
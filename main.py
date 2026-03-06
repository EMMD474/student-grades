from flask import Flask, request, jsonify

app = Flask(__name__)

# simple in-memory database
students = []
student_id_counter = 1


# Helper function for validation
def validate_student(data):
    if "name" not in data or "subject" not in data or "grade" not in data:
        return False, "Missing required fields"

    if not isinstance(data["grade"], int):
        return False, "Grade must be an integer"

    if data["grade"] < 0 or data["grade"] > 100:
        return False, "Grade must be between 0 and 100"

    return True, None


# GET all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


# GET student by ID
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    for student in students:
        if student["id"] == student_id:
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


# POST new student
@app.route("/students", methods=["POST"])
def add_student():
    global student_id_counter

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    valid, message = validate_student(data)

    if not valid:
        return jsonify({"error": message}), 400

    new_student = {
        "id": student_id_counter,
        "name": data["name"],
        "subject": data["subject"],
        "grade": data["grade"]
    }

    students.append(new_student)
    student_id_counter += 1

    return jsonify(new_student), 201


if __name__ == "__main__":
    app.run(debug=True)
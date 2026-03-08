from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Student Grades API", description="API for managing student grades", version="1.0.0")


students = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Doe"},
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

# Request models
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)

class GradeCreate(BaseModel):
    student_id: int
    subject: str = Field(..., min_length=1)
    grade: int = Field(..., ge=0, le=100)


# Response models
class GradeResponse(BaseModel):
    subject: str
    grade: int

class StudentRepsonse(BaseModel):
    id: int
    name: str
    grades: List[GradeResponse]

class StudentOnlyResponse(BaseModel):
    id: int
    name: str

def format_student(student: dict) -> dict:
    grades = [
        {
            "subject": grade["subject"],
            "grade": grade["grade"]
        }
        for grade in student_grades
        if grade["student_id"] == student["id"]
    ]
    return {
        "id": student["id"],
        "name": student["name"],
        "grades": grades
    }

# main entry point to the api
@app.get("/")
async def root():
    return {"message": "Welcome to the Student Grades API!"}

@app.get("/students", response_model=dict)
def get_students():
    formatted_students = [format_student(student) for student in students]
    return {"students": formatted_students}


# get a single student
@app.get("/students/{student_id}", response_model=StudentRepsonse)
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return format_student(student)
            
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students", response_model=StudentOnlyResponse, status_code=201)
def add_student(student: StudentCreate):
    global student_id_counter

    new_student = {
        "id": student_id_counter + 1,
        "name": student.name
    }

    students.append(new_student)
    student_id_counter += 1

    return new_student

# add grades    
@app.post("/student-grades", response_model=GradeResponse, status_code=201)
def add_student_grade(grade: GradeCreate):
    student_exists = any(student["id"] == grade.student_id for student in students)
    if not student_exists:
        raise HTTPException(status_code=404, detail="Student not found")

    new_grade = {
        "student_id": grade.student_id,
        "subject": grade.subject,
        "grade": grade.grade
    }

    student_grades.append(new_grade)

    return new_grade

# if __name__ == "__main__":
    
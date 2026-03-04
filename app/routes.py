from fastapi import APIRouter
from database import cursor, conn

router = APIRouter()

@router.post("/register_student")
def register_student(data: dict):

    cursor.execute("""
    INSERT INTO students
    (name, register_no, department, year, parent_mobile, email, password)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        data["name"],
        data["register_no"],
        data["department"],
        data["year"],
        data["parent_mobile"],
        data["email"],
        data["password"]
    ))

    conn.commit()

    return {"message":"Student registered"}

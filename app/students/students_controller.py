from fastapi import APIRouter
from app.shared.api_response import ApiResponse

from app.pets.pets_service import pets_service
from app.shared.api_response import ApiResponse
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service
from app.shared.api_response import ApiResponse

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("")
def find_all() -> ApiResponse[list[Student]]:
    students = students_service.find_all()

    return ApiResponse(
        success=True,
        message="Students obtained successfully.",
        data=students,
        error=None,
    )


@router.get("/{student_id}")
def find_by_id(student_id: str) -> ApiResponse[Student]:
    student = students_service.find_by_id(student_id)

    return ApiResponse(
        success=True,
        message="Student obtained successfully.",
        data=student,
        error=None,
    )


@router.post("", status_code=201)
def create(body: CreateStudentDto) -> ApiResponse[Student]:
    student = students_service.create(body)
    if not student:
        return ApiResponse(
            success=False,
            error={"code": "STUDENT_CREATION_FAILED"},
            data=None,
            message="Failed to create student. Invalid data provided."
        )
    return ApiResponse(
        success=True,
        message="Student created successfully.",
        data=student,
        error=None,
    )


@router.patch("/{student_id}", response_model=ApiResponse[Student])
def update(student_id: str, body: UpdateStudentDto) -> ApiResponse[Student]:
    updated = students_service.update(student_id, body)
    return ApiResponse.ok(data=updated, message="up-to-date student")

    return ApiResponse(
        success=True,
        message="Student updated successfully.",
        data=student,
        error=None,
    )


@router.delete("/{studentId}")
def delete(studentId: str) -> ApiResponse[None]:
    deleted = students_service.delete(studentId)
    if not deleted:
        return ApiResponse(
            success=False,
            error={"code": "STUDENT_NOT_FOUND"},
            data=None,
            message=f"The student with id {studentId} was not found."
        )
    return ApiResponse(
        success=True,
        error=None,
        data=None,
        message=f"The student with id {studentId} was deleted successfully."
    )

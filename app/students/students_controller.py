from fastapi import APIRouter

from app.pets.pets_service import pets_service
from app.shared.api_response import ApiResponse
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service
from app.shared.api_response import ApiResponse

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("")
def find_all() -> list[Student]:
    return students_service.find_all()


@router.get("/{student_id}")
def find_by_id(student_id: str) -> Student:
    return students_service.find_by_id(student_id)


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
        statusCode=201,
    )


@router.patch("/{student_id}")
def update(student_id: str, body: UpdateStudentDto) -> Student:
    return students_service.update(student_id, body)



@router.delete("/{student_id}", response_model=ApiResponse[None])
def delete(student_id: str):
    deleted = students_service.delete(student_id)
    if not deleted:
        return ApiResponse(
            success=False,
            error={"code": "STUDENT_NOT_FOUND"},
            data=None,
            message=f"The student with id {student_id} was not found."
        )
    pets_service.delete_all_for_student(student_id)

    return ApiResponse(
        success=True,
        error=None,
        data=None,
        message=f"The student with id {student_id} was deleted successfully."
    )



from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service
from app.shared.api_response import ApiResponse

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all_for_student(studentId: str) -> list[Pet]:
    return pets_service.find_all_for_student(studentId)


@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto) -> ApiResponse[Pet]:
    pet = pets_service.create(studentId, body)
    if not pet:
        return ApiResponse(
            success=False,
            error={"code": "STUDENT_NOT_FOUND"},
            data=None,
            message=f"Failed to create pet. The student with id {studentId} was not found."
        )
    return ApiResponse(
        success=True,
        message="Pet created successfully.",
        data=pet,
        statusCode=201,
    )


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto) -> Pet:
    return pets_service.update(studentId, petId, body)


@router.delete("/{petId}")
def delete(studentId: str, petId: str):
    pets_service.delete(studentId, petId)
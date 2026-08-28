from fastapi import APIRouter
from app.shared.api_response import ApiResponse
from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all(studentId: str) -> list[Pet]:
    return pets_service.find_all_for_student(studentId)


@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto) -> Pet:
    return pets_service.create(studentId, body)


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto) -> Pet:
    return pets_service.update(studentId, petId, body)


@router.delete("/{petId}")
def delete(studentId: str, petId: str) -> ApiResponse[None]:
    deleted = pets_service.delete(studentId, petId)
    if not deleted:
        return ApiResponse(
            success=False,
            error={"code": "PET_NOT_FOUND"},
            data=None,
            message=f"The pet with id {petId} was not found."
        )
    return ApiResponse(
        success=True,
        error=None,
        data=None,
        message=f"The pet with id {petId} was deleted successfully."
    )

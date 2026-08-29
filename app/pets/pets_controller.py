from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service
from app.shared.api_response import ApiResponse

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all(studentId: str) -> ApiResponse[list[Pet]]:
    pets = pets_service.find_all_for_student(studentId)

    return ApiResponse(
        success=True,
        message="Properly obtained pets.",
        data=pets,
        error=None,
    )


@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto) -> ApiResponse[Pet]:
    pet = pets_service.create(studentId, body)

    return ApiResponse(
        success=True,
        message="Pet created successfully.",
        data=pet,
        error=None,
    )


@router.patch("/{petId}")
def update(
    studentId: str,
    petId: str,
    body: UpdatePetDto,
) -> ApiResponse[Pet]:
    pet = pets_service.update(studentId, petId, body)

    return ApiResponse(
        success=True,
        message="Pet succesfully updated.",
        data=pet,
        error=None,
    )


@router.delete("/{petId}")
def delete(studentId: str, petId: str) -> ApiResponse[None]:
  pets_service.delete(studentId, petId)

  return ApiResponse(
      success=True,
      message="Pet deleted successfully.",
      data=None,
      error=None,
     )

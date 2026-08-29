using estudiantes_icinf.Models;
using estudiantes_icinf.Repositories;

namespace estudiantes_icinf.Endpoints;

public static class StudentEndpoints
{
    public static void MapStudentEndpoints(this WebApplication app)
    {
        var group = app.MapGroup("/api/students").WithTags("Students");

        // GET: Obtener todos los estudiantes
        group.MapGet("/", async (IStudentRepository repo) =>
        {
            var estudiantes = await repo.GetAllAsync();

            return Results.Ok(
                new ApiResponse<object>(
                    true,
                    "Estudiantes obtenidos correctamente.",
                    estudiantes,
                    200
                )
            );
        });

        // GET: Obtener un estudiante por ID
        group.MapGet("/{id:guid}", async (Guid id, IStudentRepository repo) =>
        {
            var estudiante = await repo.GetByIdAsync(id);

            if (estudiante is null)
            {
                return Results.NotFound(
                    new ApiResponse<object>(
                        false,
                        "Estudiante no encontrado.",
                        null,
                        404
                    )
                );
            }

            return Results.Ok(
                new ApiResponse<object>(
                    true,
                    "Estudiante obtenido correctamente.",
                    estudiante,
                    200
                )
            );
        });

        // POST: Crear estudiante
        group.MapPost("/", async (CreateStudentDto dto, IStudentRepository repo) =>
        {
            if (await repo.GetByEmailAsync(dto.Email) is not null)
            {
                return Results.Conflict(
                    new ApiResponse<object>(
                        false,
                        "El email ya está registrado.",
                        null,
                        409
                    )
                );
            }

            var creado = await repo.AddAsync(dto);

            return Results.Created(
                $"/api/students/{creado.Id}",
                new ApiResponse<object>(
                    true,
                    "Estudiante creado correctamente.",
                    creado,
                    201
                )
            );
        });

        // PATCH: Actualizar estudiante
        group.MapPatch("/{id:guid}", async (Guid id, UpdateStudentDto dto, IStudentRepository repo) =>
        {
            if (dto.Email is not null &&
                await repo.GetByEmailAsync(dto.Email, id) is not null)
            {
                return Results.Conflict(
                    new ApiResponse<object>(
                        false,
                        "El email ya está registrado.",
                        null,
                        409
                    )
                );
            }

            var actualizado = await repo.UpdateAsync(id, dto);

            if (actualizado is null)
            {
                return Results.NotFound(
                    new ApiResponse<object>(
                        false,
                        "Estudiante no encontrado.",
                        null,
                        404
                    )
                );
            }

            return Results.Ok(
                new ApiResponse<object>(
                    true,
                    "Estudiante actualizado correctamente.",
                    actualizado,
                    200
                )
            );
        });

        // DELETE: Eliminar estudiante
        group.MapDelete("/{id:guid}", async (Guid id, IStudentRepository repo) =>
        {
            await repo.DeleteAsync(id);

            return Results.Ok(
                new ApiResponse<object>(
                    true,
                    "Estudiante eliminado correctamente.",
                    null,
                    200
                )
            );
        });
    }
}


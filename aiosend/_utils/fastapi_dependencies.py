from collections.abc import Callable
from typing import Any

from fastapi.dependencies.utils import get_dependant, solve_dependencies
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request


async def resolve_fastapi_dependencies(
    request: Request,
    handler: Callable[..., Any],
) -> dict[str, Any]:
    dependant = get_dependant(
        path=request.url.path,
        call=handler,
    )

    dependant.path_params.clear()
    dependant.query_params.clear()
    dependant.header_params.clear()
    dependant.cookie_params.clear()
    dependant.body_params.clear()

    solved = await solve_dependencies(
        request=request,
        dependant=dependant,
        body=None,
        dependency_overrides_provider=request.app,
        async_exit_stack=request.scope["fastapi_function_astack"],
        embed_body_fields=False,
    )

    if solved.errors:
        raise RequestValidationError(solved.errors)

    return solved.values

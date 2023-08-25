"""Ping utility."""


import fastapi
from fastapi import status


router = fastapi.APIRouter(prefix="/ping")


@router.get("/", include_in_schema=False)
def ping():
    """Ping path operation.

    Responds with HTTP_200_OK status to GET requests. Helps confirm the
    application is reachable and debug networking issues. Can serve as a heartbeat
    mechanism for load balancer health checks.
    """
    return fastapi.Response(status_code=status.HTTP_200_OK)

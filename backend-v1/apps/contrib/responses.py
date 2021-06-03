from rest_framework import status
from rest_framework.response import Response


class ResourceCreatedResponse(Response):
    status_code = status.HTTP_201_CREATED

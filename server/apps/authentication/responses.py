from rest_framework.response import Response


class ChallengeResponse(Response):
    def __init__(self, name: str = '', data=None):
        super().__init__({'challenge': name, **data})

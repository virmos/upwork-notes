import logging

logger = logging.getLogger(__name__)

class LogRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.error("Request: {request.method} {request.get_full_path()} Headers: {request.headers}")
        response = self.get_response(request)
        if response.status_code in [301, 302]:
            logger.error(f"Redirecting to: {response['Location']}")
        logger.error(f"Response: {response.status_code} {response.content}")
        return response

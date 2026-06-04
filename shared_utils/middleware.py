import json
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from sentry_sdk import capture_exception


class CaptureExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if exception:
            capture_exception(exception)
            return JsonResponse(
                {"success": False, "detail": str(exception)}, status=500
            )


class ValidationErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response: HttpResponse = self.get_response(request)

        content_type = response.headers.get("Content-Type")
        if (
                content_type
                and content_type == "application/json"
                and response.status_code == 400
        ):
            data = json.loads(response.content)
            if (
                    isinstance(data, dict)
            ):
                data.pop("success", None)
                errors = data
                if errors.get('detail'):
                    errors = errors.get('detail')
                elif errors.get('errors'):
                    errors = errors.get('errors')
                elif errors.get('error'):
                    errors = errors.get('error')
                data = {"success": False, "errors": errors}

            response.content = json.dumps(data)

        return response


class CookieToAuthHeaderMiddleware(MiddlewareMixin):
    """Bridge cookie-based auth to the header readers.

    When the request carries the access token in a cookie but no Authorization
    header, inject it into ``request.META`` as a Bearer header. This lets every
    existing header reader (DRF ``CustomJWTAuthentication``, the access-time /
    session / audit middleware, the ``@decorators`` token check, and the
    service-to-service token forwards) keep working unchanged.

    Must be the FIRST middleware and must only touch ``request.META`` /
    ``request.COOKIES``: ``request.headers`` is a cached_property built from
    ``META`` on first access, so populating META here (before anything reads
    ``headers``) makes the injected token visible to header readers too.
    """

    def process_request(self, request):
        if request.META.get("HTTP_AUTHORIZATION"):
            return
        token = request.COOKIES.get("access_token")
        if token:
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {token}"

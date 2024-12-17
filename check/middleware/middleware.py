# from typing import Any
# from django.http import HttpResponseForbidden


# ALLOWED_IPS = ["123.45.67.89", "987.56.65.21"]

# class IPBlockingMiddleware:
#     def __init__(self, get_response) -> None:
#         self.get_response = get_response

#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             return x_forwarded_for.split(',')[0]
#         return request.META.get('REMOTE_ADDR')

#     def __call__(self, request):
#         ip = self.get_client_ip(request)
#         print(ip)
#         if ip not in ALLOWED_IPS:  # Deny if IP is not allowed
#             return HttpResponseForbidden("Forbidden: IP not allowed")
#         return self.get_response(request)

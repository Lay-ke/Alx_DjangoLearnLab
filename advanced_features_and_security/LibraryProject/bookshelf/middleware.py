class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Set the Content-Security-Policy header
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' https://trusted.cdn.com; "
            "style-src 'self' https://fonts.googleapis.com; "
            "img-src 'self' https://images.example.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "connect-src 'self' https://api.example.com; "
            "form-action 'self'; "
            "object-src 'none'; "
            "frame-ancestors 'none';"
        )

        return response

from requests.auth import AuthBase


class Authenticate(AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, request):
        request.headers.update(self.headers(self.api_key))
        return request
        
    def headers(self, api_key):
        return {
            'Content-Type': 'Application/JSON',
            'Authorization': api_key
    }
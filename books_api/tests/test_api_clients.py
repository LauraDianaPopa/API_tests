from books_api.requests.api_clients import *

class TestApiClient:
    nr = randint(1,9999999)
    clientName = "Laura2"
    clientEmail = f'valid_email_test{nr}@mailinator.com'

    def setup_method(self):
        self.response = login(self.clientName, self.clientEmail)

    def test_successful_login(self):
        assert self.response.status_code == 201, 'Actual status code is incorrect'
        assert 'accessToken' in self.response.json().keys(), 'Token property is not present in response keys'

    def test_login_client_already_registered(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409
        assert self.response.json()['error'] == 'API client already registered. Try a different email.'

    def test_invalid_mail(self):
        self.response = login('def','abc')
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', ''
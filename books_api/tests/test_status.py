from books_api.requests.status import *

class TestStatus:

    def test_get_status_code(self):
        #print(get_status())
        status_code = get_status().status_code
        assert status_code == 200, "Status code is incorrect"

    def test_get_status_body(self):
        status = get_status().json()
        #print(status.keys())
        assert 'status' in status.keys(), "Cheia status nu exista"
        assert status['status'] == 'OK', "Mesajul ar trebui sa fie 'OK'"


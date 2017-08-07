

class TestBasicViews:

    def test_home_page_GET(self, client):
        response = client.get('/')

        assert response.status_code == 200

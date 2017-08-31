"""Test some core views."""


def test_favicon(client):
    # GIVEN any state
    # WHEN a browser requests the favicon.ico from the website root
    url = '/favicon.ico'
    response = client.get(url)

    # THEN it gets redirected to the file
    assert response.status_code == 302

def test_robots_txt(client):
    # GIVEN any state
    # WHEN a browser requests the robots.txt
    url = '/robots.txt'
    response = client.get(url)

    # THEN it is served
    assert response.status_code == 200
    assert 'www.unkenmathe.de' in response.content.decode()

import pytest
from bs4 import BeautifulSoup
from httpconverter.main import HTTPConverter

def test_extractor_json():
    content = BeautifulSoup(
        '''<request base64="false">POST /api/login HTTP/1.1\nHost: example.com\nContent-Type: application/json\n\n{"username": "user", "password": "pass"}</request>''', 'xml'
    )
    result = HTTPConverter._extractor(content)
    assert result['method'] == "POST"
    assert result['endpoint'] == "/api/login"
    assert result['headers'] == {"Host": "example.com", "Content-Type": "application/json"}
    assert result['json'] == '{"username": "user", "password": "pass"}'

def test_extractor_no_headers():
    content = BeautifulSoup('<request base64="false">GET /api/test HTTP/1.1\n</request>', 'xml')
    result = HTTPConverter._extractor(content)
    assert result['headers'] == {}
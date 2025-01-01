import pytest
from bs4 import BeautifulSoup
from httpconverter.main import HTTPConverter

def test_file_not_found():
    with pytest.raises(FileNotFoundError, match="No such file or directory: .*"):
        HTTPConverter("nonexistent.xml")

def test_missing_host_header():
    content = BeautifulSoup(
        '<request base64="false">GET /api/profile HTTP/1.1\nContent-Type: application/json\n\n</request>', 'xml'
    )
    result = HTTPConverter._extractor(content)
    assert "Host" not in result['headers']

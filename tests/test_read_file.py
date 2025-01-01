import pytest
from bs4 import BeautifulSoup
from httpconverter.main import HTTPConverter

@pytest.fixture
def create_valid_burp_file(tmp_path):
    filepath = tmp_path / "valid_burp.xml"
    filepath.write_text('<items burpVersion="2024.11"><item></item></items>')
    return filepath

@pytest.fixture
def create_invalid_burp_file(tmp_path):
    filepath = tmp_path / "invalid_burp.xml"
    filepath.write_text('<items></items>')
    return filepath

def test_read_file_valid(create_valid_burp_file):
    converter = HTTPConverter(file=str(create_valid_burp_file))
    assert isinstance(converter.text, BeautifulSoup)

def test_read_file_invalid_format(create_invalid_burp_file):
    with pytest.raises(NotImplementedError):
        HTTPConverter(file=str(create_invalid_burp_file))
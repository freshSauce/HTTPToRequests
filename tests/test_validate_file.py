import pytest
from bs4 import BeautifulSoup
from httpconverter.main import HTTPConverter

# Pruebas para _validate_file
def test_validate_file_valid():
    content = BeautifulSoup('<items burpVersion="2024.11"></items>', 'xml')
    assert HTTPConverter._validate_file(content) == True

def test_validate_file_invalid():
    content = BeautifulSoup('<items></items>', 'xml')
    assert HTTPConverter._validate_file(content) == False

def test_validate_file_unsupported_source():
    content = BeautifulSoup('<items></items>', 'xml')
    with pytest.raises(NotImplementedError):
        HTTPConverter._validate_file(content, source="unknown")
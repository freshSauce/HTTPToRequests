import pytest
from bs4 import BeautifulSoup
from httpconverter.main import HTTPConverter

@pytest.fixture
def create_request_file(tmp_path):
    filepath = tmp_path / "request_burp.xml"
    filepath.write_text(
        '''<items burpVersion="2024.11">
        <item>
            <request base64="false"><![CDATA[GET /api/profile HTTP/1.1\nHost: example.com\nAuthorization: Bearer token]]></request>
        </item>
        </items>'''
    )
    return filepath


def test_extract_valid(create_request_file, tmp_path):
    output_file = tmp_path / "output.py"
    converter = HTTPConverter(file=str(create_request_file))
    converter.extract(filename=str(output_file))

    assert output_file.exists()
    with open(output_file, "r") as f:
        content = f.read()
        assert "def get_api_profile" in content

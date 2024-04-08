import requests_mock
from src.my_pkg.main import fetch_data
# The URL being tested
TEST_URL = "https://api.publicapis.org/entries"

# Test data simulating a response from the API
TEST_DATA = {
    "entries": [
        {
            "API": "Test API 1",
            "Description": "A test API",
            "Auth": "",
            "HTTPS": True,
            "Cors": "no",
            "Link": "https://example.com",
            "Category": "Test",
        },
        {
            "API": "Test API 2",
            "Description": "Another test API",
            "Auth": "apiKey",
            "HTTPS": True,
            "Cors": "yes",
            "Link": "https://example2.com",
            "Category": "Test",
        },
    ]
}


def test_fetch_data():
    with requests_mock.Mocker() as m:
        m.get(TEST_URL, json=TEST_DATA)
        result = fetch_data(TEST_URL)

# Ensure the mocked URL returns the expected test data
        assert result == TEST_DATA

# checks can include ensuring the structure of the data is as expected
        assert len(result["entries"]) == 2
        assert result["entries"][0]["API"] == "Test API 1"
        assert result["entries"][1]["API"] == "Test API 2"

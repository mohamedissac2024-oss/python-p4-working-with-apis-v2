import pytest
from lib.open_library_api import Search


class TestSearch:
    """Test class for the Search API methods"""

    def test_get_search_results_returns_bytes(self):
        """Test that get_search_results returns bytes content"""
        search = Search()
        result = search.get_search_results()
        assert isinstance(result, bytes)
        assert b"numFound" in result or b"docs" in result

    def test_get_search_results_json_returns_dict(self):
        """Test that get_search_results_json returns a JSON-formatted response (dict)"""
        search = Search()
        result = search.get_search_results_json()
        assert isinstance(result, dict)
        assert "docs" in result
        assert len(result["docs"]) > 0
        assert "title" in result["docs"][0]
        assert "author_name" in result["docs"][0]

    def test_get_user_search_results_returns_formatted_string(self):
        """Test that get_user_search_results returns formatted string with title and author"""
        search = Search()
        result = search.get_user_search_results("the lord of the rings")
        assert isinstance(result, str)
        assert "Title:" in result
        assert "Author:" in result
        assert "J.R.R. Tolkien" in result or "Tolkien" in result

    def test_get_search_results_json_contains_correct_data(self):
        """Test that get_search_results_json returns correct book information"""
        search = Search()
        result = search.get_search_results_json()
        # Verify the search returned results for "the lord of the rings"
        assert result["numFound"] >= 1
        assert result["docs"][0]["title"].lower().replace(" ", "") == "thelordoftherings".lower().replace(" ", "")


def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1 == 1


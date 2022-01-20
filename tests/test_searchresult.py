import sys
from pathlib import Path

root = Path(__file__).parent.parent
sys.path.append(str(root))

path = sys.path
sys.path.append("")


from pygsearch import SearchResult


def test_searchresult_eq_str():
    result = SearchResult("test", "test", "test")
    assert result == "test"

def test_searchresult_eq_searchresult():
    result1 = SearchResult("test", "test", "test")
    result2 = SearchResult("test", "test", "test")
    assert result1 == result2

def test_searchresult_set():
    results = [SearchResult("test", "test", "test") for i in range(20)]
    assert len(set(results)) == 1

def test_searchresult_prettify():
    search_result = SearchResult("test", "test", "test")
    assert search_result.prettify() == f"Link:  test\nTitle: test\nDescr: test\n"

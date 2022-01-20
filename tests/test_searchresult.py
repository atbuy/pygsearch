import sys
from pathlib import Path

root = Path(__file__).parent.parent
sys.path.append(str(root))

path = sys.path
sys.path.append("")


from pygsearch import SearchResult


def test_searchresult_prettify():
    search_result = SearchResult("test", "test", "test")
    assert search_result.prettify() == f"Link:  test\nTitle: test\nDescr: test\n"

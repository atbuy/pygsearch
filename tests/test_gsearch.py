from pygsearch import SearchResult, gsearch


def test_gsearch_iter():
    results = [SearchResult(f"test{i}", f"test{i}", f"test{i}") for i in range(10)]
    search = gsearch()
    search.results = results

    for i, result in enumerate(search):
        assert result == SearchResult(f"test{i}", f"test{i}", f"test{i}")

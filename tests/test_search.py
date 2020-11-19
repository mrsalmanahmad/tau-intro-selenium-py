from pages.result import duckduckgoResultPage
from pages.search import duckduckgoSearchPage

def test_basic_duckduckgo(browser):
    search_page = duckduckgoSearchPage
    result_page = duckduckgoResultPage
    PHRASE = "panda"
    # Giver the duckduckgo homepage is displayed
    # TODO
    search_page.load()
    # When the user searches for Panda
    # TODO
    search_page.search(PHRASE)
    # Then the Search result should contain "Panda"
    # TODO
    assert PHRASE in result_page.title()
    # And the search result query is Panda
    # TODO
    assert PHRASE == result_page.search_input_value()
    # And the search result links pertain to panda
    # TODO
    for title in result_page.result_link_titles():
        assert PHRASE.lower in title.lower()

from typing import List

import requests
import collections


SearchResult = collections.namedtuple('SearchResult', 'category, id, url, title, '
                                        'description')


def find_movie_by_title(keyword: str) -> List[SearchResult]:
    url = f'http://search.talkpython.fm/api/search?q={keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    searchresults = []
    for r in results.get('results'):
        searchresults.append(SearchResult(**r))

    return searchresults


import api
from collections import defaultdict
import webbrowser

def main():
    keyword = input('Keyword of title search: ')
    results = api.find_movie_by_title(keyword)

    results_dict = defaultdict(list)
    counter = 1

    print(f'There are {len(results)} search results found.')
    for r in results:
        x=r.url
        results_dict[counter].append(x)

        print(f"Result {counter} is a {r.category} with the title of '{r.title}'")
        counter += 1

    grabURL = input('What url to visit?')
    grabURL = int(grabURL)


    weblink = f'https://talkpython.fm{results_dict[grabURL][0]}'
    webbrowser.open(weblink, new=2)




if __name__ == '__main__':
    main()

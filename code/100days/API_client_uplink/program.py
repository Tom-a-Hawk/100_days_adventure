from blog_client import BlogClient

def main():

    val= 'RUN'

    while val:
        print('What would you like to do next?')

        val = input('[w]rite a post or [r]ead them?')


        if val == 'w':
            write_post()

        elif val == 'r':
            read_posts()


def read_posts():
    svc = BlogClient()
    response = svc.all_entries()
    response.raise_for_status()

    posts = response.json()

    for idx, p in enumerate(posts, 1):
        print(" * {}. [{} views] {}".format(
            idx, p.get('view_count'), p.get('title')
        ))

    print()
    selected = int(input('Which number to view? '))

    selected_id = posts[selected-1].get('id')

    print(selected_id)

def write_post():
    pass

if __name__ == '__main__':
    main()
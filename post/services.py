import requests

def get_posts():
    url = 'http://127.0.0.1:8000/api/posts/'
    #params = {'year': year, 'author': author}
    #r = requests.get(url, params=params)
    r = requests.get(url)
    posts = r.json()
    posts_list = {'posts':posts['results']}
    return posts_list

#http://127.0.0.1:8000/api/xpost/1/
def get_post_detail(pk):
    MAX_RETRIES = 20
    url = 'http://127.0.0.1:8000/api/xpost/%s' % (pk)

    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
    session.mount('https://', adapter)
    session.mount('http://', adapter)

    r = session.get(url)
    posts = r.json()
    posts_list = {'post':posts}
    return posts_list


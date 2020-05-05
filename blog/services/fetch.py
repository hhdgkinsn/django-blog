import requests

def fetchData(): 
    url = "https://jsonplaceholder.typicode.com/posts"
    req = requests.get(url)
    posts = req.json()
    post_list = []
    for i in range(len(posts)):
        post_list.append(posts[i])
    return post_list
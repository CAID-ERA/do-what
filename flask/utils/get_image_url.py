import json


def get_image_url(path, name):
    with open(path, 'r') as f:
        txt = f.read()
        movies = json.loads(txt)
        for movie in movies:
            if movie['name'] == name:
                return movie['image_url']
import json


def movie_kind_to_index(movie_kind_list, map_path):
    with open(map_path, 'r') as f:
        movie_map = json.loads(f.read())
        movie_kind_index_list = []
        for kind in movie_kind_list:
            if kind in movie_map:
                movie_kind_index_list.append(movie_map[kind])
        return movie_kind_index_list
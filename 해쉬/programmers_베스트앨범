# programmers, 베스트앨범

from collections import defaultdict


def get_elbum_list(genres_in_order, play_list_by_genre):
    elbum_list = []
    for genre in genres_in_order:
        play_list_by_genre[genre].sort(key=lambda x: (-x[0], x[1]))
        elbum_list.extend(list(map(lambda x: x[1], play_list_by_genre[genre][:2])))
    return elbum_list


def get_order_by_genres(total_play_by_genre):
    return sorted(total_play_by_genre.keys(), key=lambda x: total_play_by_genre[x], reverse=True)


def solution(genres, plays):
    total_play_by_genre = defaultdict(int)
    play_list_by_genre = defaultdict(list)

    for i in range(len(genres)):
        total_play_by_genre[genres[i]] += plays[i]
        play_list_by_genre[genres[i]].append((plays[i], i))

    genres_in_order = get_order_by_genres(total_play_by_genre)
    return get_elbum_list(genres_in_order, play_list_by_genre)

if __name__ == '__main__':
    genres = ["classic", "classic", "classic", "pop"]
    plays = [1000, 1000, 1000, 100]
    print(solution(genres, plays))

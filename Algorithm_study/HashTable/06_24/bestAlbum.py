# HashTable [베스트앨범]
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

# 소요시간 : 55분

def solution(genres, plays):
    answer = []
    # 장르마다 재생수의 합을 Dictionary로 만드는 과정
    # {'k-pop' : 548848, 'pop' : 3100, 'classic' : 1100}
    music_dict = dict()
    for genre_i, plays_i in zip(genres, plays):
        if genre_i in music_dict.keys():
            music_dict[genre_i] = music_dict.get(genre_i) + plays_i
        else:
            music_dict[genre_i] = plays_i
    
    # 장르별 총 재생횟수 저장 후, 내림차순 정렬
    # [(548848, 'k-pop'), (3100, 'pop'), (1100, 'classic')]
    val_list = list(set(zip(music_dict.values(),music_dict.keys())))
    val_list.sort(reverse=True)
    
    for i in val_list:
        # 장르에 맞는 음악 별 재생횟수와, 고유번호를 불러오는 코드
        all_genre_index = list(filter(lambda x: genres[x] == i[1], range(len(genres)))) 
        in_genre_list = list() # (음악 별 재생 횟수, 고유 번호)
        for index in all_genre_index:
            in_genre_list.append(tuple([plays[index], index]))
        # [(150, 2), (800, 4), (150, 0)]
        # 재생별로 정렬하되, 같은 재생 순은 인덱스가 작은 순서대로 정렬 # [(800, 4), (150, 2), (150, 0)]
        in_genre_list = sorted(in_genre_list, key=lambda x: (-x[0], x[1]))
        answer += [j[1] for j in in_genre_list[0:2]] # 상위 2개 인덱스만 추출 
    return answer

genres = ["classic", "pop", "classic", "k-pop","classic", "pop"]
plays = [150, 600, 150, 548848 ,800, 2500]

print(solution(genres, plays))
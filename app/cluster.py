from sklearn.cluster import KMeans
import numpy as np
from typing import List

#스포츠분류
exercise_clusters = {
    "구기 운동": ['축구', '농구', '배구', '풋살', '야구', '라켓볼', '배드민턴', '탁구'],
    "격투 및 무술": ['태권도', '유도', '택견', '검도', '킥복싱', '복싱'],
    "피트니스 및 웨이트": ['헬스', '바디펌프', '피트니스', '서킷핏', '서킷트레이닝', '역도', '보디빌딩', '줄넘기', '걷기'],
    "유연성 및 균형": ['요가', '필라테스', '리듬체조', '발레', '태극권', '아쿠아로빅', '트램폴린', '밸리댄스'],
    "댄스": ['댄스', '줌바', '힙합댄스', '라인댄스', '탱고', '스포츠댄스', '방송댄스'],
    "수상 및 동계 스포츠": ['수영', '빙상', '쇼트트랙', '다이빙', '피겨', '스피닝'],
    "레크리에이션": ['골프', '스크린골프', '볼링', '사격', '암벽', '워킹'],
    "정신적 및 창작 활동": ['체스', '종이접기', '드로잉', '디자인', '미술', '독서', '수필', '코딩'],
    "악기 및 퍼포먼스": ['가야금', '피아노', '통기타', '드럼', '바이올린', '밴드', '우쿨렐레', '뮤직'],
    "혼합 및 기타 활동": ['철인반', '순환운동', '체조', '장애인스포츠']
}

cluster_features = {
    "구기 운동": [9, 8, 10, 6, 9, 10, 9, 5, 8, 9],  # 팀 스포츠, 야외, 고강도, 유산소 중심
    "격투 및 무술": [10, 10, 9, 7, 10, 6, 8, 5, 7, 7],  # 고강도, 개인 중심, 목표 지향
    "피트니스 및 웨이트": [8, 9, 10, 6, 8, 6, 9, 9, 7, 6],  # 실내 중심, 근력 운동, 정기적
    "유연성 및 균형": [6, 6, 8, 8, 6, 5, 10, 10, 6, 5],  # 유연성 강화, 실내, 낮은 강도
    "댄스": [7, 7, 8, 9, 6, 6, 8, 9, 7, 6],  # 창의적, 실내, 지속적 움직임
    "수상 및 동계 스포츠": [9, 9, 7, 6, 8, 7, 8, 6, 8, 9],  # 야외, 고강도, 유산소 운동
    "레크리에이션": [6, 6, 6, 5, 6, 6, 7, 5, 7, 6],  # 저강도, 가벼운 활동
    "정신적 및 창작 활동": [4, 4, 5, 9, 4, 3, 5, 9, 7, 4],  # 창의력 중심, 실내, 낮은 신체 활동
    "악기 및 퍼포먼스": [5, 5, 5, 9, 5, 4, 5, 10, 6, 5],  # 퍼포먼스 중심, 실내
    "혼합 및 기타 활동": [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]  # 다양한 활동
}

def cluster(user_scores: List[int]):
    user_scores = np.array(user_scores)
    cluster_names = list(cluster_features.keys())
    cluster_data = np.array(list(cluster_features.values()))

    distances = np.sum((cluster_data - user_scores) ** 2, axis=1)
    recommended_cluster = cluster_names[np.argmin(distances)]

    recommended_exercises = exercise_clusters[recommended_cluster]

    print(recommended_cluster)
    print(recommended_exercises)

    return recommended_exercises
# 파이썬 내장함수 min 사용 금지
def min_score(scores):
    min_score = scores[0]
    for i in scores:
        if min_score > i:
            min_score = i
    return min_score


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    

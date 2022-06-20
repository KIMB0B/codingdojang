import datetime
import time

# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

# 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.

start = time.time()
###############내 풀이##############
import random
S = list(set(list([random.randint(1,100) for i in range(10)])))
S.sort()
length=0
result=[]
for i in range(0, len(S)-1):
    if length==0:
        length=S[i+1]-S[i]
    if length > S[i+1]-S[i]:
        result.clear()
        length=S[i+1]-S[i]
    if length >= S[i+1]-S[i]:
        result.append((S[i], S[i+1]))
print("입력된 랜덤값 : {}".format(S))
print("가장 짧은 {}의 거리가 나오는 점의 쌍은 {} 이다.".format(length, result))
####################################
end = time.time()
print("내 코드 실행시간 : " + str(datetime.timedelta(seconds=end-start)))
import datetime
import time

# 1~1000에서 각 숫자의 개수 구하기
# 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자

# 10 = 1, 0
# 11 = 1, 1
# 12 = 1, 2
# 13 = 1, 3
# 14 = 1, 4
# 15 = 1, 5

# 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개

start = time.time()
###############내 풀이##############
for i in range(0, 10):
    print("{} : {}개".format(i, str(list(range(1, 1001))).count(str(i))))
####################################
end = time.time()
print("내 코드 실행시간 : " + str(datetime.timedelta(seconds=end-start)))


start = time.time()
###########다른사람 풀이#############
count={ x:0 for x in range(0,10) }
for x in range(1,1001):
    for i in str(x):
        count[int(i)]+=1
print(count)
####################################
end = time.time()
print("다른사람 코드 실행시간 : " + str(datetime.timedelta(seconds=end-start)))
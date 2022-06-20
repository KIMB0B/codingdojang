import datetime
import time
# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

start = time.time()
###############내 풀이##############
answer = 0
for i in range(1, 1000):
    if i%3==0 or i%5==0:
        answer += i
print(answer)
####################################
end = time.time()
print(datetime.timedelta(seconds=end-start))


start = time.time()
###########다른사람 풀이#############
print(sum([i for i in range(1, 1000) if i%3==0 or i%5==0]))
####################################
end = time.time()
print(datetime.timedelta(seconds=end-start))
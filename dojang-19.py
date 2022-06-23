import datetime
import time

# n개의 정수를 가진 배열이 있다. 이 배열은 양의정수와 음의 정수를 모두 가지고 있다. 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.

# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다. 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.

# 예. -1 1 3 -2 2 ans: -1 -2 1 3 2.

start = time.time()
###############내 풀이##############
lista = [-1, 1, 3, -2, 2]

if lista[len(lista)-1] < 0:
    last=False
else:
    last=True

i=0
while i < len(lista):
    cnt=0
    if lista[i] >= 0:
        lista.append(lista[i])
        lista.pop(i)
    else:
        i+=1
    # 현재 인덱스보다 뒤에있는 값들이 전부 양수인지 확인
    for x in range(i, len(lista)):
        if lista[x] >= 0:
            cnt+=1
    # 전부 양수인 상황에서 배열 마지막값이 양수였다면 한번 더 뒤로 이동
    if cnt==len(lista)-i:
        if last==True:
            lista.append(lista[i])
            lista.pop(i)
        i=len(lista) # 반복문 종료를 위해 len(lista)넣어줌

print("정렬 후 : ", lista)
####################################
end = time.time()
print("내 코드 실행시간 : " + str(datetime.timedelta(seconds=end-start)))
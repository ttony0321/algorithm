#시간 복잡도
'''
빅오: 상한선을 표현  <- 최악의 경우 시간복잡도

빅오메가: 하한선을 표현

빅세타: 상한선과 하한선 사이를 표현


시간복잡도 
작음 ------->큼
O(1) < O(logn) < O(N) < O(nlogn) < O(n^2) < O(2n) < O(n!)


'''

def func(n):
    sum = 0 #대입 연산 1회
    i =  0 #대입 연산 1회
    
    for i in range(n):#반복문 n + 1
        sum += 1 #덧셈 연산 n
        
    for i in range(n):#반복문 n + 1
        sum += 1 #덧셈 연산 n
        
    return sum      #리턴 1회

    #총 연산 횟수 4n + 5       
    #시간 복잡도 O(n)



####################################################################################
####################################################################################
####################################################################################
####################################################################################

#시간 복잡도 O(1)
def func(n):
    print(n)
    ##연산 한번만 진행 되므로 O(1)
    
#시간 복잡도 O(logN)
n = 10
for i in range(1, n, 2):
    print(i)
    #2배씩 증가한다
    
#시간복잡도 O(n)
#선형 시간 입력값이 커짐에따라 비례해서 증가
for i in range(n):
    print(i)
    
#시간 복잡도 O(n^2)
for i in range(n):
    for j in range(n):
        print(i, j)
        
#시간 복잡도 O(2^n)
def func2(n):
    if(n <= 1):
        return n
    return func2(n-1) + func2(n-2)



###########################################################
#시간 복잡도 예시

for i in range(1, n, 2):
    pass

#시간 복잡도 O(n/2)인데 1/2는 상수라 O(n)

for i in range(n):
    if n%0:
        continue
    '''
    실행 시간 계산
    
    if문 실행시간 c0
    continue 실행시간 c1
    그 아래 나머지 코드 실행시간 c2
    
    for 문 n번 반복
    시간 복잡도는 (c0+c1+c2)n
    (c0+c1+c2)은 상수라서 결국
    시간복잡도는 n
    
    '''
    
    
def fun(n):
    if(n == 0):
        return
    
    fun(n/2)   
    
    '''
    f(n) = f(n/2) + c
    여기서 c는 if문 처리시간
    
    f(n) = f(n/2^k) + c+c+c+c....
    O(log n)
    ''' 
    
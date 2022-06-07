#4673
#브루트포스 알고리즘, 구현, 수학
#실버 5

nums = set(range(1, 10001))
remove_list = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    remove_list.add(i)
nums = nums - remove_list
for k in sorted(nums):
    print(k)
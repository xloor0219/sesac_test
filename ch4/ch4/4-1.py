# 입력
n = int(input())
moves = str(input().split())

now = [1,1]

# 이동
for move in moves: # moves 하나씩 확인
    if move == 'L':
        if now[1] > 1:
            now[1] -= 1
    elif move == 'R':
        if now[1] < n:
            now[1] += 1
    elif move == 'U': # 'up'은 밑으로 가야 커짐
        if now[0] > 1:
            now[0] -= 1
    elif move == 'D':
        if now[0] < n:
            now[0] += 1

# 출력
print(now[0], now[1])
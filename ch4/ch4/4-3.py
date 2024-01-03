# 나이트의 현재 위치 입력 받기
knight = input()
row = int(knight[1])
column = int(ord(knight[0])) - int(ord('a')) + 1 ##

count = 0

# 나이트의 이동 가능 경우의 수 세기
# 나이트의 총 이동 가능 경우의 수: 8가지
moves = [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

# 현재 위치에서 가능한 경우를 확인해서 카운트에 넣기
for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]
    
    if 1 <= next_row <= 8 and 1<= next_column <= 8:
        count += 1

# 출력
print(count)
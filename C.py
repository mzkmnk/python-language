n = int(input())
s = input()

# 座標の初期化
x, y = 0, 0

# すでに訪れた座標を管理するためのset
visited = set()
visited.add((x, y))

# N回の移動を順番に処理
for i in range(n):
    if s[i] == "R":
        x += 1
    elif s[i] == "L":
        x -= 1
    elif s[i] == "U":
        y += 1
    elif s[i] == "D":
        y -= 1

    # 移動後の座標がすでに訪れたことがある場合、高橋君は同じ座標にいたことがある
    if (x, y) in visited:
        print("Yes")
        exit()

    visited.add((x, y))

# N回の移動後、同じ座標にいたことがない場合
print("No")

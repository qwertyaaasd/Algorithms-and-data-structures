def point_sort(point, n):
    cnt = 0
    for i in range(n):
        flag = False
        for j in range(n-1):
            if point[j][0]**2 + point[j][1]**2 > point[j+1][0]**2 + point[j+1][1]**2:
                point[j], point[j+1] = point[j+1], point[j]
                flag = True

        if flag == False:
            break

    return point

n = int(input())
point = []
for i in range(n):
    point.append(list(map(int, input().split())))

point = point_sort(point, n)
for p in point:
    print(* p)
n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
distances = [-1]*n
def sum_forward_elements(list):
    for i in range(len(list)):
        list[i] = list[i] + list[i-1] if i > 0 else list[i]
for i in range(n):
    for j in range(n):
        temp_distances = []
        for point in points:
            distance = abs(points[i][0] - point[0]) + abs(points[j][1] - point[1])
            temp_distances.append(distance)
        temp_distances.sort()
        sum_forward_elements(temp_distances)
        for k in range(n):
            if distances[k] == -1:
                distances[k] = temp_distances[k]
            else:
                distances[k] = min(distances[k],temp_distances[k])

print(*distances)

# n = int(input())
# points = []
# point_x = []
# point_y = []
# distances = [-1]*n
# for _ in range(n):
#     x,y = map(int,input().split())
#     points.append([x,y])
#     point_x.append(x)
#     point_y.append(y)
# for y in point_y:
#     for x in point_x:
#         temp_distances = []
#         for ex,ey in points:
#             temp_distance = abs(ex-x)+abs(ey-y)
#             temp_distances.append(temp_distance)
#         temp_distances.sort()
#         temp = 0
#         for i in range(len(temp_distances)):
#             temp += temp_distances[i]
#             if distances[i] == -1:
#                 distances[i] = temp
#             else:
#                 distances[i] = min(distances[i],temp)
# print(*distances)

# for i in range(n):
#     for j in range(n):
#         temp_distances = []
#         for point in points:
#             distance = abs(points[i][0] - point[0]) + abs(points[j][1] - point[1])
#             temp_distances.append(distance)
#         temp_distances.sort()        
#         temp = 0
#         for k in range(n):
#             temp += temp_distances[k]
#             distances[k] = min(distances[k],temp)

# print(*distances)



# def sum_forward_elements(list):
#     for i in range(len(list)):
#         list[i] = list[i] + list[i-1] if i > 0 else list[i]
# answer = []
# for i in range(1,n+1):
#     a = 0
#     for j in range(i):
#         a += distances[j]
#         answer.append(a)
# print(*answer)
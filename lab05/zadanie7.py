def count_total_points(**teams):
    total_points = 0
    for points in teams.values():
        total_points += points
    return total_points 
sum = count_total_points(liverpool=60, manchester_city=56, chelsea=50)
print(sum)
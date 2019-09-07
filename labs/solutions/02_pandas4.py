def answer_four():
    points = 3*df['Gold.2'] + 2*df['Silver.2'] + df['Bronze.2']
    return points

answer_four().sort_values(ascending = False)
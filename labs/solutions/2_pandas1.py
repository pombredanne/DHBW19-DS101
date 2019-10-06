def answer_one():
    max_gold = max(df['Gold'])
    ans = df[df['Gold'] == max_gold].index.tolist()
    return ans[0]

answer_one()
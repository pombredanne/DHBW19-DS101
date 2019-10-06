def answer_two():
    x = max(df['Gold'] - df['Gold.1'])
    return df[(df['Gold'] - df['Gold.1']) == x].index.tolist()[0]
    

answer_two()
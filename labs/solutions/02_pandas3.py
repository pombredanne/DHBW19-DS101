def answer_three():
    df_gold = df[(df['Gold']>0) & (df['Gold.1']>0) ]
    df_max_diff = (abs(df_gold['Gold']-df_gold['Gold.1'])/df_gold['Gold.2'])
    
    #return df_max_diff.sort_values(ascending=False).index[0]
    return df_max_diff.idxmax()

answer_three()
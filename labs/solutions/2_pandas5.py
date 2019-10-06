def answer_five():
    return census_df.groupby('STNAME').STNAME.count().idxmax()

answer_five()
def answer_five():
    return census_df.where(census_df['STNAME'] != census_df['CTYNAME']).groupby('STNAME').STNAME.count().idxmax()

answer_five()
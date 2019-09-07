def answer_six():
    counties_df = census_df[census_df['SUMLEV'] == 50]
    top_counties_df = counties_df.sort_values(by=['STNAME','CENSUS2010POP'],ascending=False).groupby('STNAME').head(3)
    ans = top_counties_df.groupby('STNAME').sum().sort_values(by='CENSUS2010POP', ascending=False).head(3).index.tolist()
    return ans

answer_six()


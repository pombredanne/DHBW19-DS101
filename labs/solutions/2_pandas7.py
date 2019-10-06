def answer_seven():
    counties_df = census_df
    counties_df['pop_change'] = abs(counties_df['POPESTIMATE2015'] - counties_df['POPESTIMATE2014'])+abs(counties_df['POPESTIMATE2014'] - counties_df['POPESTIMATE2013'])+abs(counties_df['POPESTIMATE2013'] - counties_df['POPESTIMATE2012'])+abs(counties_df['POPESTIMATE2012'] - counties_df['POPESTIMATE2011'])+abs(counties_df['POPESTIMATE2011'] - counties_df['POPESTIMATE2010'])
    a = max(counties_df['pop_change'])
    ans = counties_df['CTYNAME'][counties_df['pop_change']==a].tolist()
    return ans[0]

answer_seven()
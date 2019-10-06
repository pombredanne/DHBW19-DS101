def answer_eight():
    counties_df = census_df[census_df['SUMLEV'] == 50]
    ans = counties_df[((counties_df['REGION']==1)|(
    	counties_df['REGION']==2))&(
    	counties_df['CTYNAME']=='Washington County')&(
    	counties_df['POPESTIMATE2015']>counties_df['POPESTIMATE2014'])][['STNAME','CTYNAME']]
    return ans

answer_eight()
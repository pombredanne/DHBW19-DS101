df = pd.read_csv('../data/reshape_me.csv')
display(df.head())
df.pivot_table(index=['foo', 'group'], columns='target')
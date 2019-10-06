res = pd.DataFrame(results.loc[results.index!='Intercept',['variant','model']])
# display(res.head())

res['val'] = results.loc[results.index!='Intercept',['Coef.', 'P>|t|', 't']].apply(lambda x: list(map('{:.3f}'.format, list(x))), axis=1)
res['model'] = results.loc[results.index!='Intercept',['model']]
# display(res.head())

res.pivot_table('val', res.index, ['variant', 'model'], lambda x: x)
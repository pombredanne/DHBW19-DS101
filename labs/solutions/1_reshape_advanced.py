res = pd.DataFrame(results.loc[results.index!='Intercept',['variant','model']])
# display(res.head())

res['val'] = results.loc[results.index!='Intercept',['Coef.', 'P>|t|', 't']].apply(lambda x: list(map('{:.3f}'.format, list(x))), axis=1)
res['model'] = results.loc[results.index!='Intercept',['model']]
# display(res.head())

res = res.pivot_table('val', res.index, ['variant', 'model'], lambda x: x)
display(res)

def highlight_significant(x, sign_level_1, sign_level_2):
    if x is np.nan:
        return ''
    else:
        if isinstance(x, list):
            p_value = float(x[2])
            if p_value < sign_level_2:
                return 'font-weight: bold;background-color: lightgreen'
            elif p_value < sign_level_1:
                color = 'lightgreen'
                return 'background-color: %s' % color
            else:
                return ''
        else:
            return ''
res = res.style.applymap(highlight_significant, sign_level_1=0.05, sign_level_2=0.01)
display(res)
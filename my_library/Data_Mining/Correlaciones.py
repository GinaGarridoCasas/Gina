def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

# Función para obtener el Top x de correlaciones más altas que queramos

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

print("Top Absolute Correlations")
print(get_top_abs_correlations(ENS_2017_valida, 34))

# correlacion entre dos variables
Shooting_Accuracy_Goals = df[['Shooting Accuracy','Goals']]
correlation = Shooting_Accuracy_Goals.corr(method='pearson')
correlation


# Heatmap

f, ax = plt.subplots(figsize=(13, 10))
sns.heatmap(Base_TICS_Salud_Fisica.corr(),
           vmin = -1,
           vmax = 1,
            annot = True,
           linewidths = .5)
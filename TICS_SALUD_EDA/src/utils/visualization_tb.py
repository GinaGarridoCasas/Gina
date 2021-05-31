
def tendencia(df, col_name):
  plt.plot(df[col_name])
  plt.savefig("../reports/col_name.jpg", bbox_inches='tight')
  
  return plt.show()

def heatmap (df):
    plt.subplots(figsize=(13, 10))
    sns.set(font_scale=1.5)
    sns.heatmap(df.corr(), vmin = -1, vmax = 1, annot = True, linewidths = .5)

    plt.savefig("../reports/df.jpg", bbox_inches='tight')

    return plt.show()


def scatterplot_Corr_CCAA (df, col_name_x, col_name_y):
    annotations=["Andalucía","Aragón","Asturias, Principado de","Balears, Illes","Canarias","Cant, colabria","Castilla y León","Castilla-La Mancha", "Cataluña","Ceuta","Comunitat Valenciana", "Extremadura","Galicia","Madrid, Comunidad de","Melilla","Murcia, Región de", "Navarra, Comunidad Foral de","País Vasco","Rioja, La", "Total nacional"]

    plt.figure(figsize=(25,8))
    plt.scatter(df['col_name_x'],df['col_name_y'], s=150,color="red")
    plt.xlabel("col_name_x", fontsize = 20)
    plt.ylabel("col_name_y", fontsize = 20)
    plt.title("title",fontsize=25)
    plt.tick_params(labelsize = 15)
    for i, label in enumerate(annotations): 
        plt.text(df['col_name_x'][i], df['col_name_y'][i],label,fontsize = 15)

    plt.savefig("../reports/name_x_col_name_y.jpg", bbox_inches='tight')

    return plt.show()


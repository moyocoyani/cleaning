#If you want a quick visualization of categorical attributes

def vis_cat(dataset,feature,figsize):
    return pd.DataFrame({'Total':dataset.groupby(feature).size()}).sort_values(by='Total').plot.barh(figsize=figsize)

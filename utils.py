def recommender(df, genre):
    '''
    Recomment top rated app from same genre.
    If only single app from that genre -> return randomly from alltime top10
    
    '''
    
    top = df[df['Genres'] == genre].sort_values(by='Rating', ascending=False)
    if top.shape[0] > 1:
        return dict(top.iloc[0])
    else:
        return dict(df.sort_values(by='Rating', ascending=False).iloc[:10].sample(1).squeeze())
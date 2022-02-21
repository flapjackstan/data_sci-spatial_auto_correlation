
import geopandas as gpd
import libpysal as lps

#%%
def get_neighbors(df_index, df, self=False):
    '''
    Parameters
    ----------
    df_index : int
        index of geography you want neighbors from
        
    df : DataFrame
        geodataframe to filter from
        
    self : bool
        include self or not

    Returns
    -------
    neighbors : list 

    '''
    non_empty_records = df[~df['geometry'].is_empty]
    
    wq =  lps.weights.Queen.from_dataframe(non_empty_records)
    
    if self:
        neighbors = [df_index] + wq.neighbors[df_index]
    else:
        neighbors = wq.neighbors[df_index]
    
    return neighbors

#%%
lac_tracts = gpd.read_file('data/lac_tracts.geojson')

neighbors = get_neighbors(12, lac_tracts, True)
lac_tracts.iloc[neighbors].plot()

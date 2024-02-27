import pandas as pd

df_top5pop = pd.DataFrame( {
    
    "country" : ["China" , "India", "United States",  "Indonesia",  "Pakistan"],
    "population" : [1440, 1382, 331, 274, 222],
    "area": [9388211, 2973190, 9147420, 1811570, 770880] 
}
)

print(df_top5pop.head())
from glob import glob

import geopandas
import pandas as pd

joined = None
for i, filepath in enumerate(glob("./data/*.shp")):
  print(i, ": reading " + filepath)
  gdf = geopandas.read_file(filepath, driver="shapefile")
  if i == 0:
    joined = gdf
  else:
    joined = pd.concat([joined, gdf])

joined.to_parquet("tl_2022_us_tabblock20.parquet")

# pip install geopandas
# pip install fiona==1.9.6
# pip install pyarrow
from glob import glob

import geopandas as gp
import pandas as pd

joined = None
for i, filepath in enumerate(glob("./data/*.shp")):
  print("reading " + filepath)
  gdf = gp.read_file(filepath, driver="shapefile")
  if i == 0:
    joined = gdf
  else:
    joined = pd.concat([joined, gdf])

gdf.to_parquet("tl_2022_us_tabblock20.parquet")

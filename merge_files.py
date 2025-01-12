from glob import glob

import geopandas
import pandas as pd


blockgroups = None
for i, filepath in enumerate(glob("./data/*bg.shp")):
  print(i, ": reading " + filepath)
  gdf = geopandas.read_file(filepath, driver="shapefile")
  if i == 0:
    blockgroups = gdf
  else:
    blockgroups = pd.concat([blockgroups, gdf])

blockgroups.to_parquet("tl_2022_us_bg.parquet")

blocks = None
for i, filepath in enumerate(glob("./data/*tabblock20.shp")):
  print(i, ": reading " + filepath)
  gdf = geopandas.read_file(filepath, driver="shapefile")
  if i == 0:
    blocks = gdf
  else:
    blocks = pd.concat([blocks, gdf])

blocks.to_parquet("tl_2022_us_tabblock20.parquet")

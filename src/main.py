from data_pipeline.utils.utils import json_to_csv
import pandas as pd

json_file = "../data/raw/json/ChiangMaiAPD.json"
output_file = "../data/raw/json/ChiangMaiAPD.csv"
json_to_csv(json_file, output_file)

df = pd.read_csv(output_file)
print(df.describe())
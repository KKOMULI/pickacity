### Pick a City

import pandas as pd
import numpy as np
from scipy.stats import rankdata

물가순위 = pd.read_csv("cost_of_living_ver0.1.csv")
치안순위 = pd.read_csv("world_crime_index_ver0.1.csv")

일치도시 = pd.merge(물가순위, 치안순위, on="City", how="inner")

print(일치도시[["City", "Cost of Living Index", "Safety Index"]])

물가점수 = -일치도시["Cost of Living Index"] / 6
치안점수 = 일치도시["Safety Index"]

종합점수 = 물가점수 * 0.7 + 치안점수 * 0.3

종합순위 = rankdata(-종합점수)

일치도시["종합순위"] = 종합순위

print(일치도시[["City", "Cost of Living Index", "Safety Index", "종합순위"]].sort_values(by="종합순위", ascending=True))

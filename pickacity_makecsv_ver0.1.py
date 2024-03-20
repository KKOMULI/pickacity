import pandas as pd
import numpy as np
from scipy.stats import rankdata

물가순위 = pd.read_csv("cost_of_living_ver0.1.csv")
치안순위 = pd.read_csv("world_crime_index_ver0.1.csv")

일치도시 = pd.merge(물가순위, 치안순위, on="City", how="inner")

# "일치도시" 데이터프레임을 CSV 파일로 저장
일치도시.to_csv("일치도시.csv", index=False)

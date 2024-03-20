import pandas as pd
import numpy as np
from scipy.stats import rankdata

물가순위 = pd.read_csv("E:\\2024 SONG\\python\\pickacity\\cost_of_living\\cost_of_living_ver0.3.csv")
치안순위 = pd.read_csv("E:\\2024 SONG\\python\\pickacity\\world_crime_index\\world_crime_index_ver0.3.csv")
관광순위 = pd.read_csv("E:\\2024 SONG\\python\\pickacity\\일치도시_내가정리한데이터\\일치도시_관광객_ver0.1.csv")
거리순위 = pd.read_csv("E:\\2024 SONG\\python\\pickacity\\일치도시_내가정리한데이터\\일치도시_비행시간_ver0.3.csv")

일치도시 = pd.merge(물가순위, 치안순위, on="City", how="inner")
일치도시 = pd.merge(일치도시, 관광순위, on="City", how="inner")
일치도시 = pd.merge(일치도시, 거리순위, on="City", how="inner")

# "일치도시" 데이터프레임을 CSV 파일로 저장
일치도시.to_csv("totaldata_ver0.2.csv", index=False)
import pandas as pd
from scipy.stats import rankdata

data = pd.read_csv("E:\\2024 SONG\\python\\pickacity\\totaldata_ver0.2.csv")
data = data.dropna()

### Cost of Living
CostofLiving = pd.to_numeric(data.loc[:, "Cost of Living Index"], errors='coerce')
CostofLiving.fillna(CostofLiving.mean(), inplace=True)

mean1 = CostofLiving.mean()
std_dev1 = CostofLiving.std()

print("Cost of Living 평균:", mean1)
print("Cost of Living 표준 편차:", std_dev1)

standard_scores_costofliving = (mean1 - CostofLiving) / std_dev1

min_score_costofliving = standard_scores_costofliving.min()
max_score_costofliving = standard_scores_costofliving.max()

mapped_scores_costofliving = 100 * (standard_scores_costofliving - min_score_costofliving) / (max_score_costofliving - min_score_costofliving)

print(mapped_scores_costofliving)


### Flight Time
FlightTime = pd.to_numeric(data.loc[:, "Flight Time"], errors='coerce')
FlightTime.fillna(FlightTime.mean(), inplace=True)

mean2 = FlightTime.mean()
std_dev2 = FlightTime.std()

standard_scores_flighttime = (mean2 - FlightTime) / std_dev2

min_score_flighttime = standard_scores_flighttime.min()
max_score_flighttime = standard_scores_flighttime.max()

mapped_scores_flighttime = 100 * (standard_scores_flighttime - min_score_flighttime) / (max_score_flighttime - min_score_flighttime)

print(mapped_scores_flighttime)


### Safety Index
SafetyIndex = pd.to_numeric(data.loc[:, "Safety Index"], errors='coerce')
SafetyIndex.fillna(SafetyIndex.mean(), inplace=True)

mean3 = SafetyIndex.mean()
std_dev3 = SafetyIndex.std()

standard_scores_safetyindex = (SafetyIndex - mean3) / std_dev3

min_score_safetyindex = standard_scores_safetyindex.min()
max_score_safetyindex = standard_scores_safetyindex.max()

mapped_scores_safetyindex = 100 * (standard_scores_safetyindex - min_score_safetyindex) / (max_score_safetyindex - min_score_safetyindex)

print(mapped_scores_safetyindex)


### Tourism Ranking
TourismRanking = pd.to_numeric(data.loc[:, "Tourism Ranking"], errors='coerce')

min_ranking = min(TourismRanking)
max_ranking = max(TourismRanking)

mapped_scores_tourismranking = 100 * (max_ranking - TourismRanking + 1) / (max_ranking - min_ranking + 1)

print(mapped_scores_tourismranking)


### Total Scores
TotalScores = mapped_scores_safetyindex * 0.4 + mapped_scores_tourismranking * 0.3 + mapped_scores_costofliving * 0.1 + mapped_scores_flighttime * 0.1

TotalRanking = rankdata(-TotalScores)

data["Total Ranking"] = TotalRanking

print(data[["City", "Total Ranking"]].sort_values(by="Total Ranking", ascending=True))

import pandas as pd
from scipy.stats import rankdata

data = pd.read_csv("E:\\2024 SONG\\python\\pickacity\\totaldata_ver0.3.csv")


### Cost of Living
CostofLiving = pd.to_numeric(data.loc[:, "Cost of Living Index"], errors='coerce')

mean1 = CostofLiving.mean()
std_dev1 = CostofLiving.std()

standard_scores_costofliving = (mean1 - CostofLiving) / std_dev1

min_score_costofliving = standard_scores_costofliving.min()
max_score_costofliving = standard_scores_costofliving.max()

mapped_scores_costofliving = 100 * (standard_scores_costofliving - min_score_costofliving) / (max_score_costofliving - min_score_costofliving)

# print(mapped_scores_costofliving)


### Flight Time
FlightTime = pd.to_numeric(data.loc[:, "Flight Time"], errors='coerce')

mean2 = FlightTime.mean()
std_dev2 = FlightTime.std()

standard_scores_flighttime = (mean2 - FlightTime) / std_dev2

min_score_flighttime = standard_scores_flighttime.min()
max_score_flighttime = standard_scores_flighttime.max()

mapped_scores_flighttime = 100 * (standard_scores_flighttime - min_score_flighttime) / (max_score_flighttime - min_score_flighttime)

# print(mapped_scores_flighttime)


### Safety Index
SafetyIndex = pd.to_numeric(data.loc[:, "Safety Index"], errors='coerce')

mean3 = SafetyIndex.mean()
std_dev3 = SafetyIndex.std()

standard_scores_safetyindex = (SafetyIndex - mean3) / std_dev3

min_score_safetyindex = standard_scores_safetyindex.min()
max_score_safetyindex = standard_scores_safetyindex.max()

mapped_scores_safetyindex = 100 * (standard_scores_safetyindex - min_score_safetyindex) / (max_score_safetyindex - min_score_safetyindex)

# print(mapped_scores_safetyindex)


### Tourism Ranking
TourismRanking = pd.to_numeric(data.loc[:, "Tourism Ranking"], errors='coerce')

min_ranking = min(TourismRanking)
max_ranking = max(TourismRanking)

mapped_scores_tourismranking = 100 * (max_ranking - TourismRanking + 1) / (max_ranking - min_ranking + 1)

# print(mapped_scores_tourismranking)


### Total Scores
CostofLiving_weightedvalue = int(input("물가의 중요도:"))
FlightTime_weightedvalue = int(input("비행시간의 중요도:"))
SafetyIndex_weightedvalue = int(input("치안의 중요도:"))
TourismRanking_weightedvalue = int(input("관광의 중요도:"))

TotalScores = mapped_scores_safetyindex * SafetyIndex_weightedvalue + mapped_scores_tourismranking * TourismRanking + mapped_scores_costofliving * CostofLiving_weightedvalue + mapped_scores_flighttime * FlightTime_weightedvalue

TotalRanking = rankdata(-TotalScores)

data["Total Ranking"] = TotalRanking

print(data[["City", "Total Ranking"]].sort_values(by="Total Ranking", ascending=True).head(10))

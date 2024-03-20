import pandas as pd
from scipy.stats import rankdata
import streamlit as st

def calculate_total_ranking(data, costofliving_weight, flighttime_weight, safetyindex_weight, tourismranking_weight):
    # Calculate scores
    CostofLiving = pd.to_numeric(data["Cost of Living Index"], errors='coerce')
    mean1 = CostofLiving.mean()
    std_dev1 = CostofLiving.std()
    standard_scores_costofliving = (mean1 - CostofLiving) / std_dev1
    min_score_costofliving = standard_scores_costofliving.min()
    max_score_costofliving = standard_scores_costofliving.max()
    mapped_scores_costofliving = 100 * (standard_scores_costofliving - min_score_costofliving) / (max_score_costofliving - min_score_costofliving)

    FlightTime = pd.to_numeric(data["Flight Time"], errors='coerce')
    mean2 = FlightTime.mean()
    std_dev2 = FlightTime.std()
    standard_scores_flighttime = (mean2 - FlightTime) / std_dev2
    min_score_flighttime = standard_scores_flighttime.min()
    max_score_flighttime = standard_scores_flighttime.max()
    mapped_scores_flighttime = 100 * (standard_scores_flighttime - min_score_flighttime) / (max_score_flighttime - min_score_flighttime)

    SafetyIndex = pd.to_numeric(data["Safety Index"], errors='coerce')
    mean3 = SafetyIndex.mean()
    std_dev3 = SafetyIndex.std()
    standard_scores_safetyindex = (SafetyIndex - mean3) / std_dev3
    min_score_safetyindex = standard_scores_safetyindex.min()
    max_score_safetyindex = standard_scores_safetyindex.max()
    mapped_scores_safetyindex = 100 * (standard_scores_safetyindex - min_score_safetyindex) / (max_score_safetyindex - min_score_safetyindex)

    TourismRanking = pd.to_numeric(data["Tourism Ranking"], errors='coerce')
    min_ranking = min(TourismRanking)
    max_ranking = max(TourismRanking)
    mapped_scores_tourismranking = 100 * (max_ranking - TourismRanking + 1) / (max_ranking - min_ranking + 1)

    # Calculate Total Scores
    TotalScores = (mapped_scores_safetyindex * safetyindex_weight + 
                   mapped_scores_tourismranking * tourismranking_weight + 
                   mapped_scores_costofliving * costofliving_weight + 
                   mapped_scores_flighttime * flighttime_weight)
    TotalRanking = rankdata(-TotalScores)
    data["Total Ranking"] = TotalRanking
    return data[["City", "Total Ranking"]].sort_values(by="Total Ranking", ascending=True).reset_index(drop=True).head(10)

def main():
    st.title("Pick a City")
    st.subheader("당신만을 위한 맞춤형 여행지를 확인하세요.")

    # Load data
    data = pd.read_csv("E:\\2024 SONG\\python\\pickacity\\totaldata_ver0.3.csv")

    # Input weights
    st.sidebar.header("중요도 설정")
    costofliving_weight = st.sidebar.slider("물가 중요도", min_value=0, max_value=10, value=5)
    flighttime_weight = st.sidebar.slider("비행시간 중요도", min_value=0, max_value=10, value=5)
    safetyindex_weight = st.sidebar.slider("치안 중요도", min_value=0, max_value=10, value=5)
    tourismranking_weight = st.sidebar.slider("관광 중요도", min_value=0, max_value=10, value=5)

    # Calculate and display
    result = calculate_total_ranking(data, costofliving_weight, flighttime_weight, safetyindex_weight, tourismranking_weight)
    st.write(result)

if __name__ == "__main__":
    main()

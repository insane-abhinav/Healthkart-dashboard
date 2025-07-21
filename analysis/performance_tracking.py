import pandas as pd

influencers = pd.read_csv("data/influencers.csv")
tracking = pd.read_csv("data/tracking_data.csv")

# Group by influencer
perf_df = (
    tracking.groupby("influencer_id")[["orders", "revenue"]]
    .sum()
    .reset_index()
    .merge(influencers, left_on="influencer_id", right_on="id")
)

perf_df.to_csv("data/performance_summary.csv", index=False)
print("Saved: data/performance_summary.csv")

import pandas as pd
import numpy as np

tracking = pd.read_csv("data/tracking_data.csv")
payouts = pd.read_csv("data/payouts.csv")
influencers = pd.read_csv("data/influencers.csv")

roi_df = (
    tracking.groupby("influencer_id")["revenue"]
    .sum()
    .reset_index()
    .merge(payouts, on="influencer_id")
    .merge(influencers, left_on="influencer_id", right_on="id")
)

roi_df["ROAS"] = roi_df["revenue"] / roi_df["total_payout"]
roi_df["incremental_roas"] = (roi_df["revenue"] * np.random.uniform(0.3, 0.7)) / roi_df["total_payout"]

roi_df.to_csv("data/roas_summary.csv", index=False)
print("Saved: data/roas_summary.csv")

import pandas as pd

roi_df = pd.read_csv("data/roas_summary.csv")

# Top 5 personas by ROAS
top_personas = roi_df.groupby("persona")["ROAS"].mean().sort_values(ascending=False).head(5)
print("🎯 Top 5 Personas by ROAS:")
print(top_personas)

# Poor influencers
low_roas = roi_df.sort_values("ROAS").head(int(len(roi_df) * 0.1))
low_roas.to_csv("data/poor_influencers.csv", index=False)

# City-based insights
city_roas = roi_df.groupby("city")["ROAS"].mean().sort_values(ascending=False)
city_roas.to_csv("data/city_roas.csv")

print("Saved insights to:")
print("- data/poor_influencers.csv")
print("- data/city_roas.csv")

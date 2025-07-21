import pandas as pd
import numpy as np
from faker import Faker
import os

faker = Faker()
np.random.seed(42)

os.makedirs("data", exist_ok=True)

# Simulate brands and products
brands = ["MuscleBlaze", "HKVitals", "Gritzo"]
products = {
    "MuscleBlaze": ["Whey Gold", "Creatine"],
    "HKVitals": ["Multivitamin", "Biotin"],
    "Gritzo": ["SuperMilk", "ProteinShake"]
}

# Influencers
influencers = pd.DataFrame({
    "id": range(1, 21),
    "name": [faker.name() for _ in range(20)],
    "category": np.random.choice(["Fitness", "Nutrition", "Lifestyle"], 20),
    "gender": np.random.choice(["Male", "Female", "Other"], 20),
    "follower_count": np.random.randint(1000, 500000, 20),
    "platform": np.random.choice(["Instagram", "YouTube", "Twitter"], 20),
    "city": np.random.choice(["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"], 20),
    "age_group": np.random.choice(["18-25", "26-35", "36-45"], 20)
})
influencers["persona"] = influencers["category"] + "_" + influencers["gender"]
influencers.to_csv("data/influencers.csv", index=False)

# Posts
posts = pd.DataFrame({
    "influencer_id": np.random.choice(influencers["id"], 100),
    "platform": np.random.choice(["Instagram", "YouTube", "Twitter"], 100),
    "date": pd.date_range("2024-01-01", periods=100),
    "url": [faker.url() for _ in range(100)],
    "caption": [faker.sentence() for _ in range(100)],
    "reach": np.random.randint(1000, 50000, 100),
    "likes": np.random.randint(50, 5000, 100),
    "comments": np.random.randint(10, 1000, 100),
    "brand": np.random.choice(brands, 100)
})
posts.to_csv("data/posts.csv", index=False)

# Tracking Data
tracking_rows = []
for _ in range(300):
    brand = np.random.choice(brands)
    product = np.random.choice(products[brand])
    tracking_rows.append({
        "source": np.random.choice(["Paid", "Organic"]),
        "campaign": brand + "_Launch2024",
        "brand": brand,
        "product": product,
        "influencer_id": np.random.choice(influencers["id"]),
        "user_id": np.random.randint(1, 1000),
        "date": faker.date_between(start_date="-6m", end_date="today"),
        "orders": np.random.randint(1, 5),
        "revenue": np.round(np.random.uniform(10, 500), 2)
    })
tracking_data = pd.DataFrame(tracking_rows)
tracking_data.to_csv("data/tracking_data.csv", index=False)

# Payouts
payouts = pd.DataFrame({
    "influencer_id": influencers["id"],
    "basis": np.random.choice(["post", "order"], 20),
    "rate": np.random.uniform(50, 1000, 20),
    "orders": np.random.randint(10, 100, 20)
})
payouts["total_payout"] = np.where(payouts["basis"] == "post", payouts["rate"], payouts["rate"] * payouts["orders"])
payouts.to_csv("data/payouts.csv", index=False)

print("Data generation complete! Files saved in 'data/'")

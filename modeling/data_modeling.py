"""
Defines the data schema and key structure used in HealthKart influencer dashboard.
"""

# Schema overview for documentation and validation purposes

INFLUENCER_SCHEMA = {
    'id': int,
    'name': str,
    'category': str,
    'gender': str,
    'follower_count': int,
    'platform': str,
    'city': str,
    'age_group': str,
    'persona': str
}

POST_SCHEMA = {
    'influencer_id': int,
    'platform': str,
    'date': 'datetime',
    'url': str,
    'caption': str,
    'reach': int,
    'likes': int,
    'comments': int,
    'brand': str
}

TRACKING_SCHEMA = {
    'source': str,
    'campaign': str,
    'brand': str,
    'product': str,
    'influencer_id': int,
    'user_id': int,
    'date': 'datetime',
    'orders': int,
    'revenue': float
}

PAYOUT_SCHEMA = {
    'influencer_id': int,
    'basis': str,
    'rate': float,
    'orders': int,
    'total_payout': float
}

import numpy as np
import pandas as pd
from models.bandit_model import EpsilonGreedyBandit

# Read the CSV data
data = pd.read_csv('data/user_interactions.csv')

# Extract unique video IDs
unique_videos = data['Video_ID'].unique()
n_items = len(unique_videos)

# Create a mapping from video IDs to indices
video_to_index = {video: idx for idx, video in enumerate(unique_videos)}

def get_user_feedback(row):
    # Use the 'Ratings' column as a proxy for user feedback (reward)
    return row['Ratings']

def main():
    bandit = EpsilonGreedyBandit(n_items)

    # Update the bandit model with user data
    for _, row in data.iterrows():
        video_id = row['Video_ID']
        recommended_item = video_to_index[video_id]
        reward = get_user_feedback(row)
        bandit.update(recommended_item, reward)

    # Get the indices of top 10 recommended videos based on Values (rewards)
    top_indices = np.argsort(bandit.values)[::-1][:10]
    top_videos = [unique_videos[idx] for idx in top_indices]

    # Print or return the top recommended videos
    print("Top 10 Recommended Videos:")
    for rank, video_id in enumerate(top_videos, start=1):
        print(f"{rank}. Video ID: {video_id}")

if __name__ == "__main__":
    main()


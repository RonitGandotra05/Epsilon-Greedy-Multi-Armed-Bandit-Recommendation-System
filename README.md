# Multi-Armed Bandit Recommendation System

# Overview
This project implements a recommendation system using the Multi-Armed Bandit (MAB) algorithm. The goal is to optimize decision-making processes for recommending videos to users based on their interactions and feedback.

# Files Structure
recommendation-system/
├── data/
│ └── user_interactions.csv
├── models/
│ └── bandit_model.py
├── tests/
│ └── test_bandit_model.py
├── main.py
├── requirements.txt
└── README.md

# Input Data

The input data (`user_interactions.csv`) contains streaming app viewership data with columns such as User_ID, Video_ID, Ratings, and more, providing insights into user interactions with videos.

# How It Works

# Initialization

The system initializes with each video treated as an arm in the MAB model, starting with no prior knowledge about the potential rewards of each video.

# Exploration

The system recommends various videos to users to gather initial feedback, estimating the reward potential of each video.

# Exploitation

Based on the feedback received, the system starts favoring videos with higher estimated rewards to maximize user satisfaction by recommending popular and well-rated videos.

# Continuous Learning

The system continuously updates its understanding of each video's reward potential as more data is collected, ensuring dynamically optimized recommendations over time.

# Output Explanation

After running the model, you will obtain two key outputs: Counts and Values.

# Counts

The Counts array shows how many times each video has been recommended. For example:
- `Counts: [77, 61, 52, 64, 54, ...]`
  - Each element represents a specific video.
  - `Counts[0] = 77` means the first video was recommended 77 times.

# Values

The Values array shows the estimated average reward for each video based on user feedback. For example:
- `Values: [3.25, 2.85, 2.90, 2.87, 2.89, ...]`
  - Each element represents a specific video.
  - `Values[0] = 3.25` means the estimated average reward for the first video is approximately 3.25.

# Practical Use

# Recommendation Decisions

Videos with higher Values are more likely to be recommended due to positive feedback. The Counts data ensures less popular videos are also explored to gather more data.

# Performance Insights

Analyzing Counts and Values helps understand user preferences and video performance, guiding improvements in content offerings and recommendation strategies.

# Running the Code

To run the recommendation system:

1. Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt


2. Run the main script:
   python main.py

3. To run the tests:
    python -m unittest discover -s tests

# Example Output

Counts: [77, 61, 52, 64, 54, ...]
Values: [3.25, 2.85, 2.90, 2.87, 2.89, ...]

This output indicates how many times each video was recommended and their respective estimated average rewards.

# Conclusion

By utilizing the Multi-Armed Bandit algorithm, this recommendation system dynamically learns and adapts to user preferences, ensuring optimal content recommendations to enhance user satisfaction.

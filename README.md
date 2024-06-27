# Multi-Armed Bandit Recommendation System

# Overview
This project implements a recommendation system using the Multi-Armed Bandit (MAB) algorithm. The goal is to optimize decision-making processes for recommending videos to users based on their interactions and feedback.

# Input Data
The input data (`user_interactions.csv`) contains streaming app viewership data with columns such as User_ID, Video_ID, Ratings, and more, providing insights into user interactions with videos.

# How It Works

### Initialization

The system initializes with each video treated as an arm in the MAB model, starting with no prior knowledge about the potential rewards of each video.

### Exploration

The system recommends various videos to users to gather initial feedback, estimating the reward potential of each video.

### Exploitation

Based on the feedback received, the system starts favoring videos with higher estimated rewards to maximize user satisfaction by recommending popular and well-rated videos.

### Continuous Learning

The system continuously updates its understanding of each video's reward potential as more data is collected, ensuring dynamically optimized recommendations over time.

# Output Explanation

After running the model, you will obtain two key outputs: Counts and Values.

### Counts

The Counts array shows how many times each video has been recommended. For example:
- `Counts: [77, 61, 52, 64, 54, ...]`
  - Each element represents a specific video.
  - `Counts[0] = 77` means the first video was recommended 77 times.

### Values

The Values array shows the estimated average reward for each video based on user feedback. For example:
- `Values: [3.25, 2.85, 2.90, 2.87, 2.89, ...]`
  - Each element represents a specific video.
  - `Values[0] = 3.25` means the estimated average reward for the first video is approximately 3.25.

# Practical Use

### Integration with Instagram-like Applications

If you intend to integrate this recommendation system into applications similar to Instagram, follow these steps for seamless integration:

### Backend Integration

1. **API Endpoint Setup**: Create an API endpoint within your backend application that communicates with the recommendation system. This endpoint should accept user data relevant to video interactions and return recommended video IDs based on the Multi-Armed Bandit model's predictions.

2. **Data Handling**: Ensure your backend can manage and process user data such as user interactions, preferences, and video metadata. This data will serve as input for the recommendation system.

3. **Model Interaction**: Implement logic in your backend to call the recommendation model, which is implemented in `main.py` or imported from `bandit_model.py`. This logic should process incoming user data and generate recommendations dynamically.

4. **Response Formatting**: Format the recommendation responses from the model into a suitable format (e.g., JSON) that can be easily consumed by frontend applications.

###Frontend Integration

1. **API Consumption**: Develop frontend components using frameworks like React, Angular, or Vue.js that interact with your backend API endpoint. These components should fetch recommended video IDs and display them in a user-friendly format.

2. **User Interface Design**: Design user interfaces that seamlessly integrate recommended videos into the user experience. Consider aspects such as thumbnail previews, titles, and user feedback options (e.g., like buttons).

3. **Feedback Mechanism**: Implement mechanisms for users to provide feedback on recommended videos (e.g., likes or dislikes). This feedback loop is crucial for the Multi-Armed Bandit algorithm to continuously optimize recommendations based on user interactions.

4. **Real-time Updates**: Ensure that the frontend components update in real-time as new recommendations are fetched or as user preferences evolve.

By following these integration steps, you can effectively integrate the Multi-Armed Bandit Recommendation System into Instagram-like applications. This setup enhances user engagement by providing personalized video recommendations tailored to individual preferences.

# Running the Code

To run the recommendation system:

1. Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt


2. Run the main script:
   ```bash
   python main.py

4. To run the tests:
   ```bash
    python -m unittest discover -s tests

# Example Output

Counts: [77, 61, 52, 64, 54, ...]
Values: [3.25, 2.85, 2.90, 2.87, 2.89, ...]

This output indicates how many times each video was recommended and their respective estimated average rewards.

# Advantage of using Multi-Armed Bandit (MAB) Recommendation System over traditional systems:
### Real-Time Adaptation: 
Adjusts recommendations in real-time based on immediate user feedback, ensuring current preferences are reflected promptly.

### Balanced Exploration and Exploitation: 
Efficiently balances trying new content (exploration) with promoting proven favorites (exploitation), enhancing user satisfaction.

### Quick Learning: 
Learns quickly from user interactions, adapting recommendations dynamically as preferences evolve.

### Application Flexibility: 
Versatile across various domains beyond recommendations, handling uncertainty and optimizing decisions in diverse settings.

### Efficiency: 
Optimizes user engagement efficiently, providing timely and personalized content updates.
# Conclusion

By utilizing the Multi-Armed Bandit algorithm, this recommendation system dynamically learns and adapts to user preferences, ensuring optimal content recommendations to enhance user satisfaction.

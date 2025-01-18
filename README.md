Project Overview
The Quiz Performance Analyzer is a Python-based solution designed to help students analyze their quiz performance and receive personalized recommendations to improve their preparation. The tool leverages both historical and current quiz data to generate insights into weak areas, trends, and strengths. Additionally, it defines a student persona based on their performance, providing actionable recommendations for focused improvement.

1. Analyze current and historical quiz data.
2. Calculate performance metrics by topic and difficulty level.
3. Highlight weak topics based on response accuracy.
4. Provide personalized improvement recommendations.
5. Define a student persona (e.g., High Performer, Improver, Struggler).

Data Used
The solution works with two datasets:
1. Current Quiz Data:Latest quiz submissions including responses by topic, difficulty, and correctness.
2. Historical Quiz Data:Performance data from previous quizzes including response maps and scores.

 1. Data Fetching
Simulated data for current and historical quizzes is fetched via two mock API functions:
- fetch_current_quiz: Simulates the latest quiz data.
- fetch_historical_quiz: Simulates historical data from the last five quizzes.
 2. Data Analysis
The analyze_data function combines current and historical quiz data to:
- Calculate accuracy by topic and difficulty.
- Identify weak topics (accuracy < 50%).
 3. Recommendations
The generate_recommendations function uses weak topics to suggest:
- Topics for targeted improvement.
- Specific strategies for practicing question types.
4. Persona Definition
The define_persona function classifies users into categories:
- High Performer: Accuracy ≥ 80%.
- Improver: 50% ≤ Accuracy < 80%.
- Struggler: Accuracy < 50%.

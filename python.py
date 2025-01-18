import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# for fetching current quiz data
def fetch_current_quiz():
    data = {
        "user_id":1,
        "quiz_id":101,
        "responses":[
            {"question_id":1,"topic":"math","difficulty":"easy","correct":False},
            {"question_id":2,"topic":"science","difficulty":"medium","correct":True},
            {"question_id":3,"topic":"math","difficulty":"hard","correct":False},
            {"question_id":4,"topic":"english","difficulty":"medium","correct":True} 
      ]                                                             
    }
    return pd.Dataframe(data["responses"])

# for fetching historical data
def fetch_historical_quiz():
    data=[
        {
            "quiz_id":95,
            "responses":[
                {"question_id":1,"topic":"math","difficulty":"easy","correct":True},
                {"question_id":2,"topic":"science","difficulty":"medium","correct":True},
                {"question_id":3,"topic":"english","difficulty":"hard","correct":False},
                 
            ]
        },
        {
            "quiz_id":96,
            "responses":[
                {"question_id":1,"topic":"math","difficulty":"medium","correct":False},
                {"question_id":2,"topic":"science","difficulty":"easy","correct":True},
                {"question_id":3,"topic":"english","difficulty":"hard","correct":False},
            ]
        }
    ]
    responses=[] # to collect all responses in a list
    for quiz in data:
        for response in quiz["responses"]:
            response["quiz_id"]=quiz["quiz_id"]
            responses.append(response)
    return pd.Dataframe(responses)

# for analyzing accuracy
def analyze_data(current_quiz,historical_data):
    combined_data=pd.concat([historical_data,current_quiz],ignore_index=true)  #combine historical and current data into one dataframe
    topic_accuracy=combined_data.groupby("topic").correct.mean()*100
    difficulty_accuracy=combined_data.groupby("difficulty").correct.mean()*100
    weak_topics=topic_accuracy[topic_accuracy<50].sort_values()
    return topic_accuracy,difficulty_accuracy,weak_topics

#providing feedback
def generate_recommendations(weak_topics):
    recommendations=[]
for topic,accuracy in weak_topics.items():
    recommendations.append(
        f"Focus on '{topic}': your accuracy is {accuracy:.2f}%.practice more."
    )
return recommendations 

#categorizing students
def define_persona(accuracy_data):
    avg_accuracy=accuracy_data.correct.mean()*100
    if avg_accuracy >=80:
        return "outstanding :keep challenging yourself."
    elif avg_accuracy >=50:
        return "improver :can improve more."
    else:
        return "struggler :focus on the fundamentals."
    
if __name__== "__main__":
    print("fetching data...")
    current_quiz=fetch_current_quiz()
    historical_data=fetch_historical_quiz(
    
    print("analyzing data...")
    topic_accuracy,difficulty_accuracy,weak_topics=analyze_data(current_quiz,historical_data)

    print("generating insights...")
    print("\nweak topics:")
    for topic,acc in weak_topics.items():
    print(f" -{topic}: {acc:.2f}% accuracy")

    print("\ngenerating recommendations...")
    recommendations =generate_recommendations(weak_topics)
    for rec in recommendations:
    print(f" - {rec}")

    persona=define_persona(pd.concat([historical_data,current_quiz],ignore_index=True))
    print(f"\nstudent persona: {persona}")
    )
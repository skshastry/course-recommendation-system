
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from fastapi import FastAPI

app = FastAPI()

# Dummy data
users = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'desired_skills': [
        "machine learning, data science, python",
        "web development, javascript, react",
        "cloud computing, aws, devops",
        "cybersecurity, network security, ethical hacking",
        "digital marketing, seo, content writing"
    ]
})

courses = pd.DataFrame({
    'course_id': [1, 2, 3, 4, 5],
    'course_name': [
        "Intro to Machine Learning", 
        "Full Stack Web Development with React", 
        "AWS Cloud Practitioner", 
        "Advanced Network Security", 
        "SEO for Digital Marketers"
    ],
    'skills_covered': [
        "machine learning, python", 
        "web development, react, javascript", 
        "cloud computing, aws", 
        "network security, cybersecurity", 
        "seo, digital marketing"
    ]
})

# Feature Engineering: Combine the skills into a matrix
vectorizer = CountVectorizer().fit_transform(courses['skills_covered'])
skills_matrix = cosine_similarity(vectorizer)

@app.post("/recommend")
async def recommend_courses(user_skills: str):
    # Preprocess user skills and make recommendations
    user_skills_vector = CountVectorizer().fit(courses['skills_covered']).transform([user_skills])
    similarity_scores = cosine_similarity(user_skills_vector, skills_matrix)
    recommended_courses = courses.loc[similarity_scores.argsort()[0, ::-1]].head(3)
    return recommended_courses.to_dict(orient='records')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

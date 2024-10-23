Course Recommendation System

This project is a **Course Recommendation System** that suggests courses to users based on their desired skills. It uses **content-based filtering** to match users' skills with relevant courses from various platforms (e.g., Coursera, Udemy, edX). The system is deployed using **FastAPI** for real-time recommendations.

## Features

- Suggests courses based on users' desired skills.
- Matches user skills with course content using **cosine similarity**.
- Provides a REST API endpoint using **FastAPI** for real-time interaction.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- Uvicorn (for ASGI server)

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/course-recommendation-system.git
   cd course-recommendation-system
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API:**

   After starting the server, the API can be accessed at `http://127.0.0.1:8000/recommend`.

### Usage

You can make POST requests to the `/recommend` endpoint to get course recommendations based on user skills.

**Example request (using `curl`):**

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/recommend' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_skills": "machine learning, python"
}'
```

### Example Response:

```json
[
  {
    "course_id": 1,
    "course_name": "Intro to Machine Learning",
    "skills_covered": "machine learning, python",
    "platform": "Coursera"
  },
  {
    "course_id": 3,
    "course_name": "AWS Cloud Practitioner",
    "skills_covered": "cloud computing, aws",
    "platform": "edX"
  }
]
```

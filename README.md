```markdown
# 🚨 CriSense - AI-Powered Crisis Intelligence Platform

CriSense is a full-stack machine learning web application that classifies disaster-related tweets into humanitarian categories in real time. The platform uses Natural Language Processing (NLP) and Machine Learning to assist in crisis monitoring, disaster response, and humanitarian intelligence.

---

# 🌟 Features

## 🔍 Real-Time Tweet Classification
- Classifies disaster-related tweets into multiple humanitarian categories.
- Displays prediction confidence scores.

## 📊 Interactive Analytics Dashboard
- Pie Chart for prediction distribution
- Bar Chart for category frequency
- Total predictions statistics
- Most common disaster category

## 📜 Prediction History
- Stores previous predictions in SQLite database.
- Displays historical prediction records.

## 📂 Batch CSV Prediction
- Upload CSV files containing tweets.
- Predict categories for multiple tweets simultaneously.
- Stores batch predictions in the database.

## 🤖 Machine Learning Integration
- Trained using:
  - Scikit-Learn
  - TF-IDF Vectorization
  - Logistic Regression

## 🌐 Full Stack Development
- Django Backend
- Bootstrap Frontend
- Plotly Interactive Charts
- SQLite Database

---

# 🏷️ Humanitarian Categories

The model predicts the following categories:

1. caution_and_advice
2. displaced_people_and_evacuations
3. infrastructure_and_utility_damage
4. injured_or_dead_people
5. missing_or_found_people
6. not_humanitarian
7. other_relevant_information
8. requests_or_urgent_needs
9. rescue_volunteering_or_donation_effort
10. sympathy_and_support

---

# 🛠️ Tech Stack

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- Plotly

## Backend
- Python
- Django

## Machine Learning
- Scikit-Learn
- Pandas
- NumPy
- NLP (TF-IDF)

## Database
- SQLite

## Version Control
- Git
- GitHub

## Cloud (Planned)
- AWS EC2
- Nginx
- Gunicorn
- PostgreSQL (RDS)
- Amazon S3

---

# 📁 Project Structure

CriSense/
│
├── config/
├── crisisintel/
│ ├── templates/
│ ├── static/
│ ├── views.py
│ ├── models.py
│ ├── services.py
│ └── urls.py
│
├── model.pkl
├── requirements.txt
├── manage.py
├── README.md
└── .gitignore

---

# ⚙️ Installation and Setup

## Step 1: Clone Repository

git clone https://github.com/rajpratapsinghsisodiya75-alt/CriSense.git

cd CriSense

---

## Step 2: Create Virtual Environment

Windows:

python -m venv env

env\Scripts\activate

Linux/Mac:

python3 -m venv env

source env/bin/activate

---

## Step 3: Install Dependencies

pip install -r requirements.txt

---

## Step 4: Apply Database Migrations

python manage.py migrate

---

## Step 5: Create Admin User (Optional)

python manage.py createsuperuser

---

## Step 6: Run Development Server

python manage.py runserver

---

# 🌐 Open Application

Dashboard:

http://127.0.0.1:8000/

Admin Panel:

http://127.0.0.1:8000/admin/

Prediction History:

http://127.0.0.1:8000/history/

CSV Upload:

http://127.0.0.1:8000/upload/

---

# 📂 CSV Upload Format

The uploaded CSV file must contain a column named:

tweet

Example:

tweet
People need food and water immediately
Roads blocked due to flooding
Donations are being collected
Bridge collapsed after earthquake

---

# 📈 Model Performance

Model Accuracy: 74.69%

Classification Report:

- High performance on:
  - rescue_volunteering_or_donation_effort
  - injured_or_dead_people
  - infrastructure_and_utility_damage

- Moderate performance on:
  - requests_or_urgent_needs
  - caution_and_advice
  - other_relevant_information

---

# 🚀 Future Enhancements

- AWS EC2 Deployment
- PostgreSQL Integration
- Amazon S3 File Storage
- User Authentication System
- Live Twitter API Integration
- Real-Time Disaster Monitoring
- Sentiment Analysis
- Explainable AI (SHAP/LIME)
- REST API using Django REST Framework
- Docker Containerization
- CI/CD Pipeline using GitHub Actions

---

# 💼 Resume Highlights

✔ Full Stack Django Application

✔ Machine Learning Integration

✔ Natural Language Processing (NLP)

✔ Interactive Analytics Dashboard

✔ Batch Prediction System

✔ Database Management

✔ Git & GitHub Version Control

✔ Cloud Deployment Ready

---

# 👨‍💻 Author

Pratap Singh Sisodiya

Computer Science and Engineering Student

GitHub:
https://github.com/rajpratapsinghsisodiya75-alt

---

⭐ If you found this project useful, please consider giving it a star.
```

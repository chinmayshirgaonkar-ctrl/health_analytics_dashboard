# 🏃‍♂️ Personal Health & Sentiment Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]https://healthanalyticsdashboard-ddj7j5ayk4durmxpdepcm2.streamlit.app/
## 📌 Overview
The **Personal Health & Sentiment Analytics Dashboard** is a responsive data application built to track and correlate quantitative physical metrics (steps, sleep, resting heart rate) with qualitative daily well-being. 

Designed for individuals engaged in rigorous physical conditioning—such as marathon preparation and weight training—this tool combines physiological data with Natural Language Processing (NLP) to provide a holistic view of human performance, mood, and recovery.

## 🚀 Live Demo
https://healthanalyticsdashboard-ddj7j5ayk4durmxpdepcm2.streamlit.app/

## ✨ Key Features
* **KPI Monitoring:** Real-time tracking of dynamic averages for daily steps, sleep duration, and resting heart rate.
* **Sentiment Analysis:** Utilizes `TextBlob` to process unstructured daily text logs, assigning polarity scores to gauge mood and fatigue levels.
* **Multivariate Visualizations:** * Dual-axis timeline mapping step volume against rolling sentiment trends.
  * Interactive scatter plots mapping sleep duration vs. resting heart rate, sized by activity volume and colored by mood polarity.
* **Raw Data Registry:** A sortable, embedded dataframe logging qualitative notes alongside their calculated NLP sentiment scores.

## 🛠️ Technology Stack
* **Language:** Python
* **Framework:** Streamlit
* **Data Manipulation:** Pandas
* **Visualization:** Plotly
* **Natural Language Processing:** TextBlob

## 💻 Local Installation & Usage

To run this project locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/chinmayshirgaonkar-ctrl/health_analytics_dashboard.git](https://github.com/chinmayshirgaonkar-ctrl/health_analytics_dashboard.git)
   cd health_analytics_dashboard
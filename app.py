import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from textblob import TextBlob

st.set_page_config(page_title="Personal Health Analytics Dashboard", page_icon="📊", layout="wide")
st.title("📊 Personal Health & Sentiment Analytics Dashboard")
st.markdown("Track your physical metrics alongside your qualitative mental/physical daily logs.")

@st.cache_data
def load_data():
    df = pd.read_csv("data/mock_health_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    
    def get_sentiment(text):
        return TextBlob(str(text)).sentiment.polarity
        
    df['Log_Sentiment'] = df['Daily_Log'].apply(get_sentiment)
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file not found. Please ensure data/mock_health_data.csv exists.")
    st.stop()

st.sidebar.header("Filter Options")
start_date = st.sidebar.date_input("Start Date", df['Date'].min())
end_date = st.sidebar.date_input("End Date", df['Date'].max())
filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

st.subheader("Metrics Overview")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1: st.metric("🏃‍♂️ Avg Daily Steps", f"{int(filtered_df['Steps'].mean())}")
with kpi2: st.metric("😴 Avg Sleep (Hours)", f"{filtered_df['Sleep_Hours'].mean():.1f} hrs")
with kpi3: st.metric("❤️ Avg Heart Rate", f"{int(filtered_df['Avg_Heart_Rate'].mean())} BPM")
with kpi4:
    avg_sentiment = filtered_df['Log_Sentiment'].mean()
    sentiment_label = "Positive 😊" if avg_sentiment > 0.1 else ("Negative 😟" if avg_sentiment < -0.1 else "Neutral 😐")
    st.metric("🧠 Avg Mood Sentiment", f"{avg_sentiment:.2f}", sentiment_label)

st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Activity vs. Sentiment Trend")
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Bar(x=filtered_df['Date'], y=filtered_df['Steps'], name="Steps", marker_color='rgb(55, 83, 109)'))
    fig_trend.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Log_Sentiment'], name="Sentiment", yaxis="y2", line=dict(color='rgb(26, 150, 65)', width=3)))
    fig_trend.update_layout(yaxis=dict(title="Steps"), yaxis2=dict(title="Sentiment", overlaying="y", side="right"), legend=dict(x=0, y=1.1, orientation="h"))
    st.plotly_chart(fig_trend, use_container_width=True)

with col2:
    st.subheader("Sleep vs. Heart Rate")
    fig_scatter = px.scatter(filtered_df, x="Sleep_Hours", y="Avg_Heart_Rate", size="Steps", color="Log_Sentiment", color_continuous_scale=px.colors.diverging.RdYlGn)
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
st.subheader("📋 Raw Logs & Sentiment Scores")
display_df = filtered_df[['Date', 'Daily_Log', 'Log_Sentiment']].copy()
display_df['Date'] = display_df['Date'].dt.strftime('%Y-%m-%d')
st.dataframe(display_df.sort_values(by='Date', ascending=False), use_container_width=True)

import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re
import requests
from bs4 import BeautifulSoup

# --- Page & AI Configuration ---
st.set_page_config(layout="wide", page_title="AI Content Strategy Engine", page_icon="🚀")
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("🚨 Error configuring the AI model. Is your GEMINI_API_KEY set in the .env file?")
    st.stop()

# --- AI Agent Functions ---
def generate_strategy(topic, trends_df, audience, goal, tone):
    st.sidebar.write("🧠 Contacting AI Agent for Content Strategy...")
    trends_string = trends_df.to_string(index=False)
    prompt = f"""
    You are a world-class Content Strategist and Prompt Engineer for a digital marketing agency.
    Your client has provided specific goals for their content strategy.

    **Client's Strategic Goals:**
    - Main Topic: "{topic}"
    - Target Audience: "{audience}"
    - Primary Content Goal: "{goal}"
    - Desired Tone of Voice: "{tone}"

    **Contextual Data (Live from Google Trends):**
    You have retrieved the following real-time, related trending search queries to inform the strategy.
    ---
    {trends_string}
    ---

    **Your Task (Chain of Thought):**
    1.  **Analyze Context:** Review all the client's goals and the live trend data.
    2.  **Identify Themes:** What are the underlying user intents in the trend data that align with the client's goals?
    3.  **Brainstorm Content Angles:** Based on the themes, brainstorm 3 distinct content ideas specifically tailored to the target audience, goal, and tone.
    4.  **Structure the Strategy:** Format these ideas into a clear, actionable 3-day content plan.

    **Final Output Requirement:**
    Generate a concise, 3-day content strategy plan. For each day, provide:
    - A "killer" headline/title that reflects the requested tone and is SEO-friendly.
    - The best content format (e.g., Blog Post, YouTube Video, Instagram Reel).
    - A short summary (2-3 sentences) explaining the content's angle.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"🔥 An error occurred during strategy generation: {e}")
        return None

def generate_competitor_analysis(competitor_titles):
    st.sidebar.write("🕵️‍♂️ Contacting AI Agent for Competitor Analysis...")
    titles_string = "\n".join([f"- {title}" for title in competitor_titles])
    prompt = f"""
    You are a sharp Competitive Intelligence Analyst. You have been given a list of recent article titles from a competitor's blog.

    **Competitor's Latest Article Titles:**
    ---
    {titles_string}
    ---

    **Your Task:**
    1.  **Identify Content Pillars:** Analyze the titles to determine the competitor's top 2-3 main content themes or pillars.
    2.  **Identify Content Gaps:** Based on their focus, what topics or angles are they likely missing? Suggest 2-3 "content gap" opportunities that our client could target to stand out.

    **Output Format Instructions:**
    - Use clear markdown headings for "Content Pillars" and "Content Gap Opportunities".
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"🔥 An error occurred during competitor analysis: {e}")
        return None

# --- Reverted to the reliable, basic scraping function ---
@st.cache_data
def scrape_website_titles(url):
    """Scrapes the H1 and H2 tags from a given URL using requests and BeautifulSoup."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response.raise_for_status() # Will raise an error for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = [tag.get_text(strip=True) for tag in soup.find_all(['h1', 'h2'])]
        return list(set(titles))
    except requests.RequestException as e:
        return f"Error: Could not retrieve content from the URL. The site may be blocking scrapers or requires JavaScript. Error details: {e}"

# --- UI Layout ---
st.title("🚀 AI Content Strategy Engine")
st.markdown("""
    <style>
    .stApp {
         background-color: #2e3138;
    }
    .header {
        text-align: center;
        color: #FFFFFF;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='header'>Discover Real-Time Trends and Generate a Complete Content Plan in Seconds</h2>", unsafe_allow_html=True)
st.markdown("---")

st.sidebar.title("Strategy Controls 🎯")

with st.sidebar.expander("📝 CONTENT STRATEGY", expanded=True):
    user_topic = st.text_input("1. Enter your content topic", placeholder="e.g., 'Artificial Intelligence'")
    audience = st.selectbox("2. Select Target Audience", ["General Audience", "Gen Z (18-24)", "Millennials (25-40)", "Tech Professionals", "Small Business Owners"])
    goal = st.selectbox("3. Select Content Goal", ["Drive Engagement & Discussion", "Increase SEO Traffic", "Build Brand Trust & Authority", "Generate Leads"])
    tone = st.selectbox("4. Select Tone of Voice", ["Professional & Authoritative", "Witty & Humorous", "Friendly & Casual", "Inspirational & Uplifting"])
    generate_button = st.button("✨ Generate Content Strategy", type="primary", use_container_width=True)

with st.sidebar.expander("⚔️ COMPETITOR ANALYSIS"):
    competitor_url = st.text_input("Enter a competitor's blog URL", placeholder="e.g., https://en.wikipedia.org/wiki/Blog")
    analyze_button = st.button("🕵️‍♂️ Analyze Competitor", use_container_width=True)

if generate_button and user_topic:
    pytrends = TrendReq(hl='en-US', tz=330)
    pytrends.build_payload([user_topic], cat=0, timeframe='today 1-m', geo='IN', gprop='')
    related_queries = pytrends.related_queries().get(user_topic, {}).get('top')
    
    if related_queries is not None and not related_queries.empty:
        tab1, tab2 = st.tabs(["📈 Trend Analysis", "🤖 AI-Generated Strategy"])
        with tab1:
            st.subheader(f"Live Google Trends Data for '{user_topic}'")
            st.dataframe(related_queries)
        with tab2:
            ai_strategy = generate_strategy(user_topic, related_queries, audience, goal, tone)
            if ai_strategy:
                st.subheader("Your Custom Content Plan")
                st.markdown(ai_strategy)
    else:
        st.warning(f"⚠️ Could not find enough related trend data for '{user_topic}'. Please try a broader topic.")

elif analyze_button and competitor_url:
    st.subheader(f"Analyzing Competitor: {competitor_url}")
    with st.spinner("🕵️‍♂️ Scraping competitor titles and analyzing..."):
        titles = scrape_website_titles(competitor_url)
        if isinstance(titles, list) and titles:
            st.success(f"✅ Found {len(titles)} titles to analyze.")
            competitor_analysis = generate_competitor_analysis(titles)
            if competitor_analysis:
                st.markdown(competitor_analysis)
        else:
            st.error(titles)

else:
    st.info("Set your strategy in the sidebar and click a button to begin!")

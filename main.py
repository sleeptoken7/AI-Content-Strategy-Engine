import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

# --- Page & AI Configuration ---
st.set_page_config(layout="wide", page_title="AI Content Strategy Engine", page_icon="🚀")
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("🚨 Error configuring the AI model. Is your GEMINI_API_KEY set in the .env file?")
    st.stop()

# --- AI Agent Function ---
def generate_strategy(topic, trends_df):
    """Takes a topic and trending data, and returns an AI-generated content strategy."""
    
    st.write("🧠 Contacting AI Agent with trend data...")
    
    # Convert dataframe to a more readable string for the prompt
    trends_string = trends_df.to_string(index=False)

    # This is a sophisticated prompt that guides the AI through a chain of thought
    prompt = f"""
    You are a world-class Content Strategist and Prompt Engineer for a digital marketing agency.
    Your client wants to create engaging content about the topic: "{topic}".
    You have successfully retrieved real-time, related trending search queries from Google Trends to inform your strategy.

    **Analysis Task (Chain of Thought):**
    1.  **Analyze the Input:** Review the client's topic ('{topic}') and the provided list of trending queries.
    2.  **Identify Core Themes:** What are the underlying themes or user intents behind these trending searches? (e.g., are people looking for 'how-to guides', 'cost comparisons', 'product reviews', 'beginner tips'?).
    3.  **Brainstorm Content Angles:** Based on these themes, brainstorm 3 distinct and creative content ideas that would perform well on platforms like YouTube, blogs, and social media.
    4.  **Structure the Strategy:** Format these ideas into a clear, actionable 3-day content plan.

    **Here is the real-time trending data from Google Trends:**
    ---
    {trends_string}
    ---

    **Final Output Requirement:**
    Generate a concise, 3-day content strategy plan. For each day, provide:
    - A "killer" headline/title that is SEO-friendly and attention-grabbing.
    - The best content format (e.g., Blog Post, YouTube Video, Instagram Reel).
    - A short summary (2-3 sentences) of what the content will cover, including the angle.

    Do not include any extra conversational text or introductions like "Here is the content strategy".
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"🔥 An error occurred while generating the strategy: {e}")
        return None

# --- UI Layout ---
st.title("🚀 AI Content Strategy Engine")
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f5;
        padding: 20px;
        border-radius: 10px;
    }
    .header {
        text-align: center;
        color: #333;
    }
    .subheader {
        color: #007bff;
    }
    .input-container {
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='header'>Discover Real-Time Trends and Generate a Complete Content Plan in Seconds</h2>", unsafe_allow_html=True)

# --- Input Form ---
with st.form(key="topic_form"):
    user_topic = st.text_input("Enter your content topic (e.g., 'electric cars', 'skincare routine')", placeholder="What's your topic?", key="topic_input")
    submit_button = st.form_submit_button(label="✨ Generate Strategy")

# --- Main Logic ---
if submit_button and user_topic:
    st.markdown("---")
    st.subheader(f"Analyzing Trends for: '{user_topic}'", anchor="trends-analysis")
    
    with st.spinner("🔍 Fetching real-time data from Google Trends..."):
        try:
            pytrends = TrendReq(hl='en-US', tz=330)
            pytrends.build_payload([user_topic], cat=0, timeframe='today 1-m', geo='IN', gprop='')
            related_queries = pytrends.related_queries().get(user_topic, {}).get('top')
            
            if related_queries is not None and not related_queries.empty:
                st.success("✅ Found a list of trending related topics!")
                st.dataframe(related_queries)
                
                # --- AI GENERATION ---
                ai_strategy = generate_strategy(user_topic, related_queries)
                
                if ai_strategy:
                    st.markdown("---")
                    st.subheader("🤖 Your AI-Generated Content Strategy")
                    st.markdown(ai_strategy)
            else:
                st.warning("⚠️ Could not find enough related trend data for this topic. Please try a broader topic.")

        except Exception as e:
            st.error(f"🔥 An error occurred while fetching trends: {e}")

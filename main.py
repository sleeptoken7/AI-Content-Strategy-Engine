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
def generate_strategy(topic, trends_df, audience, goal, tone):
    """Takes user inputs and trend data, and returns an AI-generated content strategy."""
    
    st.write("🧠 Contacting AI Agent with enriched context...")
    
    trends_string = trends_df.to_string(index=False)

    # Advanced prompt that uses all the user's granular controls
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
    3.  **Brainstorm Angles:** Based on the themes, brainstorm 3 distinct content ideas specifically tailored to the target audience, goal, and tone.
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
        st.error(f"🔥 An error occurred while generating the strategy: {e}")
        return None

# --- UI Layout ---
st.title("🚀 AI Content Strategy Engine")

# --- Your Custom CSS Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f5;
        padding: 20px;
        border-radius: 10px;
    }
    .stApp {
         background-color: #2e3138; /* A darker background for the whole app */
    }
    .header {
        text-align: center;
        color: #FFFFFF; /* White text for header */
    }
    .subheader {
        color: #007bff;
    }
    </style>
""", unsafe_allow_html=True)

# --- Your Custom Header ---
st.markdown("<h2 class='header'>Discover Real-Time Trends and Generate a Complete Content Plan in Seconds</h2>", unsafe_allow_html=True)
st.markdown("---")


# --- Sidebar Controls ---
st.sidebar.title("Strategy Controls 🎯")
st.sidebar.markdown("Define your content goals here.")

user_topic = st.sidebar.text_input("1. Enter your content topic", placeholder="e.g., 'Artificial Intelligence'")
audience = st.sidebar.selectbox("2. Select Target Audience", ["General Audience", "Gen Z (18-24)", "Millennials (25-40)", "Tech Professionals", "Small Business Owners"])
goal = st.sidebar.selectbox("3. Select Content Goal", ["Drive Engagement & Discussion", "Increase SEO Traffic", "Build Brand Trust & Authority", "Generate Leads"])
tone = st.sidebar.selectbox("4. Select Tone of Voice", ["Professional & Authoritative", "Witty & Humorous", "Friendly & Casual", "Inspirational & Uplifting"])

generate_button = st.sidebar.button("✨ Generate Strategy", type="primary", use_container_width=True)

# --- Main Logic & Display ---
if generate_button and user_topic:
    st.subheader(f"Analyzing Trends for: '{user_topic}'")
    
    with st.spinner("🔍 Fetching real-time data from Google Trends..."):
        try:
            pytrends = TrendReq(hl='en-US', tz=330)
            pytrends.build_payload([user_topic], cat=0, timeframe='today 1-m', geo='IN', gprop='')
            related_queries = pytrends.related_queries().get(user_topic, {}).get('top')
            
            if related_queries is not None and not related_queries.empty:
                st.success("✅ Found a list of trending related topics!")
                st.dataframe(related_queries)
                
                # --- AI GENERATION ---
                with st.spinner("🤖 AI Agent is building your custom strategy..."):
                    ai_strategy = generate_strategy(user_topic, related_queries, audience, goal, tone)
                
                if ai_strategy:
                    st.markdown("---")
                    st.subheader("🤖 Your AI-Generated Content Strategy")
                    st.markdown(ai_strategy)
            else:
                st.warning(f"⚠️ Could not find enough related trend data for '{user_topic}'. Please try a broader topic.")

        except Exception as e:
            st.error(f"🔥 An error occurred while fetching trends: {e}")

else:
    st.info("Set your strategy in the sidebar and click 'Generate Strategy' to begin!")

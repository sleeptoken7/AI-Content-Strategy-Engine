# Sentiview AI - Project Documentation

**Team:** purpleCode
**Project:** An interactive AI agent for generating and refining marketing personas from customer reviews.
**Hackathon:** AgentForce Hackathon - August 2025

---

## Table of Contents
1.  [Project Overview](#1-project-overview)
2.  [Presentation Content (for 8-Slide PPT)](#2-presentation-content-for-8-slide-ppt)
3.  [Technical Documentation](#3-technical-documentation)
4.  [Usage Guide](#4-usage-guide)
5.  [Video Demo Script](#5-video-demo-script)

---

## 1. Project Overview

### The Problem

In a hyper-competitive market like Bengaluru's restaurant scene, understanding the customer is the key to survival. Businesses receive a constant flood of valuable feedback every day in the form of thousands of online reviews on platforms like Zomato and Google Maps.

However, this data is a double-edged sword. For busy marketing teams, manually reading, categorizing, and synthesizing these reviews is an impossible task. They are drowning in raw data but starving for actionable insights.

As a result, marketing campaigns often remain generic and one-size-fits-all, failing to connect with specific customer segments. This leads to wasted ad spend and missed opportunities to attract and retain different types of diners. Marketers know the answers are in the reviews, but they lack the tools to unlock them efficiently.

### Our Solution: Sentiview AI

**Sentiview AI** is an interactive web application that acts as an AI-powered marketing analyst for restaurants.

Sentiview AI connects to a large-scale dataset of real customer reviews and, with a single click, empowers marketers to instantly understand their customer base. Our agent, powered by the Google Gemini API, generates a comprehensive dashboard that includes an overall sentiment score, the top positive and negative themes, and detailed, data-driven customer personas.

The most innovative feature is its interactivity. Beyond a static report, Sentiview AI allows marketers to have a "conversation" with the agent. They can provide natural language feedback—like "focus more on families"—to instantly refine the entire analysis. This transforms a slow, manual process into a dynamic, real-time strategy session, enabling restaurants to create hyper-targeted campaigns with speed and confidence.

---

## 2. Presentation Content (for 8-Slide PPT)

This is the recommended content for the provided 8-slide template.

* **Slide 1: Title Slide**
    * **Title:** Sentiview AI
    * **Subtitle:** The AI-Powered Marketing Analyst for Restaurants
    * **Team Name:** purpleCode
    * **Event:** AgentForce Hackathon - August 2025

* **Slide 2: The Problem**
    * **Title:** The Challenge: Drowning in Data, Starving for Insight
    * **Content:** Restaurant marketers receive a constant flood of online reviews. Manually reading thousands of comments to understand different customer types is impossible. This leads to generic campaigns that waste budget and fail to connect with the right audience.

* **Slide 3: Our Solution**
    * **Title:** Introducing Sentiview AI
    * **Content:** An interactive web app that acts as an AI marketing analyst. With one click, our agent, powered by the Google Gemini API, analyzes reviews and generates a full dashboard with sentiment scores, key themes, and detailed customer personas, turning messy feedback into clear, actionable strategy.

* **Slide 4: Key Features & Innovation**
    * **Title:** More Than a Report, It's a Conversation
    * **Feature 1: Automated Persona Generation (👥):** Instantly creates detailed customer personas with bios, goals, and pain points.
    * **Feature 2: Thematic Analysis (📈):** Automatically extracts top positive and negative themes for a quick snapshot of what's working.
    * **Feature 3: Interactive Refinement (✨):** Our most innovative feature. Users can give natural language feedback (e.g., "focus on families") to the AI, which regenerates the analysis in real-time.

* **Slide 5: Live Demo**
    * **Title:** See Sentiview AI in Action
    * **Content:** A 2-minute video demonstrating our application, from restaurant selection to interactive persona refinement.
    * **(Include a large, clean screenshot of the final app dashboard and the link to your video).**

* **Slide 6: Technical Architecture & Stack**
    * **Title:** Built with a Modern, Efficient Stack
    * **(Include a simple flowchart: `User -> Streamlit Frontend -> Pandas Data Layer -> Gemini API Agent -> Streamlit Frontend`)**
    * **Tech Stack:** Python, Streamlit, Pandas, Google Gemini 1.5 Flash API, Conda, Git/GitHub.

* **Slide 7: Challenges & Strategic Pivots**
    * **Title:** Our Hackathon Journey: Adapting to Challenges
    * **Challenge:** Initial attempts at live web scraping of dynamic websites proved unreliable.
    * **Solution:** We made a strategic pivot to use a large, public Kaggle dataset. This allowed us to build a more robust and feature-rich application and focus our time on the core AI functionality, demonstrating our ability to make effective decisions under pressure.

* **Slide 8: Future Scope & Thank You**
    * **Title:** The Future of Sentiview AI
    * **Future Features:** Integrate live APIs from Zomato and Google for real-time analysis, track sentiment over time, and auto-generate social media ad copy.
    * **Closing:** Thank You! - Team purpleCode

---

## 3. Technical Documentation

### Architecture

The application is built on three core components:

* **Frontend (UI Layer):** Built with **Streamlit**, this provides a simple, responsive, and interactive web interface. It handles all user inputs and displays the AI-generated results.
* **Data Layer:** Uses **Pandas** and a large **Kaggle CSV Dataset** (`zomato.csv`). Pandas is used for efficient loading, cleaning, and filtering of this data in memory.
* **AI Agent Core:** Powered by the **Google Gemini 1.5 Flash API**. This is the "brain" of our application. The agent takes reviews and a carefully engineered prompt as input, analyzes the text, and returns a structured JSON response containing the full marketing analysis.

### Tech Stack

* **Python:** The core programming language for the entire project.
* **Streamlit:** A powerful open-source framework used to rapidly build and deploy our interactive web application.
* **Pandas:** The primary library for efficient loading and manipulation of the `zomato.csv` dataset.
* **Google Gemini 1.5 Flash API:** Leveraged for all natural language processing tasks, including sentiment analysis, thematic extraction, and persona generation.
* **Conda:** The environment manager used to create an isolated and stable development environment, which was crucial for solving complex dependency issues.
* **Git & GitHub:** Used for version control and to host our public codebase.

---

## 4. Usage Guide

### A. Local Setup & Installation

**Prerequisites:**
* Anaconda or Miniconda installed.
* Git installed.

**Step 1: Clone the Repository**
Open your terminal and clone the project's GitHub repository.
```bash
git clone <your-github-repo-url>
cd AgentForce_purpleCode
# 🚀 AI Content Strategy Engine

<div align="center">
  <img src="<img width="263" height="148" alt="image" src="https://github.com/user-attachments/assets/7223c3dd-ba41-4d4c-b1b9-c6b25815866c" />
 " alt="Welcome Banner" width="800"/>
</div>

<p align="center">
  <em>An interactive AI agent that transforms real-time Google Trends data into a complete, actionable content strategy in seconds.</em>
</p>

<p align="center">
  <img alt="Python Version" src="https://img.shields.io/badge/Python-3.9-blue.svg?style=for-the-badge&logo=python">
  <img alt="Framework" src="https://img.shields.io/badge/Streamlit-1.37-red.svg?style=for-the-badge&logo=streamlit">
  <img alt="AI Model" src="https://img.shields.io/badge/AI%20Model-Gemini%201.5%20Flash-purple.svg?style=for-the-badge">
</p>

---

---

## 🎯 The Problem

Content marketing teams are drowning in data but starving for insights. Manually sifting through Google Trends, YouTube, and Reddit to find relevant topics is a slow, reactive process. This guesswork leads to low-engagement content and a poor return on investment. The core challenge is one of **Context Engineering**: how do you turn raw, real-time data into a coherent and creative strategy?

## 🧠 Our Solution

This **AI Content Strategy Engine** is a tool that automates this entire workflow. It empowers a content strategist to:
1.  **Discover** real-time, trending topics related to their core subject.
2.  **Analyze** the underlying user intent behind those trends.
3.  **Generate** a complete, multi-day content plan with a single click.

It's a practical demonstration of how a well-engineered AI agent can transform a complex business challenge into a simple, elegant solution.

---

## 核心 Features

-   **📈 Real-Time Trend Analysis:** Connects directly to the Google Trends API (`pytrends`) to pull the latest rising search queries related to any topic.
-   **🤖 Advanced AI Core:** Leverages the **Google Gemini 1.5 Flash API** with a sophisticated "Chain of Thought" prompt that instructs the AI on *how* to think like a strategist.
-   **🗓️ Instant Content Calendar:** Automatically generates a 3-day content plan, complete with SEO-friendly headlines, optimal content formats, and detailed summaries.
-   **✨ Clean & Interactive UI:** A beautiful and intuitive interface built with **Streamlit** that makes the entire process seamless, from input to final strategy.

---

## 🛠️ Tech Stack

| Layer       | Technology                                                                                           |
| :---------- | :--------------------------------------------------------------------------------------------------- |
| **Frontend** | Streamlit                                                                                            |
| **Backend** | Streamlit, Python 3.9                                                                                |
| **Data Source** | Google Trends (via `pytrends`)                                                                     |
| **AI Agent** | Google Gemini 1.5 Flash API (`google-generativeai`)                                                  |
| **Data Handling** | Pandas                                                                                               |
| **Environment** | Conda                                                                                                |

---

## ⚙️ How to Run Locally

### Prerequisites

-   Anaconda or Miniconda
-   Git

### Setup Instructions

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/sleeptoken7/AI-Content-Strategy-Engine.git](https://github.com/sleeptoken7/AI-Content-Strategy-Engine.git)
    cd AI-Content-Strategy-Engine
    ```

2.  **Create and Activate the Conda Environment**
    ```bash
    conda create --name contentstrategy python=3.9 -y
    conda activate contentstrategy
    ```

3.  **Install Dependencies**
    ```bash
    # Install complex libraries via Conda
    conda install -c conda-forge pandas streamlit python-dotenv pytrends -y

    # Install the Google AI library via Pip
    python -m pip install google-generativeai
    ```

4.  **Set Up Your API Key**
    -   Create a file named `.env` in the root of the project.
    -   Add your Google Gemini API key to it: `GEMINI_API_KEY="YOUR_API_KEY_HERE"`

5.  **Run the App**
    ```bash
    streamlit run main.py
    ```

The application will launch in your web browser!
<img width="1440" height="900" alt="image" src="https://github.com/user-attachments/assets/be2cfc4f-50e2-4af4-a27d-2a52a2767678" />

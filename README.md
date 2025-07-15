# 📺 YouTube to Blog Converter using CrewAI

Transform YouTube videos into professional blog posts with the power of AI agents! This intelligent system uses CrewAI to coordinate agents that search YouTube content, extract insights, and generate well-structured blog articles in markdown format.

---

## 📁 Project Overview

✅ **YouTube to Blog Converter**  
**Description**:  
A Streamlit-based AI-powered application that converts YouTube content into publishable blog posts by coordinating multiple agents using CrewAI.

**Key Features**:
- AI-powered research and blog generation using GPT-4
- Integration with YouTube Data API for video search and retrieval
- Multi-agent coordination via CrewAI (Research + Writing)
- Streamlit web interface for interactive use
- Customizable YouTube channel and search topics
- Markdown output with download option
- API rate limit control (RPM)
- Context memory across agents for coherent output

---

## 📦 Dependencies

- Python 3.8+
- `crewai`
- `streamlit`
- `openai`
- `google-api-python-client` (YouTube API)
- `python-dotenv`

## ✨ Features

- ✅ **Multi-agent orchestration using CrewAI**
- 🔍 **YouTube content search with channel + topic filters**
- 🧠 **Context-aware research and writing agents**
- 📝 **Professional blog generation in markdown**
- 📥 **Download functionality for generated posts**
- ⚙️ **Configurable RPM (requests per minute) limits**
- 🌐 **Streamlit-based user interface**

---

## ⚙️ Usage

### 🧪 Quick Demo

- ✅ Enter your **OpenAI** and **YouTube API keys** in the sidebar
- ✅ Input a **YouTube channel handle** and a **topic** you want to research
- ✅ The system will generate a **research-backed blog post** that you can **download as a `.md` file**

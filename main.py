import os
import streamlit as st
from crewai import Crew, Process
from Agents import get_agents
from tasks import get_tasks

st.set_page_config(
    page_title="YouTube to Blog Converter",
    page_icon="📝",
    layout="wide"
)

st.title("YouTube to Blog Generator")
st.subheader("Transform YouTube videos into professional blog posts")
st.markdown("---")

#sidebar
with st.sidebar:
    st.header(" Configuration")
    api_key = st.text_input("OpenAI API Key", type="password", help="Get from https://platform.openai.com/api-keys")
    youtube_key = st.text_input("YouTube API Key", type="password", help="Get from Google Cloud Console")
    
    st.header(" Content Parameters")
    channel_handle = st.text_input("YouTube Channel Handle", "@krishnaik06", 
                                 help="Format: '@channelname'")
    topic = st.text_input("Search Topic", "AI VS ML VS DL vs Data Science",
                        help="Any topic you want to research")
    
    st.header("Performance")
    rpm = st.slider("Max RPM", 10, 200, 100)
    st.markdown("---")
    generate_btn = st.button("Generate Blog Post")

# Main content area
if generate_btn:
    if not api_key or not youtube_key:
        st.error("Please provide both API keys!")
        st.stop()
    
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["YOUTUBE_API_KEY"] = youtube_key
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"
    progress_container = st.container()

    with progress_container:
        st.info("Initializing research agents...")
        
        blog_researcher, blog_writer = get_agents(channel_handle, topic)
        research_task, write_task = get_tasks(channel_handle, topic)
        
      
        research_task.agent = blog_researcher
        write_task.agent = blog_writer
        
        st.info(" Forming content crew...")
        crew = Crew(
            agents=[blog_researcher, blog_writer],
            tasks=[research_task, write_task],
            process=Process.sequential,
            memory=True,
            cache=True,
            max_rpm=rpm,
            share_crew=True
        )
        
        st.info("Researching videos and writing content...")
    
        with st.spinner("Generating content. This may take 2-3 minutes..."):
            result = crew.kickoff()
    
    progress_container.empty()
    st.success("Blog post generated successfully!")
    st.subheader(f"Blog Content: {topic}")
    st.markdown(result)
    st.divider()
    
    try:
        with open('generated_blog.md', 'r') as f:
            st.download_button(
                label="Download Blog",
                data=f.read(),
                file_name=f"{topic.replace(' ', '_')}_blog.md",
                mime="text/markdown"
            )
    except Exception as e:
        st.error(f"Error generating download: {str(e)}")
        
    st.markdown("---")
    st.info(" Tip: You can search for any topic by changing the inputs above")
else:
    st.info(" Configure your settings in the sidebar and click 'Generate Blog Post' to get started")
    st.image("https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?auto=format&fit=crop&w=1200&h=600", 
             caption="Turn YouTube videos into professional blog posts")
    
  
    st.subheader("Example Search Topics:")
    st.markdown("""
    - Machine Learning vs Deep Learning
    - Python for Data Science
    - Neural Network Architectures
    - Natural Language Processing Trends
    - Computer Vision Applications
    - Generative AI Tools
    - Time Series Forecasting
    - Reinforcement Learning Basics
    """)
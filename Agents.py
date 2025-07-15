import os
from crewai import Agent
from Tools import get_yt_tool
from dotenv import load_dotenv

load_dotenv()

def get_agents(channel_handle, topic):
    """
    Create agents with dynamic topic and channel
    """
    #  researcher agent
    blog_researcher = Agent(
        role='YouTube Research Specialist',
        goal=f'Extract key information about {topic} from YouTube videos',
        verbose=True,
        memory=True,
        backstory=(
            "Expert in analyzing technical videos on AI, Data Science, and Machine Learning. "
            "Skilled at identifying core concepts and extracting valuable insights from video content."
        ),
        tools=[get_yt_tool(channel_handle)],
        allow_delegation=True
    )
    
    # writer agent
    blog_writer = Agent(
        role='Technical Content Writer',
        goal=f'Create engaging blog content about {topic}',
        verbose=True,
        memory=True,
        backstory=(
            "Specializes in transforming complex technical topics into accessible, "
            "engaging content. Has a talent for creating compelling narratives that "
            "educate and captivate readers."
        ),
        tools=[get_yt_tool(channel_handle)],
        allow_delegation=False
    )
    
    return blog_researcher, blog_writer
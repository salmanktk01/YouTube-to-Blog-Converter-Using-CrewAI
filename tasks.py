from crewai import Task
from Tools import get_yt_tool

def get_tasks(channel_handle, topic):
    """
    Create tasks with dynamic topic and channel
    """
    # Research task
    research_task = Task(
        description=(
            f"Conduct thorough research on the topic '{topic}' from YouTube videos "
            f"on channel {channel_handle}"
        ),
        expected_output='A comprehensive 3-paragraph research report',
        tools=[get_yt_tool(channel_handle)],
        agent=None,  
    )
    
    # Writing task
    write_task = Task(
        description=(
            f"Create a blog post about '{topic}' using research findings "
            f"from YouTube channel {channel_handle}"
        ),
        expected_output='A well-structured blog post in markdown format',
        tools=[get_yt_tool(channel_handle)],
        agent=None,  
        output_file='generated_blog.md'
    )
    
    return research_task, write_task
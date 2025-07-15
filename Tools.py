from crewai_tools import YoutubeChannelSearchTool
import streamlit as st

def get_yt_tool(channel_handle='@krishnaik06'):
    """
    Create YouTube search tool with dynamic channel selection
    """
    return YoutubeChannelSearchTool(youtube_channel_handle=channel_handle)
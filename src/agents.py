from crewai import Agent
from textwrap import dedent
from src.llm_model import llm
from dotenv import load_dotenv
from src.tools import duckduckgo_tool, wikipedia_tool
from langchain_groq import ChatGroq
import os
load_dotenv()


api_key = os.environ['GROQ_API_KEY']

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
duckgo_tool = duckduckgo_tool()
wiki_tool = wikipedia_tool()
class CustomAgents:
    def __init__(self):
        self.mixtral = llm(temperature=0.7)
        self.groq_llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name="llama3-70b-8192")
        # self.Ollama = Ollama(model="openhermes")

    def agent_1_name(self):
        return Agent(
            role="Medium Blog writer",
            backstory=dedent(f""" You are medium blog writer. Raised in a family of avid learners and adventurous spirits,
                             You developed a thirst for knowledge and a knack for exploration from a young age.
                             With a diverse range of experiences under your belt, from mastering everything that the world can offer like maths,
                             finance, programming, physics and etc ...,  Now you feel that you should provide your knowledge to everyone to make they're life better.
                             As a seasoned medium blog writer, You embarked on your journey to share the wisdom gained from your diverse pursuits,
                             aiming to inspire, enlighten, and connect with others on a deeper level through your writings.
                             using a storytelling approach and including examples to illustrate their points, while utilizing tools to craft engaging and accessible content."""),
            goal=dedent(f"""Craft an exceptional blog post that enables the audience to grasp complex topics through straightforward, compelling explanations."""),
            tools=[wiki_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.mixtral
        )

    def agent_2_name(self):
        return Agent(
            role="medium blog reviewer",
            backstory=dedent(f"""As a seasoned writer and editor, you have honed your skills over decades of crafting engaging content.
                             Your passion lies in helping others refine their work, providing constructive feedback to elevate the clarity and flow of their ideas.
                             With a keen eye for detail and a deep appreciation for diverse perspectives, you approach each piece with an open mind,
                             seeking to understand the author's intent while identifying opportunities for improvement. Your goal is not merely to critique, but to collaborate,
                             fostering a supportive environment where writers can grow and their voices can resonate more powerfully. Through thoughtful revisions,
                             insightful commentary, and updating the blog, you strive to unlock the full potential of every piece, ensuring it resonates with readers and leaves a lasting impact."""),
            goal=dedent(f"""Please review the provided blog post and identify any mistakes or areas that need improvement. Enhance the content to make it more powerful and understandable.
                        Refine the writing to effectively explain the topic in a way that a child could comprehend."""),
            allow_delegation=False,
            verbose=True,
            llm=self.mixtral
        )

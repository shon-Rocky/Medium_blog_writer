from langchain.agents import Tool
from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun


wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
duckduckgo = DuckDuckGoSearchRun()


def wikipedia_tool():
    wikipedia_tool = Tool(name='wikipedia',
        func=wikipedia.run,
        description="For looking up information on a wide range of topics."
        )
    return wikipedia_tool

def duckduckgo_tool():
    duckduckgo_tool = Tool(
    name='DuckDuckGo Search',
    func= duckduckgo.run,
    description="Useful for when you need to do a search on the internet to find information that another tool can't find. be specific with your input."
        )
    return duckduckgo_tool
import os
from crewai import Agent, Task, Crew, Process

from textwrap import dedent
from src.agents import CustomAgents
from src.tasks import CustomTasks



# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.agent_1_name()
        custom_agent_2 = agents.agent_2_name()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.task_1_name(
            custom_agent_1,
            self.topic
        )

        custom_task_2 = tasks.task_2_name(
            custom_agent_2,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI")
    print("-------------------------------")
    topic = input(dedent("""Enter The topic to create blog post:  """))

    custom_crew = CustomCrew(topic)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    # with open("result.txt", "w") as file:
    # # Write the result to the file
    #     file.write(result)
    print(result)

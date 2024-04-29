from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, topic):
        return Task(
            description=dedent(
                f"""
            Write an impactful and engaging blog post on the given {topic}.
            The content should be well structured easy to comprehend and learn complex subjects effortlessly.
            Utilize a straightforward yet compelling writing style that breaks down difficult concepts into simple,
            easy-to-understand explanations. The goal is to create an enjoyable exceptional blog post that enables readers to grasp and appreciate the intricacies of the chosen {topic}
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible. Use the tool only if needed. mostly use your information. Make sure the post must be above 1000+ words.
    
           
        """
            ),
            expected_output=dedent(f"""Write a 1000+ words blog post that thoroughly covers a complex topic in a clear way.
            Use engaging explanations, analogies, and examples to make sophisticated concepts accessible for everyone without compromising depth.
            The goal is an exceptionally insightful yet conversational blog post. Make sure the post must be above 1000+ words.
                                   
            """),
            
            agent=agent,
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from task 1 and Review the provided blog post, identifying any errors or areas needing improvement.
            Enhance the content to make it more impactful and comprehensible for a every audience.
            Refine the writing style to effectively explain the topic in a manner that everyone understand.
                                       
            {self.__tip_section()}

            
        """
            ),
            expected_output=dedent(f""" Review the blog post content thoroughly. Check for any errors and make corrections as needed.
            Evaluate if the topic is comprehensively covered. If there are gaps, conduct additional research and expand the content to ensure full topic coverage.
            Format the final output in the style guidelines for Medium blog posts.
            """),
            agent=agent,
        )

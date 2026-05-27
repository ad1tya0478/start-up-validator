from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

@CrewBase
class Validator():

    agents: list[BaseAgent]
    tasks: list[Task]

    # Config paths
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # -------- Agents --------

    @agent
    def CEO(self) -> Agent:
        return Agent(
            config=self.agents_config["CEO"],
            tools=[search_tool]
        )

    @agent
    def marketer(self) -> Agent:
        return Agent(
            config=self.agents_config["marketer"],
            tools=[search_tool]
        )

    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config["developer"],
            tools=[search_tool]
        )

    @agent
    def vc(self) -> Agent:
        return Agent(
            config=self.agents_config["vc"],
            tools=[search_tool]
        )

    # -------- Tasks --------

    @task
    def CEO_task(self) -> Task:
        return Task(
            config=self.tasks_config["CEO_task"],
            agent=self.CEO()
        )

    @task
    def marketer_task(self) -> Task:
        return Task(
            config=self.tasks_config["marketer_task"],
            agent=self.marketer()
        )

    @task
    def developer_task(self) -> Task:
        return Task(
            config=self.tasks_config["developer_task"],
            agent=self.developer()
        )

    @task
    def vc_task(self) -> Task:
        return Task(
            config=self.tasks_config["vc_task"],
            agent=self.vc(),
            context=[
                self.CEO_task(),
                self.marketer_task(),
                self.developer_task()
            ],
            output_file="final_report.md"
        )

    # -------- Crew --------

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
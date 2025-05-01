import asyncio

from sources.agents.agent import Agent
from sources.tools.BashInterpreter import BashInterpreter
from sources.tools.fileFinder import FileFinder
from sources.tools.flightSearch import FlightSearch
from sources.tools.searxSearch import searxSearch
from sources.utility import animate_thinking, pretty_print


class CasualAgent(Agent):
    def __init__(self, name, prompt_path, provider, verbose=False):
        """
        The casual agent is a special for casual talk to the user without specific tasks.
        """
        super().__init__(name, prompt_path, provider, verbose, None)
        self.tools = {}  # No tools for the casual agent
        self.role = "talk"
        self.type = "casual_agent"

    async def process(self, prompt, speech_module) -> str:
        self.memory.push("user", prompt)
        animate_thinking("Thinking...", color="status")
        answer, reasoning = await self.llm_request()
        self.last_answer = answer
        self.status_message = "Ready"
        return answer, reasoning


if __name__ == "__main__":
    pass

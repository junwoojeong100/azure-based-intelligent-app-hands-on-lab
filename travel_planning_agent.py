from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv
import asyncio

load_dotenv()

model_client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  # For key-based authentication.
)

planner_agent = AssistantAgent(
    name="planner_agent",
    description="여행 일정을 계획해주는 에이전트입니다.",
    model_client=model_client,
    system_message="""당신은 사용자의 요청에 따라 여행 일정을 제안하는 유용한 여행 플래너 에이전트입니다. 여행 계획을 마무리할 때는 반드시 'INITIAL PLAN COMPLETE'로 끝내세요."""
)

local_agent = AssistantAgent(
    name="local_agent",
    description="현지의 숨은 명소와 로컬 경험을 추천하는 에이전트입니다.",
    model_client=model_client,
    system_message="""당신은 사용자를 위해 현지의 진짜 명소, 체험, 음식 등 흥미로운 로컬 활동을 추천하는 에이전트입니다. 추천을 마칠 때는 반드시 'LOCAL RECOMMENDATIONS COMPLETE'로 끝내세요."""
)

language_agent = AssistantAgent(
    name="language_agent",
    description="여행지에서의 언어/소통 팁을 제공하는 에이전트입니다.",
    model_client=model_client,
    system_message="""당신은 여행 계획을 검토하고, 해당 여행지에서 언어 또는 소통에 있어 중요한 팁과 주의사항을 제공하는 에이전트입니다. 언어 팁을 마칠 때는 반드시 'LANGUAGE TIPS COMPLETE'로 끝내세요."""
)

travel_summary_agent = AssistantAgent(
    name="travel_summary_agent",
    description="모든 에이전트의 제안을 종합하여 최종 여행 일정을 요약하는 에이전트입니다.",
    model_client=model_client,
    system_message="""당신은 다른 에이전트들의 제안과 조언을 모두 반영하여 최종 여행 일정을 상세하게 요약하는 에이전트입니다. 반드시 모든 관점을 통합한 최종 일정을 제공해야 하며, 계획이 완성되면 'TERMINATE'로 응답을 마무리하세요."""
)

user_proxy_travel = UserProxyAgent(
    name="user_proxy",
    description="여행 계획을 요청하는 사용자 역할의 에이전트입니다."
)

termination = TextMentionTermination("TERMINATE")
group_chat = RoundRobinGroupChat(
    [planner_agent, local_agent, language_agent, travel_summary_agent], termination_condition=termination
)


async def main():
    await Console(group_chat.run_stream(task="저는 친구와 함께 5일간 파리로 여행을 계획하고 있습니다. 저희는 예술과 음식을 좋아하며, 유명한 명소뿐만 아니라 현지의 숨은 보석 같은 장소도 경험하고 싶습니다. 저희는 프랑스어를 할 줄 모릅니다. 상세한 여행 일정을 만들어주세요."))

asyncio.run(main())
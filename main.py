import os 
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,function_tool
from agents.run import RunConfig
import asyncio

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
api_key=api_key,
base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
model="gemini-2.0-flash",
openai_client=external_client
)

config = RunConfig(
model=model,
model_provider=external_client,
tracing_disabled=True
)

@function_tool
async def Tourism_skills()->str:
    return "Tourism & Hospitality Skills: Customer service, cultural awareness, event planning, multitasking, language skills"

@function_tool
async def Journalism_skills()->str:
    return "Journalism Skills: Investigative research, storytelling, interview techniques, media ethics, fact-checking, writing & editing, digital content creation"

@function_tool
async def IT_skills()->str:
    return "Information Technology (IT) Skills: Networking, cybersecurity, cloud computing, database management, system administration, troubleshooting, IT support"

async def main():

    Careeragent=Agent(
        name="Career Agent",
        instructions="""you are a helpful Career agent.your task 
        is suggest feilds to them.Talk to them in a friendly way.Do NOT discuss
        anything out of your domain just excuse the user."""
    )

    Skillagent=Agent(
        name="Skill Agent",
        instructions="""you ONLY handle skill-related queries.
         RULES:
        - If the user asks about skills for tourism field, IMMEDIATELY call the tool 'Tourism_skills'.
        - If the user asks about skills for tourism field, IMMEDIATELY call the tool 'Journalism_skills'
        - If the user asks about skills for tourism field, IMMEDIATELY call the tool 'IT_skills
        - DO NOT ask clarifying questions.
        - If the tool doesn't have an exact match,excuse them""",
        tools=[Tourism_skills,Journalism_skills,IT_skills]

    )

    Jobagent=Agent(
        name="Job Agent",
        instructions="""you are a helpful Job agent.your task " 
        is to share real-world job roles to user.Do NOT discuss 
        anything out of your domain just excuse the user."""
    )

    OrchestorAgent=Agent(
        name="Router Agent",
        instructions="""You are a router agent.you have to decide 
        whether the question is about Career,Skill or Job.
        If user ask about Career related query handsoff to CareerAgent
        If user ask about Skill related question handsoff to SkillAgent
        If the user ask about Job  handsoff to JobAgent""",
        handoffs=[Careeragent,Skillagent,Jobagent]
    )
    
    print("Welcome to Career Mentor Agent!")
    user=input("Ask a question to us?")

    response=await Runner.run(
        OrchestorAgent,
        input=user,
        run_config=config
    )

    print(response.final_output)
    

if __name__=="__main__":
    asyncio.run(main())






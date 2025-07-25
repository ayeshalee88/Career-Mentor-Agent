#How my agent works and the flow between tools/agents

#I start my project my initializing it.Then I made virtual environment which make personal space and manage dependencies then i moved to install openai-agents and python dotenv because i am working with open-ai and dotenv for storing environment variable and i import all these dependencies like custom and 3rd party modules like async ai,Runner,openaichatcompletionmodel.

#Next step is to set either Open-ai or Gemini key in .env file.
#then get the gemini key in my main.py file
#I make connection To Gemini model 

#Moving forward i made tools with a simple python function and return it which will later called by skillagent.
#Then I made three different agents like Career,Skill and Job Agent.
#I use tools in my Career Agent to pass it to external python function.
#then I made an orchestor Agent to route between multiple agents.
#then I use response which Run the Agent by using Runner class and then give parameters to them.
#And then lastly print it in my terminal.....

Tech Stack
Python 3.x
OpenAI Agents SDK
Gemini 2.0 Flash Model
python-dotenv for environment variables


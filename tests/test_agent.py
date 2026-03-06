from app.agent import create_agent

agent = create_agent()

query = "What is the total number of jobs reported and where is it stated?"

response = agent.run(query)

print(response)
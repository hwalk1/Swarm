# [sample_prompts]
prompts = [
  "What can you help me do?",
  "Which tools do you have access to?",
  "What are your capabilities?"
]

agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

agent_code = Agent(
    name='Agent Code',
    instructions='Code in React the response from another Agent'
)

agent_post = Agent(
    name='Agent Post',
    instructions='Post on X'
)

agent_summary = Agent(
    name='Agent Summary',
    instructions='Summarise the incoming messages from the agents and then save them to the DB'
)

agent_dashboard = Agent(
    name='Agent Dashboard',
    insctructions='Take the incoming data and output the following json format 'x:y:z' for the dashboard
)
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
    name='Agent Code'
    instructions='Code in React the response from another Agent'
)

agent_post = Agent(
    name='Agent Post'
    instructions='Post on X'
)
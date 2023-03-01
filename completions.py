import os
import openai

os.environ["OPENAI_API_KEY"] = "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"

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Brainstorm some ideas combining VR and fitness:",
  temperature=0.6,
  max_tokens=150,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)

print(response)

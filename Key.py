import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Prompt for AI generation
prompt = "Generate creative text about"

# Generate text using the OpenAI GPT-3.5 API
response = openai.Completion.create(
  engine="text-davinci-003",  # You might use a different engine
  prompt=prompt,
  max_tokens=150  # You can adjust this based on your needs
)

# Get the generated text
generated_text = response['choices'][0]['text']

print(generated_text)

from openai import OpenAI

# Set your API key
client = OpenAI(api_key="YOUR_API_KEY")

# Prompt
prompt = "Write a short note on Artificial Intelligence."

# Generate text
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    max_output_tokens=100
)

# Print output
print("Prompt:", prompt)
print("\nGenerated Text:\n")
print(response.output[0].content[0].text)

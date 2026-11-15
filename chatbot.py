from openai import OpenAI

client = OpenAI()
q= input("ask any thing:  ")
response= client.responses.create(
    input=q,
    model="gpt-6-astra"
)
 
print(response.output_text)

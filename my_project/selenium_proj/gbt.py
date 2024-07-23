
#OPENAI_API_KEY
# sk-proj-AFeKnkSDoONzPf0yUdvzT3BlbkFJany2J95gK8iinZC2umJE

import openai
from openai import OpenAI

client = OpenAI(api_key='OPENAI_API_KEY',)
def ask_question(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}])
    return response.choices[0].message.content.strip()

answer = ask_question("Give me back an answer with numbers only. What is the height of the basket in the NBA in centimeters?")
print(answer)
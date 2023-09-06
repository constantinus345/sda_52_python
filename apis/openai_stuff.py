import openai
# from apis.configsx import openai_secret_key

openai.organization = ""
openai.api_key = ""

# print(openai.Model.list())

intrebarea = """

"""

#https://platform.openai.com/docs/api-reference/authentication
chat_request = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role":"system", "content":"Hello, please answer the following question with as many details as possible"},
        {"role":"user", "content": intrebarea}
    ]
)

print("Asteapta raspuns...")
raspuns = chat_request.choices[0].message
raspuns_string = raspuns["content"].encode("utf-8").decode("utf-8")
print(raspuns_string)
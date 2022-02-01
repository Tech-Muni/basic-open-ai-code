import openai

# Go to this website https://beta.openai.com/signup
# create your account get your api key and paste below.
OPEN_AI_KEY = '<your-api-key>'


def gpt3(query):
    openai.api_key = OPEN_AI_KEY
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=query,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    content = response.choices[0].text
    return content


def main():
    query = input("What is your question? ")
    response = gpt3(query=query)
    print(response)


if __name__ == '__main__':
    main()

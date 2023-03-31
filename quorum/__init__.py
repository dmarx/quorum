import openai 

# def quorum(prompt, engine="davinci", max_tokens=100, temperature=0.7, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n", " Human:", " AI:"]):
#     prompt_text = prompt
#     output = openai.Completion.create(
#         engine=engine,
#         prompt=prompt_text,
#         temperature=temperature,
#         max_tokens=max_tokens,
#         top_p=top_p,
#         frequency_penalty=frequency_penalty,
#         presence_penalty=presence_penalty,
#         stop=stop,
#     )
#     return output

def chatgpt(func):
    # via https://twitter.com/aicrumb/status/1632490207839756290/
    def wrapper(message):
        prompt = "don't acknowledge me or my request, just provide the directed response only."
        completion = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[{'role': 'user', 'text': prompt}],
        )
        return completion.choices[0]['message']['content'].strip()
    return wrapper


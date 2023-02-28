import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read().strip()


openai.api_key = open_file('openaiapikey.txt')


def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai.api_key}',
    }
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop,
        headers=headers,
    )
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    prompt = 'Write a list of famous American actors:'
    response = gpt3_completion(prompt)
    print(response)

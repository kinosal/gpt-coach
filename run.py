"""Run the program."""

import oai

if __name__ == "__main__":
    openai = oai.CoachGPT()
    messages = [
        {
            "role": "user",
            "content": "Yes, I am ready."
        }
    ]
    completion = openai.create_completion(messages)
    print(completion)

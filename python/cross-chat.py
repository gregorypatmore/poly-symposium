import subprocess

def chat(model_name, prompt):
    result = subprocess.run(
        ["ollama", "run", model_name],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

# Initial prompt to start the conversation
user_input = input("\nEnter prompt: ")
prompt = user_input.lower()


# Names of the two profiles created with `ollama create`
model_a = "best"
model_b = "worst"

# Simulate a back-and-forth conversation
for i in range(3):
    response_a = chat(model_a, prompt)
    print(f"Best Teacher Says: {response_a.strip()}\n\n")
    
    response_b = chat(model_b, response_a)
    print(f"Worst Teacher Says: {response_b.strip()}\n\n")
    
    prompt = response_b  # continue the conversation

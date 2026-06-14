from agent import CustomerSupportAgent


agent = CustomerSupportAgent()


print("Customer Support Agent Started")
print("Type 'exit' to quit\n")


while True:

    prompt = input("You: ")

    if prompt.lower() == "exit":
        print("\nGoodbye!")
        break

    answer = agent.ask(prompt)

    print("\nAI:")
    print(answer)
    print()

from agent import orquestador

file_path = "./data/M03_01_La_Paz.csv"

print("🤖 Agente listo. Escribe tu pregunta (o 'salir' para terminar)\n")

while True:
    question = input("Tú: ")
    if question.lower() in ["salir", "exit", "quit"]:
        print("👋 Adiós!")
        break

    response = orquestador(question, file_path)
    print(f"\n🤖 Agente:\n{response}\n")

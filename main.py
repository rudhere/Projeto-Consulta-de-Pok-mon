import requests

print("=== Consulta de Pokémon ===")

pokemon = input("Digite o nome de um Pokémon: ").strip().lower()

if not pokemon:
    print("Você não digitou nenhum nome!")
    exit()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nome = data["name"].capitalize()
        altura = data["height"]
        peso = data["weight"]

        tipos = [t["type"]["name"] for t in data["types"]]
        habilidades = [a["ability"]["name"] for a in data["abilities"]]

        print("\n--- Resultado ---")
        print(f"Nome: {nome}")
        print(f"Altura: {altura}")
        print(f"Peso: {peso}")
        print(f"Tipos: {', '.join(tipos)}")
        print(f"Habilidades: {', '.join(habilidades)}")

        # Salvando no arquivo
        with open("pokemon_info.txt", "w", encoding="utf-8") as f:
            f.write("=== Informações do Pokémon ===\n\n")
            f.write(f"Nome: {nome}\n")
            f.write(f"Altura: {altura}\n")
            f.write(f"Peso: {peso}\n")
            f.write(f"Tipos: {', '.join(tipos)}\n")
            f.write(f"Habilidades: {', '.join(habilidades)}\n")

        print("\nAs informações foram salvas em 'pokemon_info.txt'")

    else:
        print("Pokémon não encontrado! Verifique o nome e tente novamente.")

except requests.exceptions.RequestException:
    print("Erro ao conectar à API. Verifique sua conexão com a internet.")

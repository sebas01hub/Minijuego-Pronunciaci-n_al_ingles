import random
from transcript import speech
from motor_voz import hablar

words_by_level = {
    "facil": [
        "cat", "dog", "apple", "milk", "sun", "book", "house", "car", "tree", "water",
        "fish", "blue", "red", "happy", "school"
    ],
    "medio": [
        "banana", "school", "friend", "window", "yellow", "garden", "family", "morning", "teacher", 
        "computer", "holiday", "country", "picture", "kitchen", "animal"
    ],
    "dificil": [
        "technology", "university", "information", "pronunciation", "imagination", "environment", 
        "communication", "responsibility", "opportunity", "development", "experience", "knowledge", 
        "adventure", "conversation", "achievement"
    ]
}

def jugar_nivel(nivel, palabras, puntos):
    print(f"\n--- Nivel {nivel.upper()} ---")

    for i in range(5):
        palabra = random.choice(palabras)
        print(f"\nPalabra: {palabra}")

        respuesta = speech()

        if respuesta == "":
            continue

        print(f"Dijiste: {respuesta}")

        if respuesta == palabra:
            puntos += 10
            print("Correcto. +10 puntos")
        else:
            print("Incorrecto.")
            hablar(f"La pronunciación correcta es {palabra}")

        print(f"Puntos: {puntos}")

    return puntos

def main():
    puntos = 0

    print("      ##################################")
    print("       Juego de pronunciacion en ingles")
    print("      ##################################")
    print("Pronuncia correctamente las palabras en inglés.")

    for nivel in ["facil", "medio", "dificil"]:
        puntos = jugar_nivel(nivel, words_by_level[nivel], puntos)

    print("\n-------------------------------")
    print(f"Puntuacion final: {puntos}")
    print("-------------------------------")

if __name__ == "__main__":
    main()

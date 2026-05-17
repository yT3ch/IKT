# Iskolai Kaland - Fejlesztett verzió

import time
import random

questions = [
    {
        "question": "1. Mennyi a derékszögű háromszög átfogója, ha a befogók: 3 és 4?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "A"
    },
    {
        "question": "2. Thálész-tétel szerint milyen háromszög keletkezik félkörben?",
        "options": ["A) Egyenlő szárú", "B) Derékszögű", "C) Tompaszögű", "D) Hegyesszögű"],
        "answer": "B"
    },
    {
        "question": "3. Mennyi a másik befogó, ha az átfogó 13 és az egyik befogó 5?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C"
    },
    {
        "question": "4. Mennyi 8²?",
        "options": ["A) 16", "B) 32", "C) 64", "D) 128"],
        "answer": "C"
    },
    {
        "question": "5. Mennyi a háromszög belső szögeinek összege?",
        "options": ["A) 90°", "B) 180°", "C) 270°", "D) 360°"],
        "answer": "B"
    },
    {
        "question": "6. Melyik szám lehet derékszögű háromszög oldalhármasa?",
        "options": ["A) 2,3,4", "B) 3,4,5", "C) 5,6,7", "D) 4,5,6"],
        "answer": "B"
    },
    {
        "question": "7. Mennyi 12 × 12?",
        "options": ["A) 124", "B) 134", "C) 144", "D) 154"],
        "answer": "C"
    },
    {
        "question": "8. Mi a Thálész-tétel lényege?",
        "options": [
            "A) Félkörben a kerületi szög derékszög",
            "B) A háromszög szögei egyenlők",
            "C) Minden kör sugara azonos",
            "D) A négyzet oldalai egyenlők"
        ],
        "answer": "A"
    },
    {
        "question": "9. Mennyi az átfogó, ha a befogók 6 és 8?",
        "options": ["A) 9", "B) 10", "C) 12", "D) 14"],
        "answer": "B"
    },
    {
        "question": "10. Mennyi 15²?",
        "options": ["A) 125", "B) 200", "C) 225", "D) 250"],
        "answer": "C"
    }
]

# Véletlen sorrend
random.shuffle(questions)

lives = 3
score = 0
level = 1

print("🎓 ISKOLAI KALAND 🎓")
print("Elindultál az iskola bejáratától!")
print("Cél: szerezd meg a diplomát!\n")

for q in questions:

    if lives == 0:
        break

    print("\n==============================")
    print(f"📚 SZINT: {level}")
    print(f"❤️ Életek: {lives}")
    print(f"⭐ Pontszám: {score}")
    print("==============================")

    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    print("\n⏳ 30 másodperced van válaszolni!")

    start_time = time.time()

    answer = input("\nVálasz (A/B/C/D): ").upper()

    end_time = time.time()

    elapsed = end_time - start_time

    if elapsed > 30:
        print("\n⌛ Lejárt az idő!")
        lives -= 1

    elif answer == q["answer"]:
        print("\n✅ Helyes válasz!")
        score += 10
        level += 1

    else:
        print("\n❌ Rossz válasz!")
        lives -= 1

# Játék vége
print("\n==============================")

if lives > 0:
    print("🎓 GRATULÁLOK!")
    print("Megszerezted a diplomát!")
else:
    print("💀 GAME OVER")
    print("Nem sikerült megszerezni a diplomát.")

print(f"\n⭐ Végső pontszám: {score}")
print("==============================")
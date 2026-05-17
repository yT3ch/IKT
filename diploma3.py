# 🎓 ISKOLAI KALAND - DIPLOMA DAVID FINAL BOSS 🎓

import random
import time

# =========================================
# EFFEKTEK
# =========================================

def loading(text):
    print(f"\n{text}", end="")
    for i in range(5):
        time.sleep(0.3)
        print(".", end="")
    print("\n")

def explosion():
    print("""
💥💥💥💥💥💥💥💥
⚡ KRITIKUS TALÁLAT ⚡
💥💥💥💥💥💥💥💥
""")

def boss_attack():
    print("""
🔥🔥🔥🔥🔥🔥🔥🔥
👨‍🏫 DIPLOMA DAVID TÁMAD!
🔥🔥🔥🔥🔥🔥🔥🔥
""")

def combo_effect(combo):
    print(f"""
🔥🔥🔥 {combo} COMBO 🔥🔥🔥
⚡ MATEK ERŐ NÖVEKSZIK ⚡
""")

# =========================================
# KÉRDÉSEK
# =========================================

questions = [
    {
        "question": "Mennyi 15²?",
        "options": ["A) 125", "B) 200", "C) 225", "D) 250"],
        "answer": "C"
    },
    {
        "question": "Mennyi a háromszög belső szögeinek összege?",
        "options": ["A) 90°", "B) 180°", "C) 270°", "D) 360°"],
        "answer": "B"
    },
    {
        "question": "Mennyi az átfogó, ha a befogók 5 és 12?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "D"
    },
    {
        "question": "Thálész-tétel szerint félkörben milyen szög található?",
        "options": ["A) 45°", "B) 90°", "C) 60°", "D) 120°"],
        "answer": "B"
    },
    {
        "question": "Mennyi 9²?",
        "options": ["A) 18", "B) 72", "C) 81", "D) 99"],
        "answer": "C"
    },
    {
        "question": "Melyik Pitagorasz-hármas helyes?",
        "options": ["A) 3,4,5", "B) 2,3,5", "C) 5,5,5", "D) 4,4,9"],
        "answer": "A"
    },
    {
        "question": "Mennyi 7×8?",
        "options": ["A) 54", "B) 56", "C) 64", "D) 72"],
        "answer": "B"
    },
    {
        "question": "Mennyi az átfogó, ha a befogók 8 és 15?",
        "options": ["A) 16", "B) 17", "C) 18", "D) 19"],
        "answer": "B"
    },
    {
        "question": "Mennyi 13²?",
        "options": ["A) 139", "B) 149", "C) 169", "D) 196"],
        "answer": "C"
    },
    {
        "question": "Mi a befogó tétel egyik képlete?",
        "options": ["A) a²=c·p", "B) a+b=c", "C) c²=a+b", "D) ab=c"],
        "answer": "A"
    }
]

random.shuffle(questions)

# =========================================
# JÁTÉK ADATOK
# =========================================

score = 0
lives = 5
combo = 0

# =========================================
# INTRO
# =========================================

print("""
🏫🏫🏫🏫🏫🏫🏫🏫🏫🏫

      ISKOLAI KALAND

🏫🏫🏫🏫🏫🏫🏫🏫🏫🏫
""")

loading("📚 Belépés az iskolába")

print("🙂 A diák elindult a diploma felé...")
time.sleep(1)

print("📖 Matematikai próbatételek következnek...\n")
time.sleep(1)

# =========================================
# FŐ JÁTÉK
# =========================================

for i, q in enumerate(questions):

    if lives <= 0:
        break

    print("\n====================================")
    print(f"📚 SZINT {i+1}")
    print(f"❤️ HP: {lives}")
    print(f"⭐ PONT: {score}")
    print("====================================")

    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("\n👉 Válasz (A/B/C/D): ").upper()

    if answer == q["answer"]:

        explosion()
        print("✅ HELYES!")

        score += 10
        combo += 1

        if combo >= 3:
            combo_effect(combo)

    else:
        print("\n❌ ROSSZ!")
        boss_attack()

        lives -= 1
        combo = 0

# =========================================
# FINAL BOSS
# =========================================

if lives > 0:

    loading("🌑 A végső terem megnyílik")

    print("""
██████╗ ██╗██████╗ ██╗      ██████╗ ███╗   ███╗ █████╗
██╔══██╗██║██╔══██╗██║     ██╔═══██╗████╗ ████║██╔══██╗
██║  ██║██║██████╔╝██║     ██║   ██║██╔████╔██║███████║
██║  ██║██║██╔═══╝ ██║     ██║   ██║██║╚██╔╝██║██╔══██║
██████╔╝██║██║     ███████╗╚██████╔╝██║ ╚═╝ ██║██║  ██║
╚═════╝ ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
""")

    print("""
🔥🔥🔥 DIPLOMA DAVID 🔥🔥🔥

👨‍🏫 A nevezetes azonosságok ura
⚡ A matematika sötét mestere
💀 Végső vizsga készítő
""")

    boss_hp = 5

    boss_questions = [

        {
            "question": "(a+b)² = ?",
            "options": [
                "A) a²+b²",
                "B) a²+2ab+b²",
                "C) 2a²+b²",
                "D) a²-ab+b²"
            ],
            "answer": "B"
        },

        {
            "question": "(a-b)² = ?",
            "options": [
                "A) a²+b²",
                "B) a²-2ab+b²",
                "C) a²-ab",
                "D) 2ab"
            ],
            "answer": "B"
        },

        {
            "question": "(a+b)(a-b) = ?",
            "options": [
                "A) a²-b²",
                "B) a²+b²",
                "C) 2ab",
                "D) ab²"
            ],
            "answer": "A"
        },

        {
            "question": "(x+5)² = ?",
            "options": [
                "A) x²+10x+25",
                "B) x²+25",
                "C) x²+5x+25",
                "D) 2x²"
            ],
            "answer": "A"
        },

        {
            "question": "(2a-b)² = ?",
            "options": [
                "A) 4a²-4ab+b²",
                "B) 2a²-b²",
                "C) 4a²+b²",
                "D) a²-b²"
            ],
            "answer": "A"
        }

    ]

    for q in boss_questions:

        if boss_hp <= 0 or lives <= 0:
            break

        print("\n====================================")
        print(f"👨‍🏫 DIPLOMA DAVID HP: {boss_hp}")
        print(f"🙂 JÁTÉKOS HP: {lives}")
        print("====================================")

        print("\n🔥 BOSS KÉRDÉS 🔥")
        print(q["question"])

        for option in q["options"]:
            print(option)

        answer = input("\n⚔️ Válasz: ").upper()

        if answer == q["answer"]:

            explosion()
            print("⚡ DIPLOMA DAVID SEBZŐDÖTT!")
            boss_hp -= 1
            score += 15

        else:

            boss_attack()
            print("💀 MEGSEBZETT A BOSS!")
            lives -= 1

# =========================================
# ENDING
# =========================================

print("\n====================================")
print("🎓 JÁTÉK VÉGE 🎓")
print("====================================")

print(f"\n⭐ VÉGSŐ PONT: {score}")

# RANG

if score <= 30:
    print("\n💀 RANG: Bukó lista")

elif score <= 70:
    print("\n📚 RANG: Közepes matekos")

else:
    print("\n👑 RANG: Nevezetes azonosság profi")

# Befejezés

if lives > 0:

    print("""
🎓🎓🎓🎓🎓🎓🎓🎓🎓🎓

 GRATULÁLUNK!

 LEGYŐZTED
 DIPLOMA DAVIDOT!

 MEGSZEREZTED A DIPLOMÁT!

🎓🎓🎓🎓🎓🎓🎓🎓🎓🎓
""")

else:

    print("""
💀💀💀 GAME OVER 💀💀💀

Diploma David győzött...

📚 Többet kell tanulnod.
""")
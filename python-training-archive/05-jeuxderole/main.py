from random import randint

# Initial stats for the player and the enemy
PLAYER_HP = 50
ENEMY_HP = 50
POTIONS = 3
skip_turn = False

print("⚔️ The Battle Begins ⚔️")

# Main game loop — runs as long as both players are alive
while PLAYER_HP > 0 and ENEMY_HP > 0:

    # If the player used a potion last turn, they skip their attack
    if skip_turn:
        enemy_damage = randint(5, 15)
        PLAYER_HP -= enemy_damage
        print(f"UNABLE TO ATTACK! You took {enemy_damage} damage! ⚔️ HP remaining: {PLAYER_HP} ❤️")
        print("-" * 50)
        if PLAYER_HP <= 0:
            print("YOU LOSE ❌")
            break
        skip_turn = False
        continue

    # Ask the player for their action
    try:
        choice = int(input("Attack 🗡️ (1) or use a potion 🧪 (2)? "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        continue

    # Option 1 — Attack
    if choice == 1:
        player_damage = randint(5, 10)
        ENEMY_HP -= player_damage
        print(f"You dealt {player_damage} damage to the enemy! ⚔️")
        if ENEMY_HP <= 0:
            print("🎊 YOU WIN 🎊")
            break

    # Option 2 — Use a potion
    elif choice == 2:
        if POTIONS > 0:
            skip_turn = True
            heal = randint(15, 50)
            PLAYER_HP += heal
            POTIONS -= 1
            if PLAYER_HP > 50:
                PLAYER_HP = 50
            print(f"You healed {heal} HP ❤️ (Potions remaining: {POTIONS} 🧪)")
        else:
            print("No potions left! 🛑")
            continue
    else:
        print("Invalid choice. Please try again.")
        continue

    # Enemy attacks if still alive
    if ENEMY_HP > 0:
        enemy_damage = randint(5, 15)
        PLAYER_HP -= enemy_damage
        print(f"You took {enemy_damage} damage! ⚔️\nYour HP: {PLAYER_HP} ❤️ | Enemy HP: {ENEMY_HP}")
        if PLAYER_HP <= 0:
            print("YOU LOSE ❌")
            break
        print("-" * 50)
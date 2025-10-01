import random

# Skapa kortleken
def create_deck():
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Räkna ut poäng för en hand
def calculate_score(hand):
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

    score = sum(values[card[0]] for card in hand)
    # Justera ess (A) från 11 till 1 om man är över 21
    aces = sum(1 for card in hand if card[0] == "A")
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

# Visa kort
def show_hand(hand, hide_first=False):
    if hide_first:
        return "[??] " + " ".join(f"[{rank}{suit}]" for rank, suit in hand[1:])
    return " ".join(f"[{rank}{suit}]" for rank, suit in hand)

def blackjack():
    deck = create_deck()

    # Dela ut två kort till spelare och dator
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("🎲 Blackjack börjar!\n")
    print("Dina kort:", show_hand(player_hand), "=>", calculate_score(player_hand))
    print("Dealerns kort:", show_hand(dealer_hand, hide_first=True))

    # Spelarens tur
    while True:
        if calculate_score(player_hand) == 21:
            print("🎉 Blackjack! Du stannar automatiskt.")
            break

        choice = input("Vill du [h]it eller [s]tand? ").lower()
        if choice == "h":
            player_hand.append(deck.pop())
            print("Du drog:", show_hand([player_hand[-1]]))
            print("Dina kort:", show_hand(player_hand), "=>", calculate_score(player_hand))

            if calculate_score(player_hand) > 21:
                print("💥 Du gick över 21! Du förlorade.")
                return
        elif choice == "s":
            break
        else:
            print("Ogiltigt val, skriv 'h' eller 's'.")

    # Dealerns tur
    print("\nDealerns tur:")
    print("Dealerns kort:", show_hand(dealer_hand), "=>", calculate_score(dealer_hand))

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print("Dealern drog:", show_hand([dealer_hand[-1]]))
        print("Dealerns kort:", show_hand(dealer_hand), "=>", calculate_score(dealer_hand))

    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)

    # Avgör resultat
    if dealer_score > 21:
        print("🎉 Dealern gick över 21. Du vinner!")
    elif dealer_score > player_score:
        print("😢 Dealern vann med", dealer_score, "mot dina", player_score)
    elif dealer_score < player_score:
        print("🎉 Du vann med", player_score, "mot dealerns", dealer_score)
    else:
        print("🤝 Oavgjort! Båda har", player_score)

if __name__ == "__main__":
    blackjack()

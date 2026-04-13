import random


# -----------------------------
# Deck Class
# -----------------------------
class Deck:
    def __init__(self):
        """Create a standard deck of 52 cards"""
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        self.cards = [rank + " of " + suit for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        """Remove and return the top card from the deck"""
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


# -----------------------------
# Function to deal initial hand
# -----------------------------
def deal_hand(deck):
    """Deal 5 cards from the deck"""
    hand = []
    for _ in range(5):
        hand.append(deck.deal_card())
    return hand


# -----------------------------
# Function to display hand
# -----------------------------
def display_hand(hand):
    """Display cards with position numbers"""
    print("\nYour current hand:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")


# -----------------------------
# Function to replace cards
# -----------------------------
def replace_cards(deck, hand):
    """Allow user to replace selected cards"""
    choices = input("\nEnter card positions to replace (e.g., 1,3,5) or press Enter to keep all: ")

    if choices.strip() == "":
        return hand

    try:
        positions = [int(x.strip()) for x in choices.split(",")]

        for pos in positions:
            if 1 <= pos <= 5:
                hand[pos - 1] = deck.deal_card()
            else:
                print(f"Ignoring invalid position: {pos}")

    except ValueError:
        print("Invalid input. No cards replaced.")

    return hand


# -----------------------------
# Main function
# -----------------------------
def main():
    """Main game logic"""
    deck = Deck()

    # Deal initial hand
    hand = deal_hand(deck)
    display_hand(hand)

    # Replace selected cards
    hand = replace_cards(deck, hand)

    # Show final hand
    print("\nFinal hand:")
    for card in hand:
        print(card)


# -----------------------------
# Run program
# -----------------------------
if __name__ == "__main__":
    main()
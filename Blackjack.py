import random

# Move a card from deck to hand
def draw_card(hand, deck):
    hand.append(deck.pop())   # take last card from deck


# Calculate the score of a hand
def calculate_score(hand):
    score = 0
    aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            aces += 1
        else:
            score += int(card)

    for _ in range(aces):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1



# Print game status
def print_status(player_hand, dealer_hand, hide_dealer_card=True):
    print("\n--- Current Game Status ---")

    if hide_dealer_card:
        print("Dealer's hand: ", dealer_hand[0], "[hidden]")
    else:
        print("Dealer's hand: ", dealer_hand, 
              "(Score:", calculate_score(dealer_hand), ")")

    print("Your hand: ", player_hand, 
          "(Score:", calculate_score(player_hand), ")")


# Main game loop
def main():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    player_hand = []
    dealer_hand = []

    # shuffle the deck
    random.shuffle(deck)

    # Dealer draws one card (shown)
    draw_card(dealer_hand, deck)

    # Player draws two cards
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)

    # Player turn
    while True:
        print_status(player_hand, dealer_hand, hide_dealer_card=True)

        player_score = calculate_score(player_hand)
        if player_score > 21:
            print("\nYou busted! Your score is", player_score)
            print("Dealer wins.")
            return

        choice = input("\nDo you want to hit or stay? (h/s): ").lower()
        if choice == "h":
            draw_card(player_hand, deck)
        elif choice == "s":
            break
        else:
            print("Please enter 'h' for hit or 's' for stay.")

    # Dealer turn
    print("\nDealer's turn...")
    print_status(player_hand, dealer_hand, hide_dealer_card=False)

    while calculate_score(dealer_hand) < 17:
        draw_card(dealer_hand, deck)
        print_status(player_hand, dealer_hand, hide_dealer_card=False)

    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)

    # Determine winner
    print("\n--- Final Results ---")
    print("Dealer score:", dealer_score)
    print("Your score:", player_score)

    if dealer_score > 21:
        print("Dealer busted! You win!")
    elif dealer_score > player_score:
        print("Dealer wins!")
    elif dealer_score < player_score:
        print("You win!")
    else:
        print("It's a tie!")


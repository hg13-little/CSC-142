import pygame
import pygwidgets
import random
import sys
pygame.init()
# --------------------------------------------------
# Constants
# --------------------------------------------------
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 650
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 110, 0)
GOLD = (255, 215, 0)
RED = (180, 0, 0)
DEALER_STAND_VALUE = 17
# --------------------------------------------------
# Card and Deck Classes
# --------------------------------------------------
class Card:
    def __init__(self, rank):
        self.rank = rank
    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)
class Deck:
    def __init__(self):
        # Single-suit deck for simplicity
        self.cards = ['2', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'J', 'Q', 'K', 'A']
        random.shuffle(self.cards)
    def deal_card(self):
        if len(self.cards) == 0:
            self.__init__()
        return Card(self.cards.pop())
# --------------------------------------------------
# Blackjack Helper Functions
# --------------------------------------------------
def draw_card(hand, deck):
    hand.append(deck.deal_card())
def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        if card.rank == 'A':
            ace_count += 1
        else:
            score += card.get_value()
    for _ in range(ace_count):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    return score
def hand_to_string(hand):
    return ' '.join(card.rank for card in hand)
def visible_dealer_hand_string(hand, show_all):
    if show_all:
        return hand_to_string(hand)
    if len(hand) == 0:
        return ''
    if len(hand) == 1:
        return hand[0].rank
    return f'{hand[0].rank} ?'
def start_new_round():
    deck = Deck()
    player_hand = []
    dealer_hand = []
    # Dealer draws two cards (first visible)
    draw_card(dealer_hand, deck)
    draw_card(dealer_hand, deck)
    # Player receives two cards
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)
    return deck, player_hand, dealer_hand
# --------------------------------------------------
# Setup Window
# --------------------------------------------------
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Simple Blackjack')
clock = pygame.time.Clock()
# --------------------------------------------------
# Text Displays
# --------------------------------------------------
title_text = pygwidgets.DisplayText(
    window, (300, 20),
    'Simple Blackjack',
    fontName='arial',
    fontSize=36,
    textColor=GOLD
)
dealer_label = pygwidgets.DisplayText(window, (60, 110), 'Dealer', fontName='arial', fontSize=28, textColor=WHITE)
dealer_cards_text = pygwidgets.DisplayText(window, (60, 160), '', fontName='courier', fontSize=30, textColor=WHITE)
dealer_score_text = pygwidgets.DisplayText(window, (60, 210), '', fontName='arial', fontSize=24, textColor=WHITE)
player_label = pygwidgets.DisplayText(window, (60, 340), 'Player', fontName='arial', fontSize=28, textColor=WHITE)
player_cards_text = pygwidgets.DisplayText(window, (60, 390), '', fontName='courier', fontSize=30, textColor=WHITE)
player_score_text = pygwidgets.DisplayText(window, (60, 440), '', fontName='arial', fontSize=24, textColor=WHITE)
message_text = pygwidgets.DisplayText(window, (60, 540), 'Click Deal to start', fontName='arial', fontSize=26, textColor=WHITE)
# --------------------------------------------------
# Buttons
# --------------------------------------------------
deal_button = pygwidgets.TextButton(window, (650, 140), 'Deal', width=180, height=45)
hit_button = pygwidgets.TextButton(window, (650, 210), 'Hit', width=180, height=45)
stay_button = pygwidgets.TextButton(window, (650, 280), 'Stay', width=180, height=45)
quit_button = pygwidgets.TextButton(window, (650, 350), 'Quit', width=180, height=45)
# --------------------------------------------------
# Game State
# --------------------------------------------------
deck = None
player_hand = []
dealer_hand = []
round_active = False
round_over = True
show_dealer_cards = False
message = 'Click Deal to start'
# --------------------------------------------------
# Main Loop
# --------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Deal button
        if deal_button.handleEvent(event):
            deck, player_hand, dealer_hand = start_new_round()
            round_active = True
            round_over = False
            show_dealer_cards = False
            message = 'Hit or Stay?'
        # Hit button
        if hit_button.handleEvent(event):
            if round_active and not round_over:
                draw_card(player_hand, deck)
                if calculate_score(player_hand) > 21:
                    show_dealer_cards = True
                    message = 'You busted! You lose!'
                    round_over = True
        # Stay button
        if stay_button.handleEvent(event):
            if round_active and not round_over:
                show_dealer_cards = True
                while calculate_score(dealer_hand) < DEALER_STAND_VALUE:
                    draw_card(dealer_hand, deck)
                player_score = calculate_score(player_hand)
                dealer_score = calculate_score(dealer_hand)
                if dealer_score > 21:
                    message = 'Dealer busts! You win!'
                elif dealer_score > player_score:
                    message = 'Dealer wins!'
                elif dealer_score < player_score:
                    message = 'You win!'
                else:
                    message = "It's a tie!"
                round_over = True
        # Quit button
        if quit_button.handleEvent(event):
            pygame.quit()
            sys.exit()
    # --------------------------------------------------
    # Update Display Values
    # --------------------------------------------------
    if round_active:
        player_cards_text.setValue(hand_to_string(player_hand))
        player_score_text.setValue(f"Player's total is {calculate_score(player_hand)}")
        dealer_cards_text.setValue(visible_dealer_hand_string(dealer_hand, show_dealer_cards))
        if show_dealer_cards:
            dealer_score_text.setValue(f"Dealer's total is {calculate_score(dealer_hand)}")
        else:
            dealer_score_text.setValue("Dealer's second card is hidden")
    else:
        player_cards_text.setValue('')
        player_score_text.setValue('')
        dealer_cards_text.setValue('')
        dealer_score_text.setValue('')
    message_text.setValue(message)
    # --------------------------------------------------
    # Draw Screen
    # --------------------------------------------------
    window.fill(GREEN)
    title_text.draw()
    dealer_label.draw()
    dealer_cards_text.draw()
    dealer_score_text.draw()
    player_label.draw()
    player_cards_text.draw()
    player_score_text.draw()
    message_text.draw()
    deal_button.draw()
    hit_button.draw()
    stay_button.draw()
    quit_button.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
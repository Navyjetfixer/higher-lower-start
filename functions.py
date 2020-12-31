from random import randint
from game_data import data
from replit import clear
from art import logo, vs
def generate_followed():
    return data[randint(0, len(data) - 1)]


def print_follower_format(letter, follower_dict):
    print(f"Compare {letter}: {follower_dict['name']}, {follower_dict['description']}, from {follower_dict['country']}")
    print(follower_dict['follower_count'])

def evaluate_player_choice(choice, count_a, count_b):
    if count_a['follower_count'] >= count_b['follower_count']:
        if choice == 'a':
            return 'winner'
        else:
            return 'loser'
    if count_a['follower_count'] < count_b['follower_count']:
        if choice == 'b':
            return 'winner'
        else:
            return 'loser'

def print_logo():
    clear()
    print(logo)

def print_vs(followed_a, followed_b):
    print_follower_format('A', followed_a)
    print(vs)
    print_follower_format('B', followed_b)
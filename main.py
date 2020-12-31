
from functions import print_follower_format, generate_followed, evaluate_player_choice, print_logo, print_vs



def game():
    score = 0
    print_logo()

    followed_a = generate_followed()
    followed_b = generate_followed()
    print_vs(followed_a, followed_b)

    while True:
        player_choice = input("Who has more followers? Type 'A' or 'B: '").lower()
    
        if evaluate_player_choice(player_choice, followed_a, followed_b) == 'winner':
            score += 1
            followed_a = followed_b
            followed_b = generate_followed()
            print_logo()
            print(f"Your right!, Current score: {score}.")
            print_vs(followed_a, followed_b)
        else:
            print_logo()
            print(f"Your wrong! Current score: {score}.")
            break

game()
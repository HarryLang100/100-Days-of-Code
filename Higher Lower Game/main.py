import random

from art import logo, vs
from game_data import data


def get_items_index_pair(items_not_used):
    A_index, B_index = random.sample(items_not_used, k=2)
    items_not_used.remove(A_index)
    items_not_used.remove(B_index)
    return A_index, B_index, items_not_used


def format_account(account):
    string = f"{account['name']}, a {account['description']}, from {account['country']}"
    return string


def main():
    print(logo)

    still_playing = True
    score = 0
    items_not_used = list(range(len(data)))

    while still_playing:
        A_index, B_index, items_not_used = get_items_index_pair(items_not_used)
        correct_answer = 'A' if data[A_index]['follower_count'] > data[B_index]['follower_count'] else 'B'
        first_string = (
            f"Compare A: {data[A_index]['name']}, a {data[A_index]['description']}, from {data[A_index]['country']}"
        )
        print(f"Compare A: {format_account(data[A_index])}")
        print(vs)
        second_string = (
            f"Against B: {format_account(data[B_index])}"
        )
        print(second_string)
        print("-" * 35)
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        if user_input.upper() == correct_answer:
            score += 1
            print("*" * 35)
            print(f"You're right! Current score: {score}.")
            print("*" * 35)
        else:
            print("=" * 35)
            print(f"Sorry, that's wrong. Final score: {score}.")
            print("=" * 35)
            still_playing = False


if __name__ == "__main__":
    play_again = True
    while play_again:
        main()
        choice = input("Press 'y' to play again, or anything else to exit: ")
        if choice.lower() == 'y':
            pass
        else:
            play_again = False

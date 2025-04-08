from yatzy import Yatzy

def play_mock_game():
    game = Yatzy()
    print(f"Initial roll: {game.get_dice()}")
    print("Scoring options:")
    print(f"Ones: {game.Ones()}")
    print(f"Twos: {game.Twos()}")
    print(f"OnePair: {game.OnePair()}")
    print(f"TwoPairs: {game.TwoPairs()}")
    print(f"ThreeAlike: {game.ThreeAlike()}")
    print(f"FourAlike: {game.FourAlike()}")
    print(f"Small: {game.Small()}")
    print(f"Large: {game.Large()}")
    print(f"FullCourse: {game.FullCourse()}")
    print(f"Chance: {game.Chance()}")
    print(f"Yatzy: {game.Yatzy()}")

if __name__ == "__main__":
    play_mock_game()
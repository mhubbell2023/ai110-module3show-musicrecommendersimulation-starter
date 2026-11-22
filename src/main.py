"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.2
        },
        "Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95
        }
    }

    for profile_name, profile in profiles.items():
        user_prefs = {
            "genre": profile["favorite_genre"],
            "mood": profile["favorite_mood"],
            "energy": profile["target_energy"]
        }

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name} — Top 5 Recommendations")
        print("=" * (len(profile_name) + 24))

        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec

            print(f"\n{rank}. {song['title']}")
            print(f"   Artist: {song['artist']}")
            print(f"   Score: {score:.2f}")
            print("   Reasons:")

            for reason in explanation.split("; "):
                print(f"   - {reason}")


if __name__ == "__main__":
    main()

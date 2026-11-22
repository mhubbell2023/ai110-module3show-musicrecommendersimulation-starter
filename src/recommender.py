from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
from pathlib import Path

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert their numerical features."""
    print(f"Loading songs from {csv_path}...")

    path = Path(csv_path)
    if not path.is_absolute():
        project_root = Path(__file__).resolve().parent.parent
        path = project_root / path

    songs = []
    with path.open("r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if "id" in row:
                row["id"] = int(row["id"])

            if "energy" in row:
                row["energy"] = float(row["energy"])

            if "tempo_bpm" in row:
                row["tempo_bpm"] = int(row["tempo_bpm"])

            if "valence" in row:
                row["valence"] = float(row["valence"])

            if "danceability" in row:
                row["danceability"] = float(row["danceability"])

            if "acousticness" in row:
                row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a song's weighted match score and explain its score."""
    # Get preferences and song values with beginner-friendly defaults.
    preferred_genre = str(user_prefs.get("genre", "")).lower()
    preferred_mood = str(user_prefs.get("mood", "")).lower()
    target_energy = float(user_prefs.get("energy", 0.0))

    song_genre = str(song.get("genre", "")).lower()
    song_mood = str(song.get("mood", "")).lower()
    song_energy = float(song.get("energy", 0.0))

    # Genre: 40% if it matches, otherwise 0%.
    genre_score = 1.0 if song_genre == preferred_genre and preferred_genre else 0.0

    # Mood: 30% if it matches, otherwise 0%.
    mood_score = 1.0 if song_mood == preferred_mood and preferred_mood else 0.0

    # Energy similarity: 30%, with 1.0 for an exact match.
    energy_similarity = 1.0 - abs(song_energy - target_energy)
    energy_similarity = max(0.0, min(1.0, energy_similarity))

    score = (0.40 * genre_score) + (0.30 * mood_score) + (0.30 * energy_similarity)
    score = max(0.0, min(1.0, score))

    reasons = []

    if genre_score == 1.0:
        reasons.append(f"Genre matches your preference: {song.get('genre')}")
    else:
        reasons.append(f"Genre '{song.get('genre')}' differs from your preference '{user_prefs.get('genre')}'")

    if mood_score == 1.0:
        reasons.append(f"Mood matches your preference: {song.get('mood')}")
    else:
        reasons.append(f"Mood '{song.get('mood')}' differs from your preference '{user_prefs.get('mood')}'")

    reasons.append(
        f"Energy similarity is {energy_similarity:.2f} "
        f"(song: {song_energy:.2f}, target: {target_energy:.2f})"
    )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, rank it from highest to lowest, and return the top matches."""
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        recommendations.append((song, score, explanation))

    recommendations = sorted(
        recommendations,
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    return recommendations[:k]

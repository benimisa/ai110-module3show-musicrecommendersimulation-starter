import csv
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

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
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        scored: List[Tuple[Song, float, List[str]]] = []
        for song in self.songs:
            score, reasons = score_song(prefs, song)
            scored.append((song, score, reasons))

        scored.sort(key=lambda item: item[1], reverse=True)
        return [song for song, _, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(prefs, song)
        if not reasons:
            return "No strong matches found."
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if not row.get("id"):
                continue
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            row["genre"] = row["genre"].strip().lower()
            row["mood"] = row["mood"].strip().lower()
            songs.append(row)
    return songs

def _get_song_value(song: Any, key: str) -> Any:
    if isinstance(song, dict):
        return song.get(key)
    return getattr(song, key, None)


def score_song(user_prefs: Dict, song: Any) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    genre_pref = user_prefs.get("genre") or user_prefs.get("favorite_genre")
    mood_pref = user_prefs.get("mood") or user_prefs.get("favorite_mood")
    if "energy" in user_prefs:
        target_energy = user_prefs["energy"]
    else:
        target_energy = user_prefs.get("target_energy")
    if "target_valence" in user_prefs:
        target_valence = user_prefs["target_valence"]
    else:
        target_valence = None
    if "target_tempo" in user_prefs:
        target_tempo = user_prefs["target_tempo"]
    else:
        target_tempo = None
    likes_acoustic = user_prefs.get("likes_acoustic")

    song_genre = _get_song_value(song, "genre")
    song_mood = _get_song_value(song, "mood")
    song_energy = float(_get_song_value(song, "energy") or 0.0)
    song_valence = float(_get_song_value(song, "valence") or 0.0)
    song_tempo = float(_get_song_value(song, "tempo_bpm") or 0.0)
    acousticness = float(_get_song_value(song, "acousticness") or 0.0)

    if genre_pref and song_genre and genre_pref.strip().lower() == song_genre.strip().lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if mood_pref and song_mood and mood_pref.strip().lower() == song_mood.strip().lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    if target_energy is not None:
        energy_bonus = max(0.0, 1.0 - abs(song_energy - float(target_energy))) * 2.0
        score += energy_bonus
        reasons.append(f"energy closeness (+{energy_bonus:.2f})")

    if target_valence is not None:
        valence_bonus = max(0.0, 1.0 - abs(song_valence - float(target_valence))) * 1.2
        score += valence_bonus
        reasons.append(f"valence closeness (+{valence_bonus:.2f})")

    if target_tempo is not None and song_tempo > 0:
        tempo_bonus = max(0.0, 1.0 - abs(song_tempo - float(target_tempo)) / 120.0) * 1.0
        score += tempo_bonus
        reasons.append(f"tempo closeness (+{tempo_bonus:.2f})")

    if likes_acoustic is True and acousticness >= 0.6:
        score += 0.5
        reasons.append("acoustic preference (+0.5)")
    elif likes_acoustic is False and acousticness <= 0.3:
        score += 0.5
        reasons.append("low-acoustic preference (+0.5)")

    if not reasons:
        reasons.append("no strong matches")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "no strong matches"
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]

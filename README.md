# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This simulator uses a small catalog of songs and a simple scoring rule to rank tracks for a user profile. It combines exact matches for genre and mood with closeness-based scores for energy, valence, and tempo so that songs are recommended based on how well they fit a user's musical vibe.

---

## How The System Works

Each `Song` uses these features in the system:
- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `acousticness`

The `UserProfile` stores:
- `favorite_genre`
- `favorite_mood`
- `target_energy`
- `likes_acoustic`

The recommender computes a score for each song by:
- giving a strong bonus when the song genre matches the user's favorite genre
- giving a smaller bonus when the song mood matches the user's favorite mood
- rewarding songs whose energy is closer to the user's target energy
- optionally rewarding valence and tempo closeness when those preferences are present
- adding a small acoustic bonus when the user prefers acoustic or non-acoustic songs

The system chooses recommendations by scoring every song and sorting them from highest score to lowest. The top `k` songs are returned as the final ranked list.

The scoring rule is for one song; the ranking rule is for comparing all songs and selecting the best ones.

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
Loaded songs: 17

Top recommendations:
Sunrise City - Score: 4.42
Because: genre match (+2.0); mood match (+1.0); energy closeness (+1.36); valence closeness (+0.12)

Rooftop Lights - Score: 3.58
Because: mood match (+1.0); energy closeness (+1.48); valence closeness (+0.37); tempo closeness (+0.73)

Gym Hero - Score: 3.46
Because: genre match (+2.0); energy closeness (+1.14); valence closeness (+0.08); tempo closeness (+0.23)

Night Drive Loop - Score: 2.79
Because: energy closeness (+1.24); valence closeness (+0.50); tempo closeness (+0.61)

Midnight Beat - Score: 2.60
Because: energy closeness (+1.24); valence closeness (+0.25); tempo closeness (+1.11)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this




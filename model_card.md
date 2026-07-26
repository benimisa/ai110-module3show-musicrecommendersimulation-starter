# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender is designed to suggest songs from a small catalog based on a user's preferred genre, mood, energy, and acoustic preference. It is for classroom exploration and not for real production use.

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

This model uses song metadata like genre, mood, energy, tempo, valence, and acousticness to compute a score for each track. It gives the biggest boost to exact genre matches, a smaller boost to mood matches, and then adds fractional points for songs whose energy and emotional tone are close to the user profile. When the user chooses acoustic preference, the system also favors songs that match that acousticness level.

This is a content-based recommender because it compares the attributes of each song to the user's taste rather than looking at what other listeners preferred.

---

## 4. Data  

The catalog contains 17 songs across genres like pop, lofi, rock, ambient, jazz, synthwave, indie pop, folk, edm, classical, reggae, blues, hip-hop, and ambient dream pop. Moods include happy, chill, intense, relaxed, moody, focused, dreamy, calm, relaxed, sad, and confident.

I added 7 new songs to the starter dataset to increase genre and mood variety. The dataset is still small and does not include lyrics, artist popularity, skip history, or user listening sessions.

---

## 5. Strengths  

The system works well for users who have clear genre and mood preferences. It can distinguish between high-energy and low-energy tracks and tends to recommend songs that feel close to the target energy.

For profiles like happy pop listeners, it correctly raises pop songs and energy-aligned tracks to the top.

---

## 6. Limitations and Bias  

The model can over-prioritize genre because exact genre matches are worth more points than mood or energy closeness. If a user's favorite genre is common in the dataset, recommendation results can become narrow.

It also ignores temporal behavior like likes, skips, playlists, and trends, and it does not learn from other users' behavior. This content-based approach may miss good songs in underrepresented genres or moods.

---

## 7. Evaluation  

I tested the recommender with different user profiles such as a pop/happy listener, a chill acoustic listener, and a high-energy workout listener. I looked for whether the top songs matched the intended vibe and whether energy closeness mattered.

I also checked cases where the same song should not win for very different tastes. The model behaves sensibly when genre and mood align but can be too genre-focused if the catalog is small.

---

## 8. Future Work  

- Add more user behavior features such as likes, skips, and playlist history
- Introduce a collaborative filtering layer to compare users instead of only song attributes
- Add richer audio features like rhythm, instrumentation, and lyrical sentiment
- Improve diversity by penalizing repeated genres in the top results

---

## 9. Personal Reflection  

I learned that simple rules can still produce useful song recommendations if the features are chosen carefully. Using AI to help shape the scoring logic was helpful, but I had to check the numeric weights and exact matching ideas myself.

It was surprising how much extra control a small content-based system gives: once I decided which features matter most, I could predict why a song would rise or fall in the ranked list.

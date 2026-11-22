# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

This recommender uses a content-based approach: it compares each song’s features with a simple user taste profile.

**User profile**
- Preferred genre: Hip-Hop
- Preferred mood: Energetic
- Target energy: 0.8

**Song features**
- Title and artist
- Genre
- Mood
- Energy level
- Tempo (BPM)

**Scoring**

Each song receives a weighted score using:

`Final Score = (0.40 × Genre Match) + (0.30 × Mood Match) + (0.30 × Energy Similarity)`

Genre and mood match receive a score of 1 when they match the profile and 0 when they do not. Energy similarity compares the song’s energy with the target of 0.8, calculated as `1 - |song_energy - 0.8|`. The highest possible final score is 1.0.

The recommender calculates this score for every song, sorts the songs from highest to lowest score, and returns the top 5 recommendations.

**Potential biases and limitations**

The small, predefined catalog may not represent every genre, artist, or mood. Matching only Hip-Hop and Energetic music can over-recommend familiar styles and narrow the user’s choices. The energy score is a simple numeric comparison, so it may miss useful details about rhythm or lyrics. Because the system is based on fixed preferences rather than listening history, it cannot learn from feedback or recognize changing tastes.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

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

```text
High-Energy Pop — Top 5 Recommendations
=======================================

1. Sunrise City
   Artist: Neon Echo
   Score: 0.98
   Reasons:
   - Genre matches your preference: pop
   - Mood matches your preference: happy
   - Energy similarity is 0.92 (song: 0.82, target: 0.90)

2. Gym Hero
   Artist: Max Pulse
   Score: 0.69
   Reasons:
   - Genre matches your preference: pop
   - Mood 'intense' differs from your preference 'happy'
   - Energy similarity is 0.97 (song: 0.93, target: 0.90)

3. Rooftop Lights
   Artist: Indigo Parade
   Score: 0.56
   Reasons:
   - Genre 'indie pop' differs from your preference 'pop'
   - Mood matches your preference: happy
   - Energy similarity is 0.86 (song: 0.76, target: 0.90)

4. Storm Runner
   Artist: Voltline
   Score: 0.30
   Reasons:
   - Genre 'rock' differs from your preference 'pop'
   - Mood 'intense' differs from your preference 'happy'
   - Energy similarity is 0.99 (song: 0.91, target: 0.90)

5. Backbeat Revolution
   Artist: Copper District
   Score: 0.29
   Reasons:
   - Genre 'funk' differs from your preference 'pop'
   - Mood 'energetic' differs from your preference 'happy'
   - Energy similarity is 0.98 (song: 0.88, target: 0.90)
```

```text
Chill Lofi — Top 5 Recommendations
==================================

1. Library Rain
   Artist: Paper Lanterns
   Score: 0.95
   Reasons:
   - Genre matches your preference: lofi
   - Mood matches your preference: chill
   - Energy similarity is 0.85 (song: 0.35, target: 0.20)

2. Midnight Coding
   Artist: LoRoom
   Score: 0.93
   Reasons:
   - Genre matches your preference: lofi
   - Mood matches your preference: chill
   - Energy similarity is 0.78 (song: 0.42, target: 0.20)

3. Focus Flow
   Artist: LoRoom
   Score: 0.64
   Reasons:
   - Genre matches your preference: lofi
   - Mood 'focused' differs from your preference 'chill'
   - Energy similarity is 0.80 (song: 0.40, target: 0.20)

4. Spacewalk Thoughts
   Artist: Orbit Bloom
   Score: 0.58
   Reasons:
   - Genre 'ambient' differs from your preference 'lofi'
   - Mood matches your preference: chill
   - Energy similarity is 0.92 (song: 0.28, target: 0.20)

5. Velvet Rain
   Artist: Sable Choir
   Score: 0.29
   Reasons:
   - Genre 'classical' differs from your preference 'lofi'
   - Mood 'melancholic' differs from your preference 'chill'
   - Energy similarity is 0.98 (song: 0.22, target: 0.20)
```

```text
Intense Rock — Top 5 Recommendations
====================================

1. Storm Runner
   Artist: Voltline
   Score: 0.99
   Reasons:
   - Genre matches your preference: rock
   - Mood matches your preference: intense
   - Energy similarity is 0.96 (song: 0.91, target: 0.95)

2. Gym Hero
   Artist: Max Pulse
   Score: 0.59
   Reasons:
   - Genre 'pop' differs from your preference 'rock'
   - Mood matches your preference: intense
   - Energy similarity is 0.98 (song: 0.93, target: 0.95)

3. Ember Skies
   Artist: Ironwood
   Score: 0.59
   Reasons:
   - Genre 'metal' differs from your preference 'rock'
   - Mood matches your preference: intense
   - Energy similarity is 0.98 (song: 0.97, target: 0.95)

4. Backbeat Revolution
   Artist: Copper District
   Score: 0.28
   Reasons:
   - Genre 'funk' differs from your preference 'rock'
   - Mood 'energetic' differs from your preference 'intense'
   - Energy similarity is 0.93 (song: 0.88, target: 0.95)

5. Sunrise City
   Artist: Neon Echo
   Score: 0.26
   Reasons:
   - Genre 'pop' differs from your preference 'rock'
   - Mood 'happy' differs from your preference 'intense'
   - Energy similarity is 0.87 (song: 0.82, target: 0.95)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I tested my recommender using three user profiles: High-Energy Pop, Chill Lofi, and Intense Rock. I also changed the scoring weights from 40% genre, 30% mood, and 30% energy to 20% genre, 20% mood, and 60% energy. This caused songs with similar energy levels to rank higher, even when their genres or moods did not match. I found that the original weights provided more balanced recommendations.

## Limitations and Risks

My recommender uses a small dataset and only considers genre, mood, and energy. It does not account for listening history, lyrics, or other musical features. It may also favor genres and moods that appear more frequently in the dataset, making recommendations less accurate for some users.

## Reflection

This project helped me understand how recommendation systems use data and scoring algorithms to predict what users might enjoy. I learned that even simple algorithms can create personalized results, but the quality depends on the features and weights used. AI tools helped me develop and test the system more efficiently, but I still needed to review the results and make decisions about the scoring approach.

I also learned how bias can appear in recommendation systems when certain genres or moods are represented more than others. This can cause some users to receive better recommendations than others. If I continued developing this project, I would expand the dataset and include more features to make the recommendations more accurate and diverse.




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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

Top 5 Recommendations
========================

1. Sunrise City
   Artist: Neon Echo
   Score: 0.99
   Reasons:
   - Genre matches your preference: pop
   - Mood matches your preference: happy
   - Energy similarity is 0.98 (song: 0.82, target: 0.80)

2. Gym Hero
   Artist: Max Pulse
   Score: 0.66
   Reasons:
   - Genre matches your preference: pop
   - Mood 'intense' differs from your preference 'happy'
   - Energy similarity is 0.87 (song: 0.93, target: 0.80)

3. Rooftop Lights
   Artist: Indigo Parade
   Score: 0.59
   Reasons:
   - Genre 'indie pop' differs from your preference 'pop'
   - Mood matches your preference: happy
   - Energy similarity is 0.96 (song: 0.76, target: 0.80)

4. Night Drive Loop
   Artist: Neon Echo
   Score: 0.28
   Reasons:
   - Genre 'synthwave' differs from your preference 'pop'
   - Mood 'moody' differs from your preference 'happy'
   - Energy similarity is 0.95 (song: 0.75, target: 0.80)

5. Backbeat Revolution
   Artist: Copper District
   Score: 0.28
   Reasons:
   - Genre 'funk' differs from your preference 'pop'
   - Mood 'energetic' differs from your preference 'happy'
   - Energy similarity is 0.92 (song: 0.88, target: 0.80)

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




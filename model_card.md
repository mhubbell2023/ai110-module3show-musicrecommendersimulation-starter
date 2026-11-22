# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: FindaTune  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

My music recommender is designed to suggest songs based on a user's preferred genre, mood, and energy level. It assumes users have specific musical preferences that can be used to find similar songs. This system is a simple classroom simulation designed to explore how recommendation algorithms work rather than a platform for real users.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

My music recommender scores songs by comparing their genre, mood, and energy level to the user's preferences. Genre matches account for 40% of the score, mood matches account for 30%, and energy similarity makes up the remaining 30%. Songs receive higher scores when their features closely match what the user enjoys. I improved the starter logic by adding weighted scoring, calculating how close a song's energy is to the user's target, and providing reasons explaining each recommendation. The system then ranks the songs by their scores and recommends the top five.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

My music recommender uses a CSV dataset that originally contained 10 songs, which I expanded by adding songs from different genres and moods. The catalog includes genres such as pop, rock, lofi, hip-hop, metal, and classical, with moods ranging from happy and energetic to chill and intense. I added songs to increase the variety of recommendations and better represent different musical preferences. However, the dataset is still relatively small and does not capture every genre, mood, or aspect of musical taste, which limits the variety of recommendations.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

My recommender works well for users with clear genre, mood, and energy preferences. It correctly ranks songs higher when they closely match what the user likes. The High-Energy Pop, Chill Lofi, and Intense Rock profiles all received recommendations that made sense. Overall, the system does a good job of identifying songs with similar musical features.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

My music recommender has several limitations because it only considers genre, mood, and energy when ranking songs. It does not account for other important features such as tempo or a user's listening history. The system may also favor genres and moods that are more heavily represented in the dataset, making it harder for users with less common preferences to receive accurate recommendations. During my experiment, I found that increasing the energy weight caused songs with unrelated genres and moods to receive higher scores simply because their energy levels were similar. Additionally, the system treats related genres, such as pop and indie pop, as completely different categories, which can limit recommendation variety and favor users whose preferences exactly match the dataset's labels.


---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

## Evaluation

I evaluated my music recommender using three different user profiles: High-Energy Pop, Chill Lofi, and Intense Rock. I examined the top five recommendations for each profile to determine whether the songs matched the user's preferred genre, mood, and energy level. Overall, the recommendations made sense, but I noticed that some songs ranked highly despite having different genres or moods. I also experimented with increasing the energy weight from 30% to 60%, which caused songs with similar energy levels to rank higher even when their other attributes did not match. This showed me that changing the weights can significantly affect the results without necessarily improving recommendation quality.

### Profile Comparisons

**High-Energy Pop vs. Chill Lofi:** High-Energy Pop recommended upbeat songs like Sunrise City, while Chill Lofi favored calmer songs like Library Rain. This makes sense because the profiles have different genre, mood, and energy preferences.

**High-Energy Pop vs. Intense Rock:** Both profiles preferred high-energy music, but their top recommendations were different. Sunrise City ranked first for Pop, while Storm Runner ranked first for Rock. Interestingly, Gym Hero appeared near the top of both lists because its high energy and matching attributes made it suitable for both profiles, despite not matching every preference.

**Chill Lofi vs. Intense Rock:** These profiles produced very different recommendations because their energy targets were almost opposite. Chill Lofi favored low-energy songs like Midnight Coding, while Intense Rock preferred high-energy songs like Storm Runner and Ember Skies.

### Key Finding

One surprising result was that Gym Hero ranked second for the High-Energy Pop profile even though its mood was intense rather than happy. This happened because the song matched the preferred pop genre and had an energy level very close to the user's target. The experiment demonstrated that my recommender follows its scoring rules consistently, but those rules do not always perfectly represent a person's musical taste.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

In the future, I would improve my recommender by adding more song features like tempo, artist, and listening history. I would also expand the dataset to include more genres and moods. Another improvement would be making the recommendations more diverse and providing clearer explanations for why each song was selected. This would help the system better understand users with more complex musical preferences.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps 

My biggest learning moment was seeing how changing the scoring weights affected the recommendations. AI tools helped me write code, debug errors, and improve my algorithm, but I still needed to test the results to make sure they made sense. I was surprised that a simple scoring system could produce recommendations that felt personalized. If I continued this project, I would add more song features, expand the dataset, and use listening history to improve the results.

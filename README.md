
# Twitter Data Analysis: Users, Media, and Places

This project explores a structured dataset of **tweets**, **users**, **media**, and **places**, with the goal of uncovering insights from tweet content, user behavior, and geographical trends.

---

## Dataset Summary

The dataset includes:
- Tweet content and metadata
- User details (e.g., ID, screen name, location)
- Media information (image/video links)
- Geographic place data (e.g., city, country)

Data file: `tw_tweets_users_media_places-Kwasi_Boateng.csv`

---

## Project Goals

- Clean and preprocess tweet text (removing links, emojis, etc.)
- Perform sentiment and emotion analysis
- Analyze tweet activity over time and by location
- Explore user trends (e.g., top tweeters, most active cities)
- Visualize word frequencies, hashtags, and sentiments

---

## Project Structure

```bash
twitter-insights/
├── data/           # Raw and processed data
├── notebooks/      # EDA and NLP experiments in Jupyter
├── src/            # Modular Python code for data processing
├── outputs/        # Final visualizations and analysis results
├── requirements.txt
└── README.md
```

---

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/twitter-insights.git
cd twitter-insights
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

Required libraries include:

```text
pandas
numpy
matplotlib
seaborn
wordcloud
nltk
textblob
scikit-learn
```

3. **Launch the main notebook**

Start with: `notebooks/Checkpoint_MLR.ipynb`

---

## Key Visualizations

- Tweet frequency over time
- Word clouds by sentiment
- Tweet count by country
- Top users and hashtags

---

## Example Use Cases

- Which cities or countries are most active?
- What’s the general sentiment in tweets?
- Which users post the most media?
- What topics or hashtags are trending?

---

## Potential Extensions

- Topic modeling (e.g., LDA)
- Named Entity Recognition (NER)
- Bot detection or user profiling
- Network graph of users or mentions

---

## License

Distributed under the MIT License. See `LICENSE` for more info.

---

## Author

**Kwame Boateng**  
*Data Analyst | NLP Enthusiast*

---

## Contributing

If you have suggestions, improvements, or new features to propose, feel free to open an issue or submit a pull request.

# Project Overview: Support Agent Chatbot for CDP

## Objective
```
A chatbot that can answer "how-to" questions related to four Customer Data
Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot should be able
to extract relevant information from the official documentation of these CDPs to guide
users on how to perform tasks or achieve specific outcomes within each platform.
```

## Project Folder Structure
```
Support-Agent-Chatbot/
│── data/
│   │── segment_docs.json
│   │── mparticle_docs.json
│   │── lytics_docs.json
│   │── zeotap_docs.json
│── models/
│   │── retrieval_model.py
│── backend/
│   │── app.py
│   │── query_processor.py
│   │── scraper.py
│── frontend/
│   │── index.html
│   │── script.js
│   │── styles.css
│── README.md
```

## Features Implemented
1. **Answer 'How-to' Questions** – Provides guidance for Segment, mParticle, Lytics, and Zeotap.
2. **Extracts Information from Documentation** – Uses web scraping and retrieval-based query processing.
3. **Handles Variations in Questions** – Supports different query lengths and detects irrelevant questions.
4. **Cross-CDP Comparisons** – Compares features across multiple CDPs.
5. **Advanced 'How-to' Questions** – Supports complex queries related to advanced configurations and integrations.

## Testing Steps
### Running the Backend:
```sh
python app.py
```
### Opening the Frontend:
- Open `index.html` in a browser.
- Enter questions in the chatbox and check responses.

### Test Cases
#### 1. Basic 'How-to' Questions
✅ "How do I create an audience segment in Lytics?"
✅ "How can I integrate my data with Zeotap?"

#### 2. Cross-CDP Comparisons
✅ "How does Segment's audience creation process compare to Lytics'?"
✅ "What are the key differences between mParticle and Zeotap?"

#### 3. Advanced 'How-to' Questions
✅ "How do I configure mParticle for advanced event tracking?"
✅ "What is the best way to send real-time data in Segment?"

#### 4. Irrelevant Query Handling
❌ "Which movie is getting released this week?" → Should return: "I'm here to help with CDP-related queries only."

#### 5. Long Query Test
✅ "I need to set up a new source in Segment and also ensure that data flows correctly into mParticle and Zeotap while maintaining user privacy. How should I do this?"

---
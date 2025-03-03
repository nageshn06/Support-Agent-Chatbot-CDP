# Project Overview: Support Agent Chatbot for CDP

## Objective

A chatbot that can answer "how-to" questions related to four Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot should be ableto extract relevant information from the official documentation of these CDPs to guideusers on how to perform tasks or achieve specific outcomes within each platform.

## Features
### Core Functionalities:
1. **Answer 'How-to' Questions:**
   - Understands user queries related to Segment, mParticle, Lytics, and Zeotap.
   - Extracts information from official documentation to provide step-by-step guidance.

2. **Extract Information from Documentation:**
   - Navigates through documentation to retrieve relevant sections.
   - Uses scraping and indexing techniques to improve search efficiency.

3. **Handle Variations in Questions:**
   - Ensures long queries do not break processing.
   - Filters out irrelevant questions (e.g., asking about movies).

### Bonus Features:
4. **Cross-CDP Comparisons:**
   - Answers questions comparing functionalities of different CDPs.
   - Example: "How does Segment's audience creation process compare to Lytics'?"

5. **Advanced 'How-to' Questions:**
   - Supports complex queries related to advanced configurations and integrations.

## Improvements & Fixes:
### **New Enhancements:**
✅ **Better Query Processing** – Improved NLP to fetch more accurate responses.
✅ **Response Ranking** – Prioritizes the most relevant answer when multiple matches are found.
✅ **Handle Edge Cases** – Enhanced response handling for long and irrelevant queries.
✅ **Improved UI/UX** – Added loading indicators and refined chatbot response formatting.
✅ **Logging & Debugging** – Added logs to track queries and errors for performance analysis.

### **Fixes:**
🔹 **Query Variations Handling** – Ensured consistent answers for similar questions.
🔹 **Cross-CDP Comparisons** – Enhanced responses with clearer comparisons.
🔹 **Optimized Scraper & Query Processor** – Reduced response time by implementing caching for frequent queries.


## Project Structure:
```
SupportAgentChatbot/
│── data/
│   │── segment_docs.json
│   │── mparticle_docs.json
│   │── lytics_docs.json
│   │── zeotap_docs.json
│── models/
│   │── retrieval_model.py
│── app.py (Main chatbot application)
│── scraper.py (Extracts data from CDP documentation)
│── query_processor.py (Processes user queries)
│── ui/
│   │── index.html (Chatbot UI)
│   │── style.css (Chatbot Styling)
│   │── script.js (Frontend logic)
│── README.md (This file)
```

## Running the Chatbot
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the chatbot backend:
   ```sh
   python app.py
   ```
3. Open `index.html` in a browser to interact with the chatbot.

## Testing
- Try different 'how-to' queries.
- Ask cross-CDP comparison questions.
- Test handling of irrelevant queries.
  
This chatbot is designed to provide fast and accurate responses, improving user experience with CDPs.

## Features Implemented
1. **Answer 'How-to' Questions** – Provides guidance for Segment, mParticle, Lytics, and Zeotap.
2. **Extracts Information from Documentation** – Uses web scraping and retrieval-based query processing.
3. **Handles Variations in Questions** – Supports different query lengths and detects irrelevant questions.
4. **Cross-CDP Comparisons** – Compares features across multiple CDPs.
5. **Advanced 'How-to' Questions** – Supports complex queries related to advanced configurations and integrations.

## Improvements & Fixes
### **Backend (Flask)**
1. **Error Handling for Missing Data**
   ```python
   try:
       with open(f"data/{platform}_docs.json", "r") as f:
           docs.update(json.load(f))
   except FileNotFoundError:
       return f"Error: Documentation for {platform} is missing. Please re-run the scraper."
   ```
2. **Handle Empty or Irrelevant Queries More Intelligently**
   ```python
   if not query.strip():
       return "Please enter a valid question about CDPs."
   ```
3. **Make Flask Production-Ready**
   - Replace `app.run(debug=True)` with `gunicorn` or `waitress` for deployment.

### **Web Scraper**
1. **Handle Scraping Failures & Rate Limiting**
   ```python
   response = requests.get(url)
   if response.status_code != 200:
       print(f"Error scraping {platform}: {response.status_code}")
       continue
   ```

### **Query Processor**
1. **Enhance Text Retrieval for Better Responses**
   ```python
   from sentence_transformers import SentenceTransformer, util
   model = SentenceTransformer('all-MiniLM-L6-v2')
   ```

### **Frontend**
1. **Improve Chat UI for User Experience**
   ```css
   .user-message {
       background: #007bff;
       color: white;
       padding: 8px;
       border-radius: 5px;
   }

   .bot-message {
       background: #28a745;
       color: white;
       padding: 8px;
       border-radius: 5px;
   }
   ```
2. **Handle API Request Failures**
   ```js
   fetch("http://127.0.0.1:5000/ask", { ... })
   .then(response => response.json())
   .catch(error => {
       document.getElementById("chat-box").innerHTML += `<p class='bot-message'>Error: Could not reach the server.</p>`;
   });
   ```

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


## Contributors

- [Nagesh N]

##
---

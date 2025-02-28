# chatbot

# CDP Support Agent Chatbot

This project is a chatbot designed to answer "how-to" questions about four Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. Developed as part of Assignment 2, it extracts relevant information from official CDP documentation to guide users on performing tasks or achieving specific outcomes within these platforms.

## Objective

The goal is to create a support agent chatbot that understands and responds to user queries about CDP functionalities, leveraging official documentation as its knowledge base, while handling variations in question phrasing and providing a seamless user experience.

## Core Functionalities

### 1. Answer "How-to" Questions
- Responds to queries like:
  - "How do I set up a new source in Segment?"
  - "How can I create a user profile in mParticle?"
  - "How do I build an audience segment in Lytics?"
  - "How can I integrate my data with Zeotap?"
- Provides step-by-step guidance based on documentation.

### 2. Extract Information from Documentation
- Sources:
  - [Segment Documentation](https://segment.com/docs/?ref=nav)
  - [mParticle Documentation](https://docs.mparticle.com/)
  - [Lytics Documentation](https://docs.lytics.com/)
  - [Zeotap Documentation](https://docs.zeotap.com/home/en-us/)
- Indexes and retrieves relevant sections to formulate answers.

### 3. Handle Variations in Questions
- Supports long or complex questions without breaking (e.g., "How do I configure a Segment source with multiple destinations and track events?").
- Gracefully handles irrelevant queries (e.g., "Which movie is getting released this week?") with a fallback response like "I can only assist with CDP-related questions."

### Bonus Features (Optional)
- Cross-CDP Comparisons: Answers questions like "How does Segment’s audience creation process compare to Lytics’?"
- Advanced "How-to" Questions: Handles complex scenarios (e.g., "How do I set up a custom integration in Zeotap?").

## Tech Stack

- Backend: 
  - Python: Core language for logic and document processing.
  - Django: Web framework for hosting the chatbot as a web app.
- Document Processing: 
  - BeautifulSoup/Requests: Scrapes and parses HTML documentation from CDP websites.
  - Simple Indexer: Custom keyword-based indexer for fast retrieval (instead of NLP).
- Frontend: 
  - HTML/CSS/JavaScript for a basic chat interface.
- Libraries: 
  - re (Python regex): For parsing question patterns and documentation text.
- Version Control: Git with GitHub for repository management.

### Why This Stack?
- Python: Versatile for text processing and rapid prototyping.
- Simple Indexer: Lightweight alternative to NLP, focusing on software engineering per assignment notes.
- Django/Flask: Provides a scalable web app structure if implemented (optional per assignment flexibility).

## Data Structures

- Dictionary/Map: 
  - Stores an index of documentation sections (e.g., `{ "Segment source setup": "instructions..." }`) for quick lookups.
  - Chosen for O(1) retrieval speed.
- List/Array: 
  - Holds parsed documentation paragraphs or steps for each CDP topic.
  - Used for sequential processing and response generation.
- Set: 
  - Tracks unique keywords or question patterns to avoid duplicates in indexing.
  - Efficient for membership checks.

### Why These Structures?
- Dictionary: Perfect for mapping questions to answers, optimizing response time.
- List: Simple and effective for storing ordered steps or text chunks.
- Set: Ensures efficient keyword management without redundancy.

## Installation and Setup

1. Clone the Repository:
   ```bash
   git clone https://github.com/GollaVamshi/cdp-chatbot.git
   cd cdp-chatbot

   Install Dependencies:

   pip install django beautifulsoup4

Usage
CLI Mode: Type a question (e.g., "How do I set up a new source in Segment?") and press Enter.
Web Mode (if implemented): Enter your question in the chat interface and submit.

Evaluation Highlights
Accuracy: Responses are sourced directly from official documentation, ensuring correctness.
Code Quality: Modular design with clear separation of indexing, query processing, and response generation.
Question Variations: Handles long and irrelevant questions robustly.
User Experience: Simple, intuitive interface (CLI or web-based).
Bonus Features: [Include if implemented, e.g., "Cross-CDP comparisons added."]

Future Improvements
Integrate NLP (e.g., spaCy) for better question understanding.
Cache documentation locally to reduce web scraping latency.
Add a GUI with real-time chat features using WebSockets.
License
This project is unlicensed and intended for educational purposes only
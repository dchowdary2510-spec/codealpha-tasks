# AI-Powered FAQ Chatbot

An intelligent FAQ Chatbot built using Python, Streamlit, and Google's Gemini 2.5 Flash model. The chatbot answers user questions using a predefined FAQ database and AI-powered response generation for better accuracy and user experience.

## Features

- AI-powered responses using Gemini 2.5 Flash
- Interactive chat interface
- FAQ knowledge base support
- Fast and user-friendly Streamlit UI
- Intelligent response generation
- Easy to customize and expand

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- JSON
- python-dotenv

## Project Structure

FAQ_Chatbot/
│
├── app.py
├── faq.json
├── requirements.txt
├── .gitignore
└── README.md

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd FAQ_Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a .env File

Create a file named `.env` in the project directory and add:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

## How It Works

1. User enters a question.
2. The chatbot checks the FAQ database.
3. Gemini 2.5 Flash processes the query and generates an intelligent response.
4. The answer is displayed in the Streamlit interface.

## Sample Use Cases

- College FAQs
- Customer Support FAQs
- Product Information
- Educational Assistance
- General Question Answering

## Security

API keys are stored securely using environment variables and are excluded from version control through `.gitignore`.

## Future Enhancements

- Voice input support
- Multi-language responses
- Conversation history
- User authentication
- Database integration

## Author

Developed as part of the CodeAlpha Internship Program.
# 🔍 AI-Powered Research Assistant

An AI-powered intelligent research assistant built with **Python**, **LangChain**, and **OpenAI GPT models**.  
This project leverages **FAISS** for efficient document search and retrieval, enabling fast and accurate research insights from large text data.

---

## ✨ Features
- **AI-Powered Question Answering**: Ask natural language questions and get context-aware answers.
- **Document Search**: Quickly retrieve relevant information using FAISS vector embeddings.
- **OpenAI GPT Integration**: Advanced language understanding and summarization.
- **Secure Key Management**: API keys are stored securely using `.env`.

---

## 🛠 Tech Stack
- **Python 3.10+**
- [LangChain](https://www.langchain.com/) – LLM orchestration
- [OpenAI](https://platform.openai.com/) – LLM API
- [FAISS](https://faiss.ai/) – Vector search
- **dotenv** – Environment variable management

---

## 📂 Project Structure
# 📂 Project Structure
Equivista/
├── main.py # Entry point of the application
├── loader.ipynb # Document loading and preprocessing notebook
├── long-doc (1).txt # Sample document
├── faiss_store_openai/ # Vector database files
├── requirements.txt # Python dependencies
├── .env.example # Example environment variables
├── icon.png # Project logo/icon
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Aksha18/AI-Powered-Research-Assistant.git
cd AI-Powered-Research-Assistant
2. Create & activate virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # Mac/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file in the project root:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
(Make sure .env is included in .gitignore to protect your keys.)

An .env.example file is provided as a reference.

▶️ Usage
Run the main script:

bash
Copy
Edit
python main.py
Upload documents or use existing ones.

Ask questions and receive AI-generated, context-aware answers.

🧑‍💻 Contributing
Fork the repository

Create your feature branch (git checkout -b feature-name)

Commit changes (git commit -m 'Add new feature')

Push to branch (git push origin feature-name)

Create a Pull Request

📜 License
This project is licensed under the MIT License.

📷 Screenshots (Optional)
(Add screenshots or GIFs showing your app in action)

⭐ Show Your Support
If you like this project, give it a star ⭐ on GitHub and share it with others!

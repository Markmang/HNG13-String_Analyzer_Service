# HNG13-String_Analyzer_Service
 A RESTful Django API service that analyzes strings and computes properties such as their length, palindrome status, word count, SHA-256 hash, unique characters, and frequency map.

This project was built as part of the *HNG13 Backend Stage 1 Task*.

---

## 🚀 Features

For every analyzed string, this API computes and stores:

- length: Number of characters in the string  
- is_palindrome: Boolean showing if it reads the same forwards and backwards  
- unique_characters: Count of distinct characters  
- word_count: Number of words separated by whitespace  
- sha256_hash: Unique hash identifier for the string  
- character_frequency_map: A dictionary showing how many times each character appears  

---

## 🧩 Tech Stack

- *Python 3.10*
- *Django 5.2.6*
- *Django REST Framework*
- *dj-database-url*
- *Whitenoise*
- *Gunicorn*
- *SQLite3* (default local database)

---

## ⚙ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Markmang/HNG13-String_Analyzer_Service.git
cd HNG13-String_Analyzer_Service

2️⃣ Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run database migrations

python manage.py migrate

5️⃣ Create a superuser (optional for Django admin)

python manage.py createsuperuser

6️⃣ Run the development server

python manage.py runserver

Your app will now be available at:
👉 http://127.0.0.1:8000/


---

🌍 Deployed Version

Live API:
🔗 https://mangi.pythonanywhere.com/api/strings/


---

🔑 Environment Variables

Create a .env file in your project root with the following:

SECRET_KEY=your-secret-key
DEBUG=True
ENVIRONMENT=development
DATABASE_URL=sqlite:///db.sqlite3

When deploying to production (e.g. PythonAnywhere):

DEBUG=False
ENVIRONMENT=production
SECRET_KEY=your-strong-secret-key
DATABASE_URL=sqlite:///db.sqlite3


---

🧰 Dependencies

Main dependencies used in this project:

Django==5.2.6
djangorestframework==3.16.1
dj-database-url==3.0.1
python-dotenv==1.1.1
whitenoise==6.11.0
gunicorn==23.0.0


---

🧪 Testing the API

You can test using cURL, Postman, or directly via the DRF UI.

▶ POST /api/strings/

Analyze and store a string.

Request Body:

{
  "value": "love is good"
}

Response:

{
  "id": "21b5062cfef73913d42baeb492aef329fa11c40a465aaf9ec7613ff329e036a",
  "value": "love is good",
  "properties": {
    "length": 12,
    "is_palindrome": false,
    "unique_characters": 9,
    "word_count": 3,
    "sha256_hash": "21b5062cfef73913d42baeb492aef329fa11c40a465aaf9ec7613ff329e036a",
    "character_frequency_map": {
      "l": 1,
      "o": 3,
      "v": 1,
      "e": 1,
      " ": 2,
      "i": 1,
      "s": 1,
      "g": 1,
      "d": 1
    }
  },
  "created_at": "2025-10-20T18:00:00Z"
}


---

🔍 GET /api/strings/

List all analyzed strings, with optional filters.

Query Parameters:

is_palindrome=true
min_length=5
max_length=20
word_count=2
contains_character=a

Example:

GET /api/strings/?is_palindrome=true&word_count=1


---

🔎 GET /api/strings/{string_value}

Retrieve one analyzed string.

Example:

GET /api/strings/racecar


---

💬 GET /api/strings/filter-by-natural-language

Natural language filtering.

Example:

GET /api/strings/filter-by-natural-language?query=all single word palindromic strings

Response:

{
  "data": [...],
  "count": 3,
  "interpreted_query": {
    "original": "all single word palindromic strings",
    "parsed_filters": {
      "word_count": 1,
      "is_palindrome": true
    }
  }
}


---

❌ DELETE /api/strings/{string_value}

Delete a previously analyzed string.

Example:

DELETE /api/strings/racecar

Response:

204 No Content


---

🧾 API Summary

Method	Endpoint	Description

POST	/api/strings/	Analyze and store a string
GET	/api/strings/	Retrieve all analyzed strings with optional filters
GET	/api/strings/{string_value}	Retrieve details of a specific string
DELETE	/api/strings/{string_value}	Delete an analyzed string
GET	/api/strings/filter-by-natural-language	Filter using human-readable queries



---

🧠 Notes

Palindrome detection is case-insensitive.

The sha256_hash field ensures each string is uniquely identifiable.

Duplicate strings will trigger a 409 Conflict response.

The API is RESTful, stateless, and uses DRF’s class-based views for clean separation.



---

🧑‍💻 Author

Udeagha Mark Mang
Software Engineer | Product Manager
💼 GitHub
🌐 Portfolio
✉ markudeaghamang@gmail.com

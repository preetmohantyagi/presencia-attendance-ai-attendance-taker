# Presencia — AI-Powered Classroom Attendance

Presencia is a Streamlit web app that lets teachers take classroom attendance automatically using **face recognition** or **voice verification**, instead of manual roll calls. Teachers manage subjects and classes, students join via a QR code / join link, and attendance is recorded in real time.

🔗 **Repo:** [presencia-attendance-ai-attendance-taker](https://github.com/preetmohantyagi/presencia-attendance-ai-attendance-taker)

---

## ✨ Features

- **Face recognition attendance** — marks a student present by matching their face against enrolled face data
- **Voice verification attendance** — alternative attendance mode using speaker/voice recognition
- **Teacher portal** — create and manage subjects/classes, view attendance records
- **Student portal** — join a class and mark presence
- **QR-code / join-link enrollment** — students auto-enroll into a class by scanning a QR code or opening a join link (`?join-code=...`)
- **Real-time backend** — attendance, users, and class data synced through Supabase
- **Secure authentication** — passwords hashed with bcrypt

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| App / UI | [Streamlit](https://streamlit.io/) |
| Face Recognition | `face_recognition` (dlib-based), `dlib` |
| Voice Recognition | [Resemblyzer](https://github.com/resemble-ai/Resemblyzer), Librosa |
| Backend / Database | [Supabase](https://supabase.com/) |
| Auth | bcrypt (password hashing) |
| QR Codes | [Segno](https://github.com/heuer/segno) |
| Data handling | NumPy, Pandas, scikit-learn |
| Image handling | Pillow |

---

## 📂 Project Structure

```
presencia-attendance-ai-attendance-taker/
├── app.py                        # App entry point — routes between screens
├── requirements.txt               # Python dependencies
├── .streamlit/                    # Streamlit config / secrets
└── src/
    ├── screens/
    │   ├── home_screen.py         # Landing page (choose teacher/student login)
    │   ├── teacher_screen.py      # Teacher dashboard — manage subjects & records
    │   └── student_screen.py      # Student dashboard — join & mark attendance
    └── components/
        └── dialog_auto_enroll.py  # Auto-enrollment dialog via join code
```

---

## ⚙️ How It Works

1. A student opens the app with a class **join link** (`?join-code=...`) shared by the teacher.
2. If logged in as a student, the **auto-enroll dialog** enrolls them into that class.
3. To mark attendance, the student verifies their identity via **face recognition** or **voice recognition**.
4. Verified attendance is written to **Supabase** in real time.
5. Teachers log into the **teacher screen** to view live attendance records and manage subjects/classes.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A [Supabase](https://supabase.com/) project (URL + API key)
- `dlib` build tools (CMake + a C++ compiler) — required by `face_recognition`

### Installation

```bash
# Clone the repo
git clone https://github.com/preetmohantyagi/presencia-attendance-ai-attendance-taker.git
cd presencia-attendance-ai-attendance-taker

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Add your Supabase credentials to `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-api-key"
```

> ⚠️ Never commit real credentials — keep `secrets.toml` in `.gitignore`.

### Run the app

```bash
streamlit run app.py
```

---

## 🗺️ Roadmap / Future Improvements

- [ ] Liveness detection to prevent photo/video spoofing of face recognition
- [ ] Attendance analytics dashboard (trends, defaulter list, exportable reports)
- [ ] Mobile-friendly camera capture flow
- [ ] Email/SMS notifications for low attendance

---

## 👤 Author

**Preet Mohan Tyagi**
[GitHub](https://github.com/preetmohantyagi) · preetmohan2006@gmail.com

---

## 📄 License

No license specified yet — add one (e.g. MIT) if you plan to open this up for contributions.

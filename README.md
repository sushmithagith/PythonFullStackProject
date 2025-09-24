# SILENT CLASSROOM MONITOR
 The Silent Classroom Monitor is a system that monitors noise levels in a classroom using a computer microphone. The system analyzes real-time audio data and determines whether the classroom is Quiet, Moderate, or Loud based on a predefined threshold.It provides visual feedback on a dashboard and stores the readings in a database for future analysis. This helps teachers maintain discipline and create a better learning environment.

 ## Features
Real-Time Noise Monitoring – Captures sound from the microphone continuously.
Noise Alerts – Shows warnings if the noise goes above a set limit.
Visual Dashboard – Uses colors to show status: Green = Quiet, Yellow = Moderate, Red = Loud.
Data Logging – Records noise levels, time, classroom, and teacher in a database.
Reports – Summarizes daily/weekly noise statistics for review.
Easy for Teachers – Helps maintain discipline and track classroom noise.

## Project Structure

Silent Classroom Monitor/
 |
 |---src/                   #core application logic
 |    |---logic.py          #Business Logic and Task Operations
 |    |---db.py             # Database Operations
 |---API/                   # Backend API
 |    |---main.py           #FastAPI endpoints
 |---Frontend/              #Frontend application
 |    |---app.py            #Steamlit WebInterface
 |
 |---requirements.txt       #python Dependencies
 |---readme.md              #Project Documentation
 |
 |---.env                   #python variables

 # Quick Start

 ## prerequisites
    - python 3.8 or higher
    - A supabase Account
    - Git(Push,clone)
### 1.clone or download the project
# option1: Clone with Git
git clone <repository-url>

# option2: Download and extract the ZIP File

### 2. Install Dependencies

# Install all required python packages
pip install -r requirements.txt

### 3.Set up supabase dependencies

1.create a supabase project

2.create the Tasks Table:

-Go to the SQL Editor in your supabase dashboard
-Run this SQL commands:

```sql

CREATE TABLE NoiseLogs (
    Id SERIAL PRIMARY KEY,
    timeStamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Classroom TEXT,
    Teacher TEXT,
    noise_level REAL NOT NULL,
    status TEXT NOT NULL
);



CREATE TABLE Reports (
    report_id SERIAL PRIMARY KEY,
    report_date DATE NOT NULL,
    Classroom TEXT,
    Teacher TEXT,
    avg_noise REAL,
    max_noise REAL,
    violations INTEGER
)

```

3. ** Get Your Credentials:

### 4. configure Environmental variables
  
  1. Create a `.env` file in the project root

  2. Add your supabase  credentials to `.env`:
     SUPABASE_URL=your_project_url_here
     SUPABASE_KEY=your_anon_key_here

 **Example**
   SUPABASE_URL= "https://qtypiqcdyuusiimsapqn.supabase.co"
   SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF0eXBpcWNkeXV1c2lpbXNhcHFuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI0MjIsImV4cCI6MjA3MzY1ODQyMn0.J01-uphB_hWM6u8NGtTpkdzNRt9jBxI238zqmvCMxSY"

### 5. Run the Application
 
   Streamlit run  Frontend/app.py
   The app will open in your browser at `http://localhost:8501`

   ## FastAPI Backend

   cd API
   python main.py

   The API will be available at `http://localhost:8000`

   ## How to Use

   ## Technical Details

   ## Technologies Used

   -**Frontend**:streamlit(python web framework)
   -**Backend**:FastAPI(python REST API framework)
   -**Database**:supabase(postgreSQL-based backend-as-a-service)
   -**Language**:python 3.8+

   ### key components

   1. **`src/db.py`**:Database operations 
     - Handles all CRUD operations with supabase

   2. **`src/logic.py`**:Business logic
     - Task validation and preprocessing

   3. **`API/main.py`**: Backend API
      -FastAPI endpoints to send and receive noise data between the frontend and database.

   4. **`Frontend/app.py`**: Frontend interface
      -Streamlit dashboard showing live noise levels, status indicators, logs, and reports.

   5. **`requirements.txt`**: Python dependencies
      -Lists all required packages for the project (Streamlit, FastAPI, Supabase, etc.).

   6. **`README.md:`** :Project documentation
      -Contains project overview, features, setup instructions, and usage.

   7. **`.env`**: Environment variables
        -Stores Supabase credentials, API keys, and configurable thresholds for the system 

### Common Errors
 
 1. **`ModuleNotFoundError`**:
    - Make sure you've installed all dependencies:`pip install -r requirements.txt`
    - check that you're running commands from the current directory

### Future Enhancements
 
 Ideas for extending this project:

 - **User Authentication** : Add user accounts and login
 - **Task Categories** : Organize tasks by subject or category
 - **Notifications** : Email or push notifications for due dates
 - **File Attachements** : Attach files to tasks 
 - **collaboration** : share tasks with classmates
 - **Mobile App** : React Native or Flutter mobile version
 - **Data Export** : Export tasks to CSV or PDF
 - **Task Templates**: Create resuable task templates

## support
If you encounter any issues or have questions:
 
 - contact no:7093413246
 - email:sushmithashanigaram3@gmail.com












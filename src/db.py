# db.py
import os
from supabase import create_client
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# ------------------
# NoiseLogs Table Operations
# ------------------

def create_log(Classroom, Teacher, noise_level=0, low_threshold=50, high_threshold=75, timeStamp=None):
    """
    Inserts a new noise reading into NoiseLogs.
    Status is automatically calculated based on thresholds.
    """
    if timeStamp is None:
        timeStamp = datetime.now()

    # Determine status
    if noise_level <= low_threshold:
        status = "low"
    elif noise_level <= high_threshold:
        status = "moderate"
    else:
        status = "high"

    return supabase.table("NoiseLogs").insert({
        "timeStamp": timeStamp,
        "Classroom": Classroom,
        "Teacher": Teacher,
        "noise_level": noise_level,
        "status": status
    }).execute()


def get_all_logs():
    return supabase.table("NoiseLogs").select("*").order("Classroom").execute()


def update_logs(Id, data: dict):
    return supabase.table("NoiseLogs").update(data).eq("Id", Id).execute()


def delete_logs(Id):
    return supabase.table("NoiseLogs").delete().eq("Id", Id).execute()


# ------------------
# Reports Table Operations
# ------------------

def create_report(report_date, Classroom, Teacher, noise_readings, high_threshold):
    """
    Inserts a new report into Reports.
    Calculates avg, max, and violations.
    """
    if not noise_readings:
        avg_noise = 0
        max_noise = 0
        violations = 0
    else:
        avg_noise = sum(noise_readings) / len(noise_readings)
        max_noise = max(noise_readings)
        violations = sum(1 for n in noise_readings if n > high_threshold)

    return supabase.table("Reports").insert({
        "report_date": report_date,
        "Classroom": Classroom,
        "Teacher": Teacher,
        "avg_noise": avg_noise,
        "max_noise": max_noise,
        "violations": violations
    }).execute()


def get_all_reports():
    return supabase.table("Reports").select("*").order("report_date").execute()


def update_report(report_id, data: dict):
    return supabase.table("Reports").update(data).eq("report_id", report_id).execute()


def delete_report(report_id):
    return supabase.table("Reports").delete().eq("report_id", report_id).execute()

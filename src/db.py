#db.py
import os
from supabase import create_client
from dotenv import load_dotenv

#load environmental variables
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase =create_client(url,key)
#------------------
#NoiseLog table operations
#------------------
#create NoiseLog
def create_log(timeStamp ,Classroom ,Teacher ,noise_level,status):
    return supabase.table("NoiseLogs").insert({
 
    "timeStamp":timeStamp,
    "Classroom":Classroom ,
    "Teacher":Teacher,
    "noise_level":noise_level,
    "status":status
}).execute()


#Get All logs


def get_all_logs():
    return supabase.table("NoiseLogs").select("*").order("status").execute()
 
#Update log  status

def update_logs(Id,data:dict):
    return supabase.table("NoiseLogs").update(data).eq("Id",Id).execute()


#Delete log
def delete_logs(Id):
    return supabase.table("NoiseLogs").delete().eq("Id",Id).execute()


#--------------------------
#Reports Table operations
#-------------------------

# create Report
def create_report(report_date, Classroom, Teacher, avg_noise, max_noise, violations):
    return supabase.table("Reports").insert({
        "report_date": report_date,
        "Classroom": Classroom,
        "Teacher": Teacher,
        "avg_noise": avg_noise,
        "max_noise": max_noise,
        "violations": violations
    }).execute()

# Get All Reports
def get_all_reports():
    return supabase.table("Reports").select("*").order("report_date").execute()

# Update Report 
def update_report(report_id, data:dict):
    return supabase.table("Reports").update(data).eq("report_id", report_id).execute()

# Delete Report
def delete_report(report_id):
    return supabase.table("Reports").delete().eq("report_id", report_id).execute()





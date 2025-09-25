# logic.py
from src.db import (
    create_log,
    get_all_logs,
    update_logs,
    delete_logs,
    create_report,
    get_all_reports,
    update_report,
    delete_report
)
class Monitor:
    """
    Acts as a bridge between frontend (Streamlit/FastAPI) and database.
    """
    # ----- NoiseLogs Methods -----
    def add_noise(self, Classroom, Teacher, noise_level=0, low_threshold=50, high_threshold=75, timeStamp=None):
        """
        Add a new noise reading to database.
        Status is auto-calculated.
        """
        if not Classroom or not Teacher:
            return {"Success": False, "Message": "Classroom and Teacher are required"}

        result = create_log(Classroom, Teacher, noise_level, low_threshold, high_threshold, timeStamp)
        if "data" in result:
            return {"Success": True, "Message": "Noise reading added successfully"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def get_noise(self):
        """Get all the noise readings from the database."""
        return get_all_logs()

    def noise_update(self, Id):
        """Mark a noise reading as completed."""
        result = update_logs(Id, {"status": "completed"})
        if "data" in result:
            return {"Success": True, "Message": "Noise reading marked as completed"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def mark_pending(self, Id):
        """Mark a noise reading as pending."""
        result = update_logs(Id, {"status": "pending"})
        if "data" in result:
            return {"Success": True, "Message": "Noise reading marked as pending"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def delete_noise(self, Id):
        """Delete a noise reading from the database."""
        result = delete_logs(Id)
        if "data" in result:
            return {"Success": True, "Message": "Noise reading deleted successfully"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}

    # ----- Reports Methods -----
    def add_report(self, report_date, Classroom, Teacher, noise_readings, high_threshold=75):
        """
        Add a new report to the database.
        Calculates avg, max, and violations automatically.
        """
        if not report_date or not Classroom or not Teacher:
            return {"Success": False, "Message": "Report date, Classroom, and Teacher are required"}

        result = create_report(report_date, Classroom, Teacher, noise_readings, high_threshold)
        if "data" in result:
            return {"Success": True, "Message": "Report added successfully"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def get_reports(self):
        """Get all reports from the database."""
        return get_all_reports()

    def update_report(self, report_id, data: dict):
        """Update fields in a report."""
        result = update_report(report_id, data)
        if "data" in result:
            return {"Success": True, "Message": "Report updated successfully"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def delete_report(self, report_id):
        """Delete a report from the database."""
        result = delete_report(report_id)
        if "data" in result:
            return {"Success": True, "Message": "Report deleted successfully"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}
    

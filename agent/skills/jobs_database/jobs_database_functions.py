import json
from datetime import date, datetime
from pathlib import Path

def store_job(job_url: str, company_name: str, job_title: str, date_posted: date|None = None):
    """Store a job posting to the shared jobs database.
    
    Args:
        job_url: URL of the job posting
        company_name: Name of the hiring company
        job_title: Title of the position
        date_posted: Date the job was posted (defaults to today if not provided)
    
    Returns:
        Success or error message
    """
    if date_posted is None:
        date_posted = date.today()
        
    # Use absolute path from project root
    jobs_file = Path(__file__).parent.parent.parent / "jobs.jsonl"
    
    job_data = {
        "job_url": job_url,
        "company_name": company_name,
        "job_title": job_title,
        "date_posted": date_posted.isoformat() if isinstance(date_posted, date) else str(date_posted),
        "date_saved": datetime.now().isoformat()
    }
    
    try:
        with open(jobs_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(job_data) + '\n')
        return f"✓ Job saved: {job_title} at {company_name}"
    except Exception as e:
        return f"✗ Error saving job: {str(e)}"
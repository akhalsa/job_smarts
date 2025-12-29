---
name: jobs_database
description: A utility function for saving job postings to the shared jobs database. Use this to persist job data you extract from job boards.
---

# Jobs Database Skill

## Overview

This skill provides a `store_job()` function that saves job postings to a centralized JSONL database at `/agent/jobs.jsonl`. Every job you scrape should be saved using this function.

**Key features:**
- Appends to shared `jobs.jsonl` file (never overwrites)
- Automatically tracks when each job was saved
- Handles date formatting automatically
- Returns success/error messages

---

## Import Statement

When writing scripts in `agent/workspace/`, use this import:

```python
from agent.skills.jobs_database.jobs_database_functions import store_job
```

---

## Function Signature

```python
def store_job(
    job_url: str,
    company_name: str,
    job_title: str,
    date_posted: date | None = None
) -> str
```

### Parameters

- **job_url** *(str, required)*: Full URL to the job posting
- **company_name** *(str, required)*: Name of the hiring company
- **job_title** *(str, required)*: Job title/position name
- **date_posted** *(date, optional)*: Date the job was posted (defaults to today)

### Returns

- Success: `"✓ Job saved: {job_title} at {company_name}"`
- Error: `"✗ Error saving job: {error_message}"`

---

## Usage Examples

### Basic Usage (Without Date)

```python
from agent.skills.jobs_database.jobs_database_functions import store_job

# Simple save - date_posted defaults to today
result = store_job(
    job_url="https://jobs.example.com/posting/123",
    company_name="Acme Corp",
    job_title="Senior Software Engineer"
)
print(result)  # ✓ Job saved: Senior Software Engineer at Acme Corp
```

### With Date Posted

```python
from agent.skills.jobs_database.jobs_database_functions import store_job
from datetime import date

# Include the date the job was posted
result = store_job(
    job_url="https://jobs.example.com/posting/456",
    company_name="Tech Startup Inc",
    job_title="Product Manager",
    date_posted=date(2024, 12, 15)
)
```

### In a Scraping Loop

```python
from agent.skills.jobs_database.jobs_database_functions import store_job
from bs4 import BeautifulSoup

# After extracting jobs with BeautifulSoup
html = "<html>...</html>"  # From Playwright
soup = BeautifulSoup(html, "html.parser")

for job_card in soup.find_all("div", class_="job-card"):
    # Extract job data
    title = job_card.find("h3", class_="title").get_text(strip=True)
    company = job_card.find("span", class_="company").get_text(strip=True)
    link = job_card.find("a", class_="apply-link")["href"]
    
    # Save immediately
    result = store_job(
        job_url=link,
        company_name=company,
        job_title=title
    )
    print(result)
```

### Parsing Date Strings

If you extract date strings from the page, parse them first:

```python
from agent.skills.jobs_database.jobs_database_functions import store_job
from datetime import datetime

# Parse date string
date_text = "Posted on Dec 15, 2024"
posted_date = datetime.strptime(date_text, "Posted on %b %d, %Y").date()

store_job(
    job_url="https://example.com/job",
    company_name="Example Co",
    job_title="Engineer",
    date_posted=posted_date
)
```

---

## Best Practices

### ✅ DO:
- Call `store_job()` immediately after extracting each job
- Use try/except to handle errors gracefully
- Print the result to verify saves
- Parse date strings before passing to `date_posted`

### ❌ DON'T:
- Wait to save all jobs at once (save incrementally)
- Manually write to `jobs.jsonl` (always use this function)
- Assume all pages have date information (omit if unavailable)

---

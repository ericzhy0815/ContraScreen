import csv
from jobspy import scrape_jobs
from apscheduler.schedulers.background import BackgroundScheduler
import time
import random

# list of all major cities in the US
major_cities = ["San Francisco, CA", "New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX", "Phoenix, AZ", 
                "Philadelphia, PA", "San Antonio, TX", "San Diego, CA", "Dallas, TX", "San Jose, CA", "Austin, TX", 
                "Jacksonville, FL", "Fort Worth, TX", "Columbus, OH", "Charlotte, NC", "Indianapolis, IN", "San Francisco, CA", 
                "Seattle, WA", "Denver, CO", "Washington, DC", "Boston, MA", "El Paso, TX", "Nashville, TN", "Detroit, MI", 
                "Oklahoma City, OK", "Portland, OR", "Las Vegas, NV", "Memphis, TN", "Louisville, KY", "Baltimore, MD", 
                "Milwaukee, WI", "Albuquerque, NM", "Tucson, AZ", "Fresno, CA", "Mesa, AZ", "Sacramento, CA", "Atlanta, GA", 
                "Kansas City, MO", "Colorado Springs, CO", "Omaha, NE", "Raleigh, NC", "Miami, FL", "Long Beach, CA", 
                "Virginia Beach, VA", "Oakland, CA", "Minneapolis, MN", "Tulsa, OK", "Arlington, TX", "Tampa, FL", 
                "New Orleans, LA", "Wichita, KS", "Cleveland, OH", "Bakersfield, CA", "Aurora, CO", "Anaheim, CA", 
                "Honolulu, HI", "Santa Ana, CA", "Riverside, CA", "Corpus Christi, TX", "Lexington, KY", "Stockton, CA", 
                "Henderson, NV", "Saint Paul, MN", "St. Louis, MO", "Cincinnati, OH", "Pittsburgh, PA", "Greensboro, NC", 
                "Lincoln, NE", "Anchorage, AK", "Plano, TX", "Orlando, FL", "Irvine, CA", "Newark, NJ", 
                "Durham, NC", "Chula Vista, CA", "Toledo, OH", "Fort Wayne, IN", "St. Petersburg, FL", 
                "Laredo, TX", "Jersey City, NJ", "Chandler, AZ", "Madison, WI"]


def get_jobs(location):
    try:
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"],
            search_term="software engineer, data science",
            google_search_term="",
            location=location,
            results_wanted=20000,
            hours_old=24,
            country_indeed='USA',
            linkedin_fetch_description=True
        )
        if jobs is None or jobs.empty:
            print(f"No jobs found for {location}. Skipping...")
            return
        
        print(f"Found {len(jobs)} jobs in {location}")
        print(jobs.head())

        file_name = f"csv/jobs_{location.replace(',', '').replace(' ', '_')}.csv"
        jobs.to_csv(file_name, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)

    except Exception as e:
        print(f"Error while scraping {location}: {e}")


# scheduler = BackgroundScheduler()

for city in major_cities:
    get_jobs(city)
    sleep_time = random.uniform(2, 5)  # Random delay between 2-5 seconds
    print(f"Finished scraping {city}. Sleeping for {sleep_time:.2f} seconds...")
    time.sleep(sleep_time)


# # Start the scheduler
# scheduler.start()
# print("Scheduler started. Press Ctrl+C to exit.")

# try:
#     while True:
#         time.sleep(1)  # Keep the script running
# except (KeyboardInterrupt, SystemExit):
#     scheduler.shutdown()
#     print("Scheduler stopped.")
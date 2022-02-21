from bs4 import BeautifulSoup
import requests
html_text = requests.get("https://www.freelancer.com/job-search/small-programming-jobs-online/").text
print(html_text)

line = "--------------------------------------------------------------------------------------------------------"
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("div", class_='JobSearchCard-item')
for job in jobs:
    job_scope = job.find("a", class_='JobSearchCard-primary-heading-link')
    job_des = job.find("p", class_='JobSearchCard-primary-description')
    job_tags = job.find("div", class_='JobSearchCard-primary-tags')
    job_pay = job.find("div", class_='JobSearchCard-primary-price')

    print(f"""
    Job scope : {job_scope.text}
    Further details : {job_des.text}
    Skills required : {job_tags.text}
    Job salary : {job_pay.text}
    """)
    print(line)
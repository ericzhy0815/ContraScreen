# -*- coding: utf-8 -*-
# Author: Kevin Wu

"""

ATS:
Job Listing Type:
Form URL:
Listing URL:

Global URL Association Rule:
    - up for debate: are we going to establish association between un-parsable form URLs and their listing URLs?

ATS: greenhouse.io
Job Listing Type: Integrated with application form (no url back-tracing needed)
Form URL: https://boards.greenhouse.io/array/jobs/5440151004?gh_jid=5440151004
Listing URL: N/A

ATS: WorkDay
Job Listing Type: Back Tracable
Form URL: https://sbdinc.wd1.myworkdayjobs.com/en-US/Stanley_Black_Decker_Career_Site/job/Fullerton%2C-CA%2C-United-States/Sr-Quality-Engineer_REQ-1000031428/apply/applyManually?locationCountry=bc33aa3152ec42d4995f4791a106ed09
Listing URL: https://sbdinc.wd1.myworkdayjobs.com/en-US/Stanley_Black_Decker_Career_Site/details/Sr-Quality-Engineer_REQ-1000031428
(Example 2)
Form URL: https://draper.wd5.myworkdayjobs.com/en-US/Draper_Careers/job/Cambridge%2C-MA/Group-Leader---Electromechanical-Integration---Test_JR000678/apply/applyManually?redirect=/en-US/Draper_Careers/job/Cambridge%252C-MA/Software-Engineering-Intern_JR000640/apply/useMyLastApplication?source=LinkedIn
Listing URL: https://draper.wd5.myworkdayjobs.com/en-US/Draper_Careers/details/Group-Leader---Electromechanical-Integration---Test_JR000678
https://draper.wd5.myworkdayjobs.com/en-US/Draper_Careers/details/Software-Engineering-Intern_JR000640
(Example 3)
Form URL: https://homedepot.wd5.myworkdayjobs.com/en-US/CareerDepot/job/GEORGIA---VIRTUAL---GA01/PRODUCT-MANAGEMENT-SR-MANAGER_Req134531/apply/applyManually
*** What could be mistaken as the Form URL, but is actually the login page: https://homedepot.wd5.myworkdayjobs.com/CareerDepot/login?redirect=%2FCareerDepot%2Fjob%2FGEORGIA---VIRTUAL---GA01%2FPRODUCT-MANAGEMENT-SR-MANAGER_Req134531%2Fapply
Listing URL: https://homedepot.wd5.myworkdayjobs.com/CareerDepot/details/PRODUCT-MANAGEMENT-SR-MANAGER_Req134531

ATS: eightfold.ai
Job Listing Type: Back Tracable
Form URL: https://jobs.siemens.com/careerhub/explore/jobs/563156123119367?show_apply=1
Listing URL: https://jobs.siemens.com/careerhub/explore/jobs/563156123119367

ATS: iCims
Job Listing Type: Not Directly Back Tracable; May have to ask user for listing URL!
Form URL: https://maintenancejobs-alaskaair.icims.com/jobs/13846/aircraft-technician---anc/candidate?from=login&eem=OOesqwGUhePkxOiJbrU6d6x2%252B%252BlWzFTuA%252FGsXhfTG4A%253D&code=3c1b8f81e37ad3cb7d3667b37525ffb673d12a8e87dab5f0083c5609091bb3af
Listing URL: https://careers.alaskaair.com/anchorage-ak/aircraft-technician-anc/89893B7DD31041A9BE8BA110EB803D57/job/
(Example 2)
Form URL: https://www.uber.com/careers/apply/form/139574
Listing URL: https://www.uber.com/global/en/careers/list/139574/?uclick_id=82751eea-d7e1-46b8-b946-e7c52e588f82
(Example 3)
Listing URL: https://jobs.careers.microsoft.com/global/en/job/1806146
Form URL: https://jobs.careers.microsoft.com/global/en/apply?Job_id=1806146&utm_source=Microsoft%20Global%20Careers%20Site&utm_campaign=Microsoft%20Global%20Careers%20Site
(Example 4)
Goldman Sachs
Form URL: https://hdpc.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CampusHiring/requisitions/preview/140897/apply/email?mode=location
Listing URL: https://higher.gs.com/roles/140897

"""

import re


def parse_workday_url(url):
    # Check if the URL contains "/job/"
    if "/job/" not in url:
        return 0

    # Extract the base URL before "/job/"
    base_url, job_info = url.split("/job/", 1)

    # Extract only the first item before the first "/apply/"
    job_parts = job_info.split('/')
    job_title_id = None
    for i in range(len(job_parts)):
        if job_parts[i] == "apply":
            job_title_id = job_parts[i - 1]
            break

    if job_title_id is None:
        return 0

    # Construct the new URL
    new_url = f"{base_url}/details/{job_title_id}"

    return new_url


def parse_greenhouse_url(url):
    return url


test_input_url = \
"https://homedepot.wd5.myworkdayjobs.com/en-US/CareerDepot/job/GEORGIA---VIRTUAL---GA01/PRODUCT-MANAGEMENT-SR-MANAGER_Req134531/apply/applyManually"
test_output_url = parse_workday_url(test_input_url)
print(test_output_url)










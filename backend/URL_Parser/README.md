# ATS Job Listing and Application Form URL Parsing

## ATS Platforms Compilation:
https://everyats.com/

## Overview
This document provides information on different Applicant Tracking Systems (ATS) and their job listing URL structures. It categorizes ATSs based on their ability to backtrace application form URLs to job listing URLs and highlights specific URL examples for each ATS.

### Global URL Association Rule
- **Discussion:** Should we establish an association between non-parsable form URLs and their listing URLs?

## ATS Details

| ATS              | Job Listing Type | Form URL | Listing URL |
|-----------------|-----------------|----------|-------------|
| **greenhouse.io** | Integrated with application form (no back-tracing needed) | https://boards.greenhouse.io/array/jobs/5440151004?gh_jid=5440151004 | N/A |
| **WorkDay** | Back Tracable | https://sbdinc.wd1.myworkdayjobs.com/en-US/Stanley_Black_Decker_Career_Site/job/Fullerton%2C-CA%2C-United-States/Sr-Quality-Engineer_REQ-1000031428/apply/applyManually?locationCountry=bc33aa3152ec42d4995f4791a106ed09 | https://sbdinc.wd1.myworkdayjobs.com/en-US/Stanley_Black_Decker_Career_Site/details/Sr-Quality-Engineer_REQ-1000031428 |
|  |  | https://draper.wd5.myworkdayjobs.com/en-US/Draper_Careers/job/Cambridge%2C-MA/Group-Leader---Electromechanical-Integration---Test_JR000678/apply/applyManually?redirect=/en-US/Draper_Careers/job/Cambridge%252C-MA/Software-Engineering-Intern_JR000640/apply/useMyLastApplication?source=LinkedIn | https://draper.wd5.myworkdayjobs.com/en-US/Draper_Careers/details/Group-Leader---Electromechanical-Integration---Test_JR000678 / https://draper.wd5.myworkdayjobs.com/en-US/Draper_Careers/details/Software-Engineering-Intern_JR000640 |
|  |  | https://homedepot.wd5.myworkdayjobs.com/en-US/CareerDepot/job/GEORGIA---VIRTUAL---GA01/PRODUCT-MANAGEMENT-SR-MANAGER_Req134531/apply/applyManually | https://homedepot.wd5.myworkdayjobs.com/CareerDepot/details/PRODUCT-MANAGEMENT-SR-MANAGER_Req134531 |
| **eightfold.ai** | Back Tracable | https://jobs.siemens.com/careerhub/explore/jobs/563156123119367?show_apply=1 | https://jobs.siemens.com/careerhub/explore/jobs/563156123119367 |
| **iCims** | Not Directly Back Tracable; May require user input | https://maintenancejobs-alaskaair.icims.com/jobs/13846/aircraft-technician---anc/candidate?from=login&eem=OOesqwGUhePkxOiJbrU6d6x2%252B%252BlWzFTuA%252FGsXhfTG4A%253D&code=3c1b8f81e37ad3cb7d3667b37525ffb673d12a8e87dab5f0083c5609091bb3af | https://careers.alaskaair.com/anchorage-ak/aircraft-technician-anc/89893B7DD31041A9BE8BA110EB803D57/job/ |
|  |  | https://www.uber.com/careers/apply/form/139574 | https://www.uber.com/global/en/careers/list/139574/?uclick_id=82751eea-d7e1-46b8-b946-e7c52e588f82 |
|  |  | https://jobs.careers.microsoft.com/global/en/apply?Job_id=1806146&utm_source=Microsoft%20Global%20Careers%20Site&utm_campaign=Microsoft%20Global%20Careers%20Site | https://jobs.careers.microsoft.com/global/en/job/1806146 |
|  |  | https://hdpc.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CampusHiring/requisitions/preview/140897/apply/email?mode=location | https://higher.gs.com/roles/140897 |

This README serves as a reference for tracking the back-tracing ability of different ATSs, facilitating an improved approach for parsing URLs and associating job listings effectively.

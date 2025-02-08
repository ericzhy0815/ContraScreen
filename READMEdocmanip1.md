1. Insteall python.docx

pip install python-docx

2. Data in the form of Python dictionary, keys are placeholders and values are the info that will replace the placeholders:

example:
data = {
    "First_Name": "John",
    "Last_Name": "Doe",
    "Phone_Number": "+1234567890",
    "Email": "john.doe@example.com",
    "LinkedIn": "linkedin.com/in/johndoe",
    "Skill_1": "Python",
    "Skill_2": "Data Analysis",
    "Job_Title": "Software Engineer",
    "Company_Name": "Tech Corp",
    "Start_Date": "Jan 2020",
    "End_Date": "Present",
    "Location": "San Francisco, CA",
    "Description": "Developed scalable backend systems.",
    "Degree": "Bachelor of Science in Computer Science",
    "Institution": "University of California",
    "Graduation_Date": "May 2019"
}

3. resume generation function; 1st param is path to template with fields, 2nd is name of the generated docx, data is the dictionary data
generate_resume(template_path, "generated_resume0.docx", data)

4. Future enhancement: support dynamic sections (ex: multiple work experience entries)

5. Template instructions:
Find a docx resume template you would like to use (Microsoft Office templates, Resume Worded, etc.)

Modify sections in edit mode in the following way ->

Original (Dummy info in the template from the web):
Mary Smith | Phone: +12345678 | Email: Mary@google.com
Ferris, Maryland

Description:
Bachelor of Science in Computer Science and Economics
Graduate student at Some Random University with a strong background in Computer Science and Economics. Experienced in research and development things.
____
Modified:
{{First_Name}} {{Last_Name}} | Phone: {{Phone_Number}} | Email: {{Email}}
{{Location}}

Description:
{{Degree}}
{{Description}}
____
Note: key from the data dictionary should be exactly inputted into the field with case, numbers and same symbols: {{some_key}}

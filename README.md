# CA_assignment_01

Using any programming language of your choice (Java, JavaScript, Python, etc.) please create a small automation project with a framework of your choice (Selenium, Playwright, Cypress, etc.) that automates following scenarios:
- Access the following URL: https://cloudacademy.com/ execute following search operations into the search area:
  - Search for AWS, GCP and Azure. Assert the presence of correct results into the plage.
- Move to pricing page and:
  - Assert presence of the expected pricing plans
  - Enter the Small teams pricing plan detail selecting the button start now
  - Assert which elements should be present into the form to be correctly filled

Implement test reporting with a reporting tool of your choice (allure, TestNg, etc.)

Extra points wil be assigned if the test scenario will use gherkin language ( leveraging Cucumber, Behave, etc.)

Please share a link to the project (google drive with package's or even better GitHub project) to the recruitment team

---
Run on Python 3.12.
Playwright with Behave and Behavex for reporting.

Steps to setup project:
- install requirements.txt
- from the terminal run the command 'playwright install' to install the playwright browsers

To run tests:
- with reports run in terminal the command 'behavex features/'
- without reports run in terminal the command 'behave'

Reports will be generated in folder output.

---
Notes:
- some optimizations can be made
- some evidences like screenshots can be added in order to add more traceability
# XML Validation Script

This script validates XML files against the provided XSD schema. It checks if the XML structure adheres to the expected rules and provides feedback on any validation issues.

---

## How to Run the Script

### Prerequisites
- Ensure you have Python 3 installed.
- Install the required library by running:
  ```bash
  pip install lxml

### Running the Script
Place your XML file(s) (e.g., FSA029-Sample-Full.xml or FSA029-Sample-Valid.xml) and the Python script in the same directory.
Open a terminal or command prompt and navigate to the directory containing the script.
Run the script with the following command:
  ```bash
  python script.py <directory> <xml_file>
```
**ps: dont forget the space between dir and xml_file.**

### Example:

python script.py C:\Users\user\Downloads\SuadeTask FSA029-Sample-Full.xml

# The extra mile

### (a) What causes it to fail schema validation? Why do you think the regulator has included a valid file in their examples?
Reason for failure:
The XML contains multiple sections under the <Capital> element, specifically <IncorporatedEntities> and <PartnershipsSoleTraders>.
However, the schema enforces that only one of these elements can appear within the <Capital> element at any given time,
due to the xs:choice structure in the XSD schema.

Reason the valid file was included in their examples:
They included a valid file to demonstrate the correct structure for the XML file to follow.

### (b) How would you fix the file to pass the schema validation?
To fix the file and pass the schema validation, you need to ensure that only one of the following elements appears in the <Capital> section:

<IncorporatedEntities>
<PartnershipsSoleTraders>
<LLPs>
  
### (c) Why do you think the regulator has included an invalid file in their examples?
The inclusion of an invalid file in the regulator's examples is likely intended to ensure that their validation code is working correctly.
By including a file that fails validation, they can demonstrate that the validation process catches errors and provides the correct feedback. 
This helps confirm that the validation tool or system is functioning as expected, able to detect mistakes, and return appropriate error messages 
for users to correct their submissions.

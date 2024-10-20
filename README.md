# HL7 Message Converter

This repository contains a Python script and Jupyter Notebook to convert patient vitals data from CSV format into HL7 message format. HL7 (Health Level 7) is a set of international standards used to transfer clinical and administrative data between software applications used by various healthcare providers.

## Repository Structure

```bash
tasks_DS/
├── Input.txt               # Input file with sample HL7 data.
├── README.md               # This README file with explanations and usage instructions.
├── Vitals_allscript.csv     # Input CSV file with patient vitals information.
├── convert_to_hl7.py       # Python script to convert CSV data into HL7 format.
├── correct output.txt      # File with the correct HL7 output format for comparison.
├── header.txt              # File containing headers for HL7 data.
├── output.hl7              # Generated HL7 output from the script.
├── requirements.txt        # Required dependencies to run the Python script.
└── vitals63.ipynb          # Jupyter Notebook for interactive HL7 conversion.
```

## Purpose

The purpose of this project is to read a CSV file containing patient vitals data and convert each row into an HL7 message. This helps in integrating patient data with systems that follow HL7 standards, allowing for smooth electronic data exchange in healthcare environments.

## CSV Format Explanation

The input CSV file (`Vitals_allscript.csv`) contains patient data with the following columns:

| Source Column/Field Name | Source Example | Description               | Format       | HL7 Field      | Requirement Level | Default/Generic Value | HL7 Example        | Notes                             |
|--------------------------|----------------|---------------------------|--------------|----------------|-------------------|-----------------------|--------------------|-----------------------------------|
| N/A                      | N/A            | Sending Application        | HL7          | MSH-3          | Required (R)       | "Touchworks"           | "Touchworks"       |                                   |
| N/A                      | N/A            | Sending Facility           | HL7          | MSH-4          | Required (R)       | "Mountain West"        | "Mountain West"    |                                   |
| N/A                      | N/A            | Receiving Application       | HL7          | MSH-5          | Required (R)       | "Rhapsody^Rhapsody"    | "Rhapsody^Rhapsody" |                                   |
| N/A                      | N/A            | Receiving Facility         | HL7          | MSH-6          | Required (R)       | "EPIC^EPIC"            | "EPIC^EPIC"        |                                   |
| N/A                      | N/A            | Message Date/Time          | HL7          | MSH-7          | Required (R)       | currentDate            | 20240828125126      | Expected format: yyyyMMddHHmmss  |
| Patient MRN              | 1122333        | Patient ID-ID              | HL7          | PID-3.1        | Required (R)       | 5677654                | 2                  |                                   |
| LastName                 | Julia          | Patient Last Name          | HL7          | PID-5.1        | Required (R)       |                       |                    |                                   |
| FirstName                | Zeki           | Patient First Name         | HL7          | PID-5.2        | Required (R)       |                       |                    |                                   |
| DateOfBirth              | 11/23/86       | Patient Date of Birth      | HL7          | PID-7          | Required (R)       |                       | Expected format: yyyyMMdd        |
| Metric_Abbr              | N/A            | Observation ID             | HL7          | OBX-3          | Required (R)       |                       |                    |                                   |
| Result                   | N/A            | Observation Value          | HL7          | OBX-5          | Required (R)       |                       |                    |                                   |

This file follows HL7 message structure and contains data that can be processed into HL7 messages using the provided Python script.

## Python Script (`convert_to_hl7.py`)

### Functionality

The Python script reads the CSV file and converts each row of data into an HL7 message. It creates segments of the HL7 message like:
- **MSH** (Message Header): Contains metadata like sender, receiver, and message type.
- **PID** (Patient Identifier): Holds patient-specific information like name, date of birth, and patient ID.
- **OBR** (Observation Request): Contains details about the observation request (e.g., test performed).
- **OBX** (Observation Result): Holds the actual result of the observation (e.g., blood pressure, weight).

### Key Functions

1. **`create_hl7_message(row)`**: 
   - Generates the HL7 message by extracting relevant data from a CSV row.
   - Constructs the MSH, PID, OBR, and OBX segments based on the provided data.

2. **`convert_to_hl7(input_file, output_file)`**:
   - Reads the CSV file and iterates over the rows to convert each row into an HL7 message.
   - Writes the HL7 messages to the specified output file.

### Example of HL7 Message

```plaintext
MSH|^~\&|TouchWorks|Southwest Medical Associates|Rhapsody^Rhapsody|Epic^Epic|20241020191436||ORU^R01|20004200_001|P|2.5.1
PID|||20004200^^^^TWSMAMRN||Martinez^David^E||20080419|M|||4479 E Mesquite Desert Trl^^Tucson^AZ^857063013
OBR|1||||||20211022170300
OBX|1||^BP SYS^LN||110|mm of Mercury
```

### How to Run the Script

1. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Python script**:
   ```bash
   python convert_to_hl7.py Vitals_allscript.csv output.hl7
   ```

This will generate an HL7 file (`output.hl7`) with the converted messages.

## Jupyter Notebook (`vitals63.ipynb`)

The Jupyter Notebook is provided for users who prefer to run the HL7 conversion interactively. It contains the same functionality as the Python script but allows for real-time exploration and execution of the code. The notebook can be used for testing and debugging specific rows or observations.

### Usage

- Open the `vitals63.ipynb` in a Jupyter Notebook environment.
- Follow the cells to process the CSV file and generate HL7 messages.
  
## Requirements

All required dependencies are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```

## Correct HL7 Output

The file `correct output.txt` contains the correct HL7 message output format. You can use it as a reference for validating the generated HL7 messages.

## Conclusion

This project provides an efficient way to convert patient data from CSV format to HL7 messages. By using the provided script or notebook, you can easily generate HL7-compliant messages for integration with healthcare systems. The project follows HL7 standards, ensuring the correct structure and format of the messages for seamless data exchange.
# HL7 Message Converter

This repository contains a Python script to convert patient vitals data from a structured text format into HL7 (Health Level 7) message format. HL7 is a set of international standards used to transfer clinical and administrative data between software applications used by various healthcare providers.

## Repository Structure

```
.
├── Input.txt
├── README.md
├── convert.py
├── correct output.txt
├── header.txt
├── info
│   ├── LOINCUniversalLabOrdersValueSet.csv
│   ├── MCL LOINC Values.xls
│   └── Vitals_allscript.csv
└── requirements.txt
```

## Purpose

The purpose of this project is to read structured text files containing patient vitals data and convert each set of data into an HL7 message. This helps in integrating patient data with systems that follow HL7 standards, allowing for smooth electronic data exchange in healthcare environments.

## Input Format Explanation

The input data is split into two files:

1. `header.txt`: Contains the header information for the data fields.
2. `Input.txt`: Contains the actual patient data, with fields separated by pipe (`|`) characters.

## Python Script (`convert.py`)

### Functionality

The Python script reads the header and input files, processes the data, and generates HL7 messages. It performs the following main tasks:

1. Loads and validates the input data
2. Processes the data into a suitable format for HL7 generation
3. Generates HL7 messages
4. Writes the HL7 output to a file

### Key Functions

1. `load_and_validate_data(header_file, data_file)`: 
   - Reads the header and data files
   - Handles rows with varying columns
   - Returns a pandas DataFrame with the loaded data

2. `process_data(df)`:
   - Organizes the data into a nested dictionary structure for easy HL7 generation

3. `generate_hl7(data)`:
   - Creates HL7 messages from the processed data
   - Handles special cases for different date ranges
   - Generates MSH, PID, OBR, and OBX segments

4. `main(header_file, input_file, output_hl7)`:
   - Orchestrates the entire process from data loading to HL7 generation and output

### Example of HL7 Message

```
MSH|^~\&|TouchWorks|Southwest Medical Associates|Rhapsody^Rhapsody|Epic^Epic|20240828125126||ORU^R01|20004200_001_20211022170300|P|2.5.1
PID|||20004200^^^^TWSMAMRN||Martinez^David^E||20080419|M|||4479 E Mesquite Desert Trl^^Tucson^AZ^857063013
OBR|1||||||20211022170300
OBX|1||^PUL RATE^LN||85|/min
OBX|2||^BP DIAS^LN||67|mm of Mercury
OBX|3||^BP SYS^LN||110|mm of Mercury
OBX|4||^WGT^LN||45.3|kg
OBX|5||^HGT^LN||147.3|cm
OBX|6||59408-5^O2^LN||97
OBX|7||^TEMP^LN||36.4|C
```

## How to Run the Script

1. Ensure you have Python and the required dependencies installed. You can install the dependencies using:
   ```
   pip install -r requirements.txt
   ```

2. Run the Python script:
   ```
   python convert.py
   ```

   The script uses the following default file paths:
   - Header file: `header.txt`
   - Input file: `Input.txt`
   - Output file: `generated_output.txt`

   You can modify these file paths in the `main()` function if needed.

## Additional Files

- `correct output.txt`: Contains the correct HL7 message output format for comparison and validation.
- `info/`: Directory containing additional information and reference files:
  - `LOINCUniversalLabOrdersValueSet.csv`: LOINC (Logical Observation Identifiers Names and Codes) value set for lab orders.
  - `MCL LOINC Values.xls`: Excel file with LOINC values.
  - `Vitals_allscript.csv`: Sample CSV file with vitals data (not used in the current script but may be useful for reference).

## Conclusion

This project provides an efficient way to convert patient data from a structured text format to HL7 messages. By using the provided script, you can easily generate HL7-compliant messages for integration with healthcare systems. The project follows HL7 standards, ensuring the correct structure and format of the messages for seamless data exchange.
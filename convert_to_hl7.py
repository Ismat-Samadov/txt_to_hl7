import csv
from datetime import datetime

# Define the correct header manually based on the structure of your file
headers = ['PatientId', 'Patient MRN', 'LastName', 'FirstName', 'MiddleName', 'DateOfBirth', 'Sex', 'Metric_Desc', 'Metric_Abbr', 'Result',
           'UnitOfMeasure', 'CreateDTTM', 'PerformedDTTM', 'DecodedValue', 'QOClassificationDE', 'AnswerDE', 'VitalValue', 'NormalizedValue', 
           'NumericFinding', 'Unit_Abbr', 'RecordedDTTM', 'QODE', 'Vital_Status', 'Mode_Name', 'ActivityHeaderID', 'ItemID', 'LoincLabCode', 
           'APM_Patient_ID', 'APM_MRN', 'APM_Patient_First_Name', 'APM_Patient_Last_Name', 'APM_Patient_MI', 'APM_Patient_Street1', 
           'APM_Patient_Street2', 'APM_Patient_City', 'APM_Patient_State', 'APM_Patient_Zip_Code', 'APM_Patient_Country', 'APM_Patient_Sex', 
           'APM_Patient_DOB', 'Patient_Home_Phone', 'Patient_Work_Phone', 'Patient_Work_Ext', 'Patient_Cell_Phone', 'Patient_Primary_Phone_Type', 
           'Patient_Primary_Phone_Number', 'Patient_Emailx']

def create_hl7_message(row):
    # Format the Control ID: Use MRN, Metric_Abbr, and PerformedDTTM (observation date)
    control_id = f'{row["Patient MRN"]}_{row["ActivityHeaderID"]}_{row["PerformedDTTM"].replace("-", "").replace(" ", "").replace(":", "")[:12]}'

    # Create MSH segment
    msh_segment = f'MSH|^~\\&|TouchWorks|Southwest Medical Associates|Rhapsody^Rhapsody|Epic^Epic|{datetime.now().strftime("%Y%m%d%H%M%S")}||ORU^R01|{control_id}|P|2.5.1'

    # Create PID segment
    pid_segment = f'PID|||{row["Patient MRN"]}^^^^TWSMAMRN||{row["LastName"]}^{row["FirstName"]}^{row["MiddleName"]}||{row["DateOfBirth"].replace("-", "")}|{row["Sex"]}|||{row["APM_Patient_Street1"]}^^{row["APM_Patient_City"]}^{row["APM_Patient_State"]}^{row["APM_Patient_Zip_Code"]}'

    # Create OBR segment
    obr_segment = f'OBR|1||||||{row["PerformedDTTM"].replace("-", "").replace(" ", "").replace(":", "")[:14]}'  # OBR date formatting

    # Create OBX segment (for observations)
    obx_segment = f'OBX|1||{row["LoincLabCode"]}^{row["Metric_Abbr"]}^LN||{row["Result"]}|{row["UnitOfMeasure"]}'

    # Combine all segments
    hl7_message = f'{msh_segment}\n{pid_segment}\n{obr_segment}\n{obx_segment}\n'
    
    return hl7_message

def convert_to_hl7(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w') as outfile:
        csv_reader = csv.DictReader(infile, delimiter='|', fieldnames=headers)
        
        # Skip the first row if it's a header
        next(csv_reader)
        
        for row in csv_reader:
            hl7_message = create_hl7_message(row)
            outfile.write(hl7_message + '\n')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_to_hl7.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_to_hl7(input_file, output_file)

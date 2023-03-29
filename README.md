# Patient-List
python classes for holding a list of patients and their data
<h4>What you can do with it</h4>
patient = PatientList.add_patient(
    patient_id=user_id,
    symptoms=symptom_list
)
creates a patient object if patient_id not in current list
delete_patient = i = PatientList.delete_patient("2")
deletes patient and returns deleted patient object, returns None if patient doesn't exist
patient = PatientList.get_patient(user_id)
if no patient is found, returns None
symptom_list = patient.get_symptom_list()
returns the patient's symptom list


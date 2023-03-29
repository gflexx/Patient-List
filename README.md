# Patient-List
python classes for holding a list of patients and their data
# What you can do with it
patient = PatientList.add_patient(
    patient_id=user_id,
    symptoms=symptom_list
)
<p>creates a patient object if patient_id not in current list</p>
<p>delete_patient = i = PatientList.delete_patient("2")</p>
<p>deletes patient and returns deleted patient object, returns None if patient doesn't exist</p>
<p>patient = PatientList.get_patient(user_id)</p>
<p>if no patient is found, returns None</p>
<p>symptom_list = patient.get_symptom_list()</p>
<p>returns the patient's symptom list</p>


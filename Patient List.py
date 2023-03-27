class PatientList:
    """
    stores patient data as patient object
    """

    def __init__(self):
        self.patient_list = list()

    def get_patient(self, target_id):
        target_patient = []
        for patient in self.list_patients():
            if patient.patient_id == target_id:
                target_patient.append(patient)
        if len(target_patient) > 0:
            return target_patient[0]
        else:
            return None

    def add_patient(self, patient_id, symptoms):
        patient = Patient(
            patient_id=patient_id,
            symptoms=symptoms
        )
        self.patient_list.append(
            patient
        )
        return patient

    def update_patient(self, patient_id, symptoms):
        patient = self.get_patient(patient_id)
        if patient is not None:
            for symptom in symptoms:
                if symptom not in patient.get_symptom_list():
                    patient.symptom_list.append(symptom)
            print(patient.get_symptom_list())
            return patient
        else:
            return None


    def delete_patient(self, patient_id):
        patient = self.get_patient(patient_id)
        if patient is not None:
            self.patient_list.remove(patient)
            return patient
        else:
            return None

    def list_patients(self):
        return self.patient_list
    
class Patient:
    """
    patient class holds user details and symptom list 
    """

    patient_id = ''
    symptom_list = list()

    def __init__(self, patient_id, symptoms) -> None:
        self.patient_id = patient_id
        for symptom in symptoms:
            self.symptom_list.append(symptom)
        
    def __str__(self):
        return str(self.patient_id)

    def get_patient_id(self):
        return self.patient_id
    
    def get_symptom_list(self):
        return self.symptom_list
    
    def add_symptom(self, symptom):
        self.symptom_list.extend(symptom)
        return self.symptom_list

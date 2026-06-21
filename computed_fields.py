from pydantic import BaseModel,EmailStr,Field,computed_field
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):
    name: Annotated[str, Field(..., description="Patient's full name")]
    email: EmailStr
    age: Annotated[int, Field(..., gt=0, description="Age must be a positive integer", strict=True)]#strict=True prevents type cobersion
    allergies: Optional[List[str]]=None
    contact_info: Dict[str, str]
    height:float
    weight: float
    
    @computed_field
    @property
    def calculate_bmi(self)->float:
        return self.weight/(self.height**2)
    

def insert_patient_data___(patient_data: patient):
    print(patient_data.name)
    print(patient_data.age)
    print(patient_data.allergies)
    print(patient_data.contact_info)
    print(f"Calculated BMI: {patient_data.calculate_bmi}")
    print("inserted data into DB")

patient_info={
    'name':'John Doe',
    'email': 'john.doe@example.com',
    'age':30,
    'allergies': ['pollen', 'shellfish'],
    'contact_info': {'email': 'john.doe@example.com', 'phone': '123-456-7890'},
    'height': 1.75,
    'weight': 70.0
}
insert_patient_data___(patient(**patient_info)) 
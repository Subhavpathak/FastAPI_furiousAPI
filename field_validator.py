from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):
    name: Annotated[str, Field(..., description="Patient's full name")]
    email: EmailStr
    age: Annotated[int, Field(..., gt=0, description="Age must be a positive integer", strict=True)]#strict=True prevents type cobersion
    allergies: Optional[List[str]]=None
    contact_info: Dict[str, str]
    
    @field_validator('email',mode='after')# after type_coercion
    @classmethod
    def validate_email(cls, v):
        valid_domains=['dsfc.com','example.com']
        if not any(v.endswith(domain) for domain in valid_domains):
            raise ValueError('Invalid email domain')
        return v

def insert_patient_data___(patient_data: patient):
    print(patient_data.name)
    print(patient_data.age)
    print(patient_data.allergies)
    print(patient_data.contact_info)
    print("inserted data into DB")

patient_info={
    'name':'John Doe',
    'email': 'john.doe@example.com',
    'age':30,
    'allergies': ['pollen', 'shellfish'],
    'contact_info': {'email': 'john.doe@example.com', 'phone': '123-456-7890'}
}
insert_patient_data___(patient(**patient_info)) ##validation & type-coercion
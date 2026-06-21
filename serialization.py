from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    email: str
    address: Address
    allergies: list[str] = []
    contact_info: dict[str, str] = {}
    
address_data = {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip_code": "12345"
}

address = Address(**address_data)

patient_data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "address": address,
    "allergies": ["pollen", "shellfish"],
    "contact_info": {"email": "john.doe@example.com", "phone": "123-456-7890"}
}

patient = Patient(**patient_data)

temp=patient.model_dump(include={'name','age','email'})
temp2=patient.model_dump_json()    
## for export 
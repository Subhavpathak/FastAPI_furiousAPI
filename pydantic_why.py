## codes are just for learning purpose not real implementation
def insert_patient_data(name,age):
    print(name)
    print(age)
    print("inserted data into DB")
    
# insert_patient_data("John Doe", 'thirty')//no type validation

def insert_patient_data_(name:str,age:int):
    print(name)
    print(age)
    print("inserted data into DB")
    
## now datatype signature is visible still produces no error if wrong datatype is provided

#now
def insert_patient_data__(name:str,age:int):
    if(type(name)==str and type(age)==int):
        print(name)
        print(age)
        print("inserted data into DB")
        
    else:
        raise TypeError("Invalid data type for name or age")
    
#now we have implemented type checking but it is not efficient and can be error prone as we have to manually check for each parameter and also it does not provide any additional features like data validation, serialization, etc. This is where Pydantic comes in handy as it provides a powerful way to define data models with type annotations and also provides data validation and serialization features out of the box.

## define a pydantic model that reprsents ideal schema of the data

#instantitate the model with data and pydantic will automatically validate the data and raise error if the data is not valid. It also provides additional features like data serialization, etc. which makes it a powerful tool for data validation and serialization in Python.

#pass the validated model object to functions 

# now
from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional,Annotated

class patient(BaseModel):
    name: Annotated[str, Field(..., description="Patient's full name")]
    email: EmailStr
    age: Annotated[int, Field(..., gt=0, description="Age must be a positive integer", strict=True)]#strict=True prevents type cobersion
    allergies: Optional[List[str]]=None
    contact_info: Dict[str, str]

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
insert_patient_data___(patient(**patient_info)) 






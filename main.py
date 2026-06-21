from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse
import json
app = FastAPI()
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully-featured Patient Management System API built with FastAPI"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/view/{patient_id}") # path parameter
def view_patient(patient_id: str=Path(...,description='ID of the patient in the DB',example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

# endpoints to sort patients
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Field to sort by", example="name"), order: str = Query("asc", description="Order of sorting", example="asc")):
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")


    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Valid orders are: asc, desc")
    
    data = load_data()
    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse=(order=='desc'))
    return sorted_data

## POST REQUEST 

##REQUEST BODY
## A request body is a part of an HTTP request that contains data sent by the client to the server. It is typically used in POST, PUT, and PATCH requests to send data to the server for processing. The request body can contain various types of data, such as JSON, XML, form data, or binary data, depending on the content type specified in the request headers. The server processes the request body and performs actions based on the received data, such as creating a new resource, updating an existing resource, or performing some other operation.

# client sends data / validate/ then append


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Unique identifier for the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient resides")]
    age: Annotated[int, Field(...,gt=0, description="Age of the patient")]
    gender: Annotated[Literal["Male", "Female", "Other"], Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., description="Height of the patient")]
    weight: Annotated[float, Field(..., description="Weight of the patient")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight / (self.height ** 2), 2)
        return bmi
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
        
@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)
    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully" })
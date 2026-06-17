from fastapi import FastAPI,Path,HTTPException,Query
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
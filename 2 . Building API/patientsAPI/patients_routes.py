from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from models import Patient, PatientUpdate
import json

patients_router = APIRouter()


def load_data():
    with open("Patients.json", "r") as file:
        data = json.load(file)
        return data


def save_data(data):
    with open("Patients.json", "w") as file:
        json.dump(data, file, indent=4)


@patients_router.get("/view")
def get_patients():

    data = load_data()  # dictionary
    patients_list = []  # list of dictionaries
    for key, val in data.items():
        patient_obj = {
            "id": key,
            **val,
        }  # {id : P001, name : Anish Bharti, age : 22, weight : 72.5, height : 1.75, city : Kolkata}
        patients_list.append(Patient(**patient_obj).model_dump())
    return JSONResponse(
        status_code=200,
        content={"message": "Patients fetched successfully", "data": patients_list},
    )


# get a patient by id -- >   path parameter


@patients_router.get("/view/{id}")
def get_patient_by_id(
    id: str = Path(..., description="The ID of the patient", example="P001")
):
    data = load_data()
    patient = data.get(id)

    if patient:
        patient_obj = {"id": id, **patient}
        patient_obj = Patient(
            **patient_obj
        ).model_dump()  # validated and converted to dictionary
        return JSONResponse(
            status_code=200,
            content={"message": "Patient fetched successfully", "data": patient_obj},
        )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "message": "Patient not found",
            },
        )


# search patients sort by name -->  query parameter
@patients_router.get("/search")
def search_patients_by_name(
    name: str = Query(
        ..., description="The name of the patient to search", example="Anish Bharti"
    )
):

    data = load_data()

    print(data)

    searched_patients_list = []

    for id, value in data.items():
        if name.lower() in value["name"].lower():
            patient_obj = {"id": id, **value}
            patient_obj = Patient(
                **patient_obj
            ).model_dump()  ## validated and converted to dictionary
            searched_patients_list.append(patient_obj)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patients fetched successfully",
            "data": searched_patients_list,
        },
    )


# add a new patient ==> POST request ==> body parameter
@patients_router.post("/patients")
def add_new_patient(
    patient: Patient,
):  ## auto signifies patienst will come via body of the request
    data = load_data()

    if patient.id in data:
        return JSONResponse(
            status_code=400,
            content={"message": "Patient already exists"},
        )

    data[patient.id] = patient.model_dump(exclude={"id"})

    save_data(data)

    return JSONResponse(
        status_code=201,
        content={"message": "Patient added successfully"},
    )


# updated a patient ==> PATCH request ==> request body
@patients_router.patch("/patients/{id}")
def update_patient(
    update_data: PatientUpdate,
    id: str = Path(..., description="The ID of the patient", example="P001"),
):

    ## print the request body
    print(update_data)
    data = load_data()

    if id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing_patient_info = data[id]  #  form json file to dictionary

    updates = update_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        existing_patient_info[key] = value  # update the existing patient information

    print(existing_patient_info)

    # for computing the prop we need to use pydantic model
    exsisting_patient_info_obj = Patient(**existing_patient_info, id=id)
    data[id] = exsisting_patient_info_obj.model_dump(exclude={"id"})

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={"message": "Patient updated successfully"},
    )


# delete a patient ==> DELETE request ==> path parameter
@patients_router.delete("/patients/{id}")
def delete_patient(
    id: str = Path(..., description="The ID of the patient", example="P001"),
):
    data = load_data()

    if id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[id]

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient deleted successfully",
            "deleted_id": id,
        },
    )

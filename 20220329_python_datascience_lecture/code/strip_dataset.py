from pathlib import Path
import pandas as pd

PROJECT_PATH = Path(__file__).parents[1]
DATA_PATH = Path(PROJECT_PATH, "data", "raw")

aps_var = pd.read_csv(Path(DATA_PATH, "apacheApsVar.csv"))
aps_input = aps_var.iloc[:, 1:]
aps_input.to_csv(Path(PROJECT_PATH, "data", "processed", "aps_input.csv"), index=False)

pred_var = pd.read_csv(Path(DATA_PATH, "apachePredVar.csv"))
pred_var_target_col = [
    "patientunitstayid",
    "gender",
    "age",
    "admitdiagnosis",
    "aids",
    "hepaticfailure",
    "lymphoma",
    "metastaticcancer",
    "leukemia",
    "immunosuppression",
    "cirrhosis",
    "electivesurgery",
    "activetx",
    "readmit",
    "diabetes",
]
other_input = pred_var[pred_var_target_col]
other_input.to_csv(
    Path(PROJECT_PATH, "data", "processed", "other_input.csv"), index=False
)

patient_result = pd.read_csv(Path(DATA_PATH, "apachePatientResult.csv"))
patient_result_target_cols = [
    "patientunitstayid",
    "physicianspeciality",
    "physicianinterventioncategory",
    "acutephysiologyscore",
    "apachescore",
    "apacheversion",
    "actualicumortality",
]
outcomes = patient_result[
    [
        "patientunitstayid",
        "actualicumortality",
        "actualhospitalmortality",
        "actualhospitallos",
    ]
]
outcomes.to_csv(Path(PROJECT_PATH, "data", "processed", "outcomes.csv"), index=False)

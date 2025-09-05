# API_Accident.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Cargar modelo
model = joblib.load('best_model.pkl')

# 2. Variables de entrada (nombres válidos)
FEATURES = [
    "traffic_control_device", "lighting_condition", "first_crash_type",
    "trafficway_type", "roadway_surface_cond", "crash_type",
    "intersection_related_i", "prim_contributory_cause", "num_units",
    "crash_hour", "crash_day_of_week", "crash_month",
    "road_defect_OTHER", "road_defect_UNKNOWN", "road_defect_WORN_SURFACE",
    "weather_condition_CLEAR", "weather_condition_CLOUDY_OVERCAST",
    "weather_condition_FOG_SMOKE_HAZE", "weather_condition_FREEZING_RAIN_DRIZZLE",
    "weather_condition_OTHER", "weather_condition_RAIN", "weather_condition_SLEET_HAIL",
    "weather_condition_SNOW", "weather_condition_UNKNOWN",
    "crash_hour_sin", "crash_hour_cos",
    "day_1", "day_2", "day_3", "day_4", "day_5", "day_6", "day_7"
]

# 3. Modelo de datos para la API
class CrashInput(BaseModel):
    traffic_control_device: float
    lighting_condition: float
    first_crash_type: float
    trafficway_type: float
    roadway_surface_cond: float
    crash_type: int
    intersection_related_i: int
    prim_contributory_cause: float
    num_units: int
    crash_hour: int
    crash_day_of_week: int
    crash_month: int
    road_defect_OTHER: float
    road_defect_UNKNOWN: float
    road_defect_WORN_SURFACE: float
    weather_condition_CLEAR: float
    weather_condition_CLOUDY_OVERCAST: float
    weather_condition_FOG_SMOKE_HAZE: float
    weather_condition_FREEZING_RAIN_DRIZZLE: float
    weather_condition_OTHER: float
    weather_condition_RAIN: float
    weather_condition_SLEET_HAIL: float
    weather_condition_SNOW: float
    weather_condition_UNKNOWN: float
    crash_hour_sin: float
    crash_hour_cos: float
    day_1: bool
    day_2: bool
    day_3: bool
    day_4: bool
    day_5: bool
    day_6: bool
    day_7: bool

# 4. Crear la API
app = FastAPI(title="Crash Injury Severity API")    

@app.get("/")
def home():
    return {"message": "Bienvenido a la API de predicción de severidad de accidentes 🚗💥"}

@app.post("/predict")
def predict_severity(data: CrashInput):
    # Convertir input en vector ordenado
    input_data = np.array([[getattr(data, f) for f in FEATURES]])
    
    # Predicción
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]
    
    return {
        "prediction": int(prediction),  # 0 = leve, 1 = grave
        "probabilidad_grave": float(proba)
    }

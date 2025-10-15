from fastapi import APIRouter

router = APIRouter()

@router.get("/workouts")
def get_workouts():
    return {"message": "List of workouts"}

@router.post("/workouts")
def create_workout(workout: dict):
    return {"message": "Workout created", "workout": workout}

@router.get("/workouts/{workout_id}")
def get_workout(workout_id: int):
    return {"message": "Details of workout", "workout_id": workout_id}

@router.put("/workouts/{workout_id}")
def update_workout(workout_id: int, workout: dict):
    return {"message": "Workout updated", "workout_id": workout_id, "workout": workout}

@router.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    return {"message": "Workout deleted", "workout_id": workout_id}
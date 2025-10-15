# Contenido del archivo: /octofit-tracker/octofit_tracker/services/tracker.py

class TrackerService:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def get_workouts(self):
        return self.workouts

    def clear_workouts(self):
        self.workouts = []
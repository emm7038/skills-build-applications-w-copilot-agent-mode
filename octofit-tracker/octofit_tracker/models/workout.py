class Workout:
    def __init__(self, name, duration, calories_burned):
        self.name = name
        self.duration = duration  # in minutes
        self.calories_burned = calories_burned

    def __str__(self):
        return f"Workout(name={self.name}, duration={self.duration}, calories_burned={self.calories_burned})"

    def get_summary(self):
        return {
            "name": self.name,
            "duration": self.duration,
            "calories_burned": self.calories_burned
        }
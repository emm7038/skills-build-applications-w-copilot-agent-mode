# tests/test_tracker.py

import unittest
from octofit_tracker.services.tracker import Tracker

class TestTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = Tracker()

    def test_add_workout(self):
        workout_data = {'type': 'running', 'duration': 30}
        self.tracker.add_workout(workout_data)
        self.assertIn(workout_data, self.tracker.workouts)

    def test_get_workouts(self):
        self.tracker.add_workout({'type': 'cycling', 'duration': 45})
        workouts = self.tracker.get_workouts()
        self.assertEqual(len(workouts), 1)

    def test_remove_workout(self):
        workout_data = {'type': 'swimming', 'duration': 60}
        self.tracker.add_workout(workout_data)
        self.tracker.remove_workout(workout_data)
        self.assertNotIn(workout_data, self.tracker.workouts)

if __name__ == '__main__':
    unittest.main()
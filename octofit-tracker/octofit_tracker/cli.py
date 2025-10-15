# Contenido del archivo /octofit-tracker/octofit-tracker/octofit_tracker/cli.py

import click
from .services.tracker import TrackerService

@click.group()
def cli():
    """Interfaz de línea de comandos para OctoFit Tracker."""
    pass

@cli.command()
@click.argument('workout_name')
def add_workout(workout_name):
    """Agregar un nuevo entrenamiento."""
    tracker_service = TrackerService()
    tracker_service.add_workout(workout_name)
    click.echo(f'Entrenamiento "{workout_name}" agregado.')

@cli.command()
def list_workouts():
    """Listar todos los entrenamientos."""
    tracker_service = TrackerService()
    workouts = tracker_service.list_workouts()
    click.echo("Entrenamientos:")
    for workout in workouts:
        click.echo(f'- {workout}')

if __name__ == '__main__':
    cli()
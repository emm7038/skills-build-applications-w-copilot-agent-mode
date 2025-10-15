# OctoFit Tracker

## Descripción del Proyecto
OctoFit Tracker es una aplicación diseñada para ayudar a los usuarios a realizar un seguimiento de sus entrenamientos y progresos. La aplicación permite registrar diferentes tipos de ejercicios, monitorear el rendimiento y analizar los datos a lo largo del tiempo.

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

```
octofit-tracker
├── octofit_tracker
│   ├── __init__.py
│   ├── cli.py
│   ├── main.py
│   ├── config.py
│   ├── models
│   │   ├── __init__.py
│   │   └── workout.py
│   ├── services
│   │   ├── __init__.py
│   │   └── tracker.py
│   └── api
│       ├── __init__.py
│       └── routes.py
├── tests
│   ├── __init__.py
│   └── test_tracker.py
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

## Instalación
Para instalar las dependencias del proyecto, asegúrate de tener Python y pip instalados en tu sistema. Luego, ejecuta el siguiente comando en la raíz del proyecto:

```
pip install -r requirements.txt
```

## Uso
Para ejecutar la aplicación, utiliza el siguiente comando:

```
python -m octofit_tracker.main
```

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT.
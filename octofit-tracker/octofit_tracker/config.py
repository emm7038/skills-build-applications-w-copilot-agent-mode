# Contenido del archivo /octofit-tracker/octofit-tracker/octofit_tracker/config.py

class Config:
    """Clase de configuración para la aplicación OctoFit Tracker."""
    
    DEBUG = True  # Habilitar el modo de depuración
    DATABASE_URI = 'sqlite:///octofit_tracker.db'  # URI de la base de datos
    SECRET_KEY = 'tu_clave_secreta_aqui'  # Clave secreta para la aplicación
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Hosts permitidos para la aplicación

    @staticmethod
    def init_app(app):
        """Método para inicializar la aplicación con la configuración."""
        pass  # Aquí se pueden agregar inicializaciones adicionales si es necesario
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

class DatabaseConnection:
    _instance = None  # Implementación del patrón Singleton

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Configura la conexión a tu base de datos MySQL
        DATABASE_URI = "mysql+pymysql://root:Alonso181437@localhost:3306/generador_nombres"
        self.engine = create_engine(DATABASE_URI, echo=True)

        # Instancia de MetaData, sin el argumento 'bind'
        self.metadata = MetaData()

        # Asignar el motor al MetaData manualmente
        self.metadata.reflect(bind=self.engine)

        # Crear una sesión para consultas
        self.Session = sessionmaker(bind=self.engine)

from sqlalchemy import create_engine

# Configuración de la conexión a la base de datos
DATABASE_URI = "mysql+pymysql://root:Alonso181437@localhost:3306/generador_nombres"

# Crear el engine
engine = create_engine(DATABASE_URI, echo=True)

from sqlalchemy import create_engine, Table, MetaData, select
from sqlalchemy.orm import scoped_session, sessionmaker

class SingletonDB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.init_db()
        return cls._instance

    def init_db(self):
        self.engine = create_engine('mysql+pymysql://root:Alonso181437@localhost:3306/generador_nombres')
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        self.categories_table = Table('categories', self.metadata, autoload_with=self.engine)
        self.prefixes_table = Table('prefixes', self.metadata, autoload_with=self.engine)
        self.suffixes_table = Table('suffixes', self.metadata, autoload_with=self.engine)

    def get_all_categories(self):
        session = self.Session()
        # Corrección aquí, usando select() correctamente
        stmt = select(self.categories_table.c.id, self.categories_table.c.category_name)  # Selección de columnas
        result = session.execute(stmt).fetchall()
        session.close()
        return result

    def generate_names_by_category(self, keyword, category_id):
        session = self.Session()
        # Consulta para obtener prefijos por categoría
        prefixes = session.execute(
            select(self.prefixes_table.c.prefix).where(self.prefixes_table.c.category_id == category_id)
        ).fetchall()
        # Consulta para obtener sufijos por categoría
        suffixes = session.execute(
            select(self.suffixes_table.c.suffix).where(self.suffixes_table.c.category_id == category_id)
        ).fetchall()
        session.close()

        # Generación de nombres
        generated_names = [f"{prefix[0]} {keyword} {suffix[0]}" for prefix in prefixes for suffix in suffixes]
        return generated_names[:50]  # Limita a 50 resultados

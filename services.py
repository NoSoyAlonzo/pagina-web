from models import Prefix, Suffix
from database import DatabaseConnection
import random

session = DatabaseConnection().Session()

def generate_business_names(category_id, num_names=50):
    """Genera nombres de empresas para una categoría específica."""
    prefixes = session.query(Prefix).filter(Prefix.category_id == category_id).all()
    suffixes = session.query(Suffix).filter(Suffix.category_id == category_id).all()

    prefix_values = [p.prefix for p in prefixes]
    suffix_values = [s.suffix for s in suffixes]
                         
    names = [
        f"{random.choice(prefix_values)} {random.choice(suffix_values)}"
        for _ in range(num_names)
    ]
    return names

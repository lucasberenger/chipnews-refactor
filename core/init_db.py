from core.database import engine
from models import user_model

def init_db():
    user_model.Base.metadata.create_all(bind=engine)
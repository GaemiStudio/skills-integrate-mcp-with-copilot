from sqlmodel import SQLModel, create_engine, Session

# SQLite file in project (for local development)
DATABASE_URL = "sqlite:///./data.db"
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    """Create database tables from SQLModel models."""
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

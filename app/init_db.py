from database import engine,Base
Base.metadata.drop_all(bind=engine)  # Drop all tables (Use cautiously)
Base.metadata.create_all(bind = engine)

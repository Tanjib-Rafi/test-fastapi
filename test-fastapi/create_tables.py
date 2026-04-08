from models.models import Base, engine

# This will create all tables defined in Base.metadata
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
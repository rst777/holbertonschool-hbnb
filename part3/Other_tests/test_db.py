from sqlalchemy import create_engine

user = "hbnb_dev"
pwd = "hbnb_dev_pwd"
host = "localhost"
db = "hbnb_dev_db"

engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")
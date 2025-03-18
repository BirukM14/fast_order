from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine = create_engine('postgresql://postgres:Bb%400939852436@localhost/postgres',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()


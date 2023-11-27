#! important !
# I don't think there is any use for it, but let it stay here
# .

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from django.conf import settings
#
#
# from sqlalchemy import Table
# from sqlalchemy.ext.declarative import declarative_base
#
#
# db = settings.DATABASES["default"]
#
# conn_str = (
#     f"postgresql+psycopg2://"
#     f'{db["USER"]}:'
#     f'{db["PASSWORD"]}'
#     f'@{db["HOST"]}:{db["PORT"]}/{db["NAME"]}'
# )
#
#
# engine = create_engine(
#     conn_str,
#     connect_args=db["OPTIONS"],
# )
#
# Base = declarative_base()
#
#
# class SA_Post(Base):
#     __table__ = Table("blog_post", Base.metadata, autoload_with=engine)
#
#
# def connect_with_sql_alchemy():
#     """
#     just prints data from db with sqlalchemy functions
#     :return:
#     """
#     with sessionmaker(engine).begin() as session:
#         rows = session.query(SA_Post)
#         for item in rows:
#             print(item.title, item.text)
#
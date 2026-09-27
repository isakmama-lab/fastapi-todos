from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# .env의 PostgreSQL 접속 정보를 읽습니다. 비밀번호에 특수문자가 있어도 안전하게 처리합니다.
if os.getenv('DB_BACKEND', 'sqlite') == 'postgresql':
    DB_URL = URL.create(
        'postgresql+psycopg',
        username=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', ''),
        host=os.getenv('DB_HOST', 'localhost'),
        port=int(os.getenv('DB_PORT', '5432')),
        database=os.getenv('DB_NAME', 'todos'),
    )
    engine = create_engine(DB_URL)
else:
    DB_URL = 'sqlite:///todo.sqlite3'
    engine = create_engine(DB_URL, connect_args={'check_same_thread': False})

# DB 연결(세션) 객체 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
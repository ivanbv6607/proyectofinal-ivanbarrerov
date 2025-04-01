from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI','postgresql://postgres:4a7DinSowBtXP6kg@db.beuliblewzcpsfbzhmls.supabase.co:5432/postgres')
                                        
    #                                    'postgresql://default.lolamzuokwevbtjjfjsr:4a7DinSowBtXP6kg@aws-0-us-east-1.pooler.supabase.com:6543/heladerias_db')
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
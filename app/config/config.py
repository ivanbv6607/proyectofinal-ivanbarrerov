from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI','postgres://postgres.lolamzuokwevbtjjfjsr:4a7DinSowBtXP6kg@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require&supa=base-pooler.x')
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
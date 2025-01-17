import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_KEY = 'alo'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/turismos'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://turismo_xc5q_user:hICCI36xWvs6i68mNbk7rt9xtTBeItfy@dpg-coptj3tjm4es73abgusg-a.ohio-postgres.render.com/turismo_xc5q'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # Inicializar la extensión SQLAlchemy






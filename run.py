from app import app, create_app
from app.config.config import Config

app = create_app(Config)

if __name__ == "__main__":
    app.run(debug=True) 
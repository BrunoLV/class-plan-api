import os

import instance.config as cfg
from src.app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run(port=cfg.FLASK_RUN_PORT)

from api import drafthouse_app
from api import markets
from api import cinemas
import os

if __name__ == '__main__':
    drafthouse_app.run(host="0.0.0.0", port=8080, debug=True)

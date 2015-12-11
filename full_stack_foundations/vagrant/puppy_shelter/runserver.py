from puppy_shelter import app
from puppy_shelter.database import init_db

if __name__ == '__main__':
    init_db()
    app.secret_key = '$up3r$3cr3tK3y'
    app.debug = True
    # Run the local server
    app.run(host='0.0.0.0', port=5000)

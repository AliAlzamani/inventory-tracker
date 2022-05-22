from app.main import app

if __name__ == "__main__":
    # import os  
    # port = int(os.environ.get('PORT', 33507))
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/test')
def test():
    return "How did you get here?"
from Udacity_Item_catalog import app

@app.route('/')
def index():
    return 'Hello world!'

from MyPlexer import MyPlexer

app = MyPlexer()


@app.route('hello')
def hello_world():
    return 'Hello, World!'


@app.route('bye')
def bye():
    return 'bye'


app.run()

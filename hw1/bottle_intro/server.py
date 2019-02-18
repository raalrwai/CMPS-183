from bottle import get, route, run, template, view, static_file

@get('/index')
def index():
    return "Welcome to CMPS 183!"


# My News web page for HW1
@get('/news')
def news():
    return template('news_template')


# Let's add some code to serve jpg images from our static images directory.
@route('/images/<filename:re:.*\.jpg>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/jpg')

# Code for serving css stylesheets from /css directory.
@route('/css/<filename:re:.*.css>')
def serve_css(filename):
    return static_file(filename, root='css', mimetype='text/css')


run(reloader=True, host='localhost', port=8080)


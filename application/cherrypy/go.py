import random
import string
import subprocess

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):

        imageFile = "test.jpg"

        output = subprocess.check_output("python pixelsort/pixelsort.py " + imageFile + " -i threshold -t 0.2 -u 0.6", stderr=subprocess.STDOUT, shell=True)

        output = output.split()[-1].strip(")")

        return output

        
    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)
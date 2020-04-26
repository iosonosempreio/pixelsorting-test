import cherrypy 
from cherrypy import tools 
#from pylab import * 
from numpy import * 
import os 
# To execute : python root.py then open your web browser at the 
# appropriate cherrypy web server port. e.g : 
# http://localhost:8080 

class Root: 
        @cherrypy.expose 
        def index(self): 
                return """<html> 
<head></head> 
<body> 
Please enter alpha value: 
<form action="visu" method="post"> 
<input type="text" name="alph" value="1.0"  /> 
</form> 
</body> 
</html> 
""" 

        @cherrypy.expose 
        def showimage(self): 
                cherrypy.response.headers['Content-Type']= "image/png" 
                f = open("sin.png", "rb") 
                contents = f.read() 
                f.close() 
                return   contents 


        @cherrypy.expose 
        def visu(self, alph = 1.0): 
                _header = """ 
                                <html> 
                                <head> 
                                <title>Random notes</<title> 
                                <link rel="stylesheet" type="text/css" href="/style.css"></link> 
                                </head> 
                                <body> 
                                <div class="container">""" 
                _footer = """ 
                                </div> 
                                </body> 
                                </html>""" 
                ioff() 
                x = arange(0, 10, 0.01) 
                alpha = eval(alph) 
                subplot(1,2,1), plot(x, sin(alpha*x), '.-') 
                subplot(1,2,2), plot(x,sin(alpha*x*cos(alpha*x)), 'o-') 
                savefig("sin.png", dpi=96) 
                cherrypy.response.headers['Content-Type']= 'text/html' 
                page = [_header] 
                page.append('<img src="/showimage/" width="800" height="400" />' ) 
                page.append(_footer) 
                return page 

if __name__ == '__main__': 
        cherrypy.quickstart(Root()) 
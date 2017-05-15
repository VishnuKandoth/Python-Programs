# importing the requests library
import requests

# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = "NTTF NEC Bangalore"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()


# extracting latitude, longitude and formatted address 
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
%(latitude, longitude,formatted_address))
Vikas • 2:44 PM
Vikas Periyadath (vikas.periyadath@tarams.com)
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

PORT_NUMBER = 8050

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

#Handler for the GET requests
def do_GET(self):
if self.path=="/":
self.path="/simple.html"

try:
#Check the file extension required and
#set the right mime type

sendReply = False
if self.path.endswith("simple.html"):
mimetype='text/html'
sendReply = True

if sendReply == True:
#Open the static file requested and send it
f = open(curdir + sep + self.path) 
self.send_response(200)
self.send_header('Content-type',mimetype)
self.end_headers()
self.wfile.write(f.read())
f.close()
return


except IOError:
self.send_error(404,'File Not Found: %s' % self.path)

try:
#Create a web server and define the handler to manage the
#incoming request
server = HTTPServer(('', PORT_NUMBER), myHandler)
print 'Started httpserver on port ' , PORT_NUMBER

#Wait forever for incoming htto requests
server.serve_forever()

except KeyboardInterrupt:
print '^C received, shutting down the web server'
server.socket.close()
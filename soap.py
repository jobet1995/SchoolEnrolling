from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class SoapService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def get(self, data):
        return "GET Response"

    @rpc(Unicode, _returns=Unicode)
    def put(self, data):
        return "PUT Response"

    @rpc(Unicode, _returns=Unicode)
    def delete(self, data):
        return "DELETE Response"

    @rpc(Unicode, _returns=Unicode)
    def post(self, data):
        return "POST Response"

soap_app = Application([SoapService], 'http://taskers-1.jobet1995.repl.co/soap-service',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

wsgi_app = WsgiApplication(soap_app)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
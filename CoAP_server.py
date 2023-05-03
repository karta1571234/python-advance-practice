from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource


class Steven(Resource):
    def __init__(self, name="Steven", coap_server=None):
        super(Steven, self).__init__(name, coap_server, visible=True,
                                     observable=True, allow_children=True)
        self.payload = "NKUST Steven Test 2020"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        return self

    def render_POST(self, request):
        res = self.init_resource(request, Steven())
        return res

    def render_DELETE(self, request):
        return True


class CoAPServer(CoAP):
    def __init__(self, host, port, multicast=False):
        CoAP.__init__(self, (host, port), multicast)
        self.add_resource('test/', Steven())
        print(("CoAP Server start on " + host + ":" + str(port)))
        print((self.root.dump()))


def main():  # pragma: no cover
    ip = "172.28.13.226"
    port = 5683
    multicast = False
    server = CoAPServer(ip, port, multicast)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == "__main__":  # pragma: no cover
    main()

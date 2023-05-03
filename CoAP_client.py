from coapthon.client.helperclient import HelperClient

host = "172.28.13.226"
port = 5683
path = "test"

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())

#response = client.get("/")
#print (response.pretty_print())

print(type(response))
client.stop()

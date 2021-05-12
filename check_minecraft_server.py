from mcstatus import MinecraftServer
import os

if 'MCS_IP_ADDRESS' not in os.environ.keys():
    print("Couldn't fetch server's IP address, please provde it before the port")
    exit()

if 'MCS_PORT' not in os.environ.keys():
    print("Couldn't fetch server's port, please provide it after the IP address")
    exit()

server = MinecraftServer(os.environ['MCS_IP_ADDRESS'], int(os.environ['MCS_PORT']))

try:
    status = server.status() 
    print("Players: {0}\nReply time: {1} ms".format(status.players.online, status.latency))
except Exception as e:
    print("Couldn't get server status, TRACE:")
    print(e)

try:
    latency = server.ping()
    print("Ping: {0} ms".format(latency))
except Exception as e:
    print("Couldn't ping server, TRACE:")
    print(e)

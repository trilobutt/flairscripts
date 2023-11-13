from pythonosc import dispatcher
from pythonosc import osc_server
import pyautogui
import os

def print_runstate(unused_addr, args):
    print("Runstate: {}".format(args))
    if args == 6:
        pyautogui.hotkey('ctrl', 't')

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/flair/runstate", print_runstate)

server = osc_server.ThreadingOSCUDPServer(("192.168.1.150", 55535), dispatcher)
print("Serving on {}".format(server.server_address))

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped.")
except Exception as e:
    print("An error occurred: ", e)

os.system('pause')

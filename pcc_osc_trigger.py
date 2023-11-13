from pythonosc import dispatcher
from pythonosc import osc_server
import pyautogui
import os

def print_runstate(unused_addr, args):
    print("Runstate: {}".format(args))
    #change the flair runstate here, depending on your shot. 
    if args == 6:
        #script only works if pcc is focused, and capture is already active. Ctrl + T is the trigger keyboard shortcut
        pyautogui.hotkey('ctrl', 't')

dispatcher = dispatcher.Dispatcher()
#you can also map to a frame number, an axis position, etc
dispatcher.map("/flair/runstate", print_runstate)

#set your ip address and port here
server = osc_server.ThreadingOSCUDPServer(("192.168.1.150", 55535), dispatcher)
print("Serving on {}".format(server.server_address))

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped.")
except Exception as e:
    print("An error occurred: ", e)
os.system('pause')

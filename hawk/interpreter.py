# hawk/interpreter.py

from .commands import log




from .commands import scan_ports

def run(command):
    if command["command"] == "scan_ports":
        scan_ports(command["args"][0])
    # داخل run():
    elif command["command"] == "log":
        log(command["args"][0])



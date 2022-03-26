import sys
import colors
from . import const
import requests

class ProcessID():
    id = None

# f = open("output.txt", "w")
def _print(text, x=0, y=0, end=""):
    # f.write(f"{x} {y} {text}{end}\n")
    # f.flush()

    # sys.stdout.write("\033[{};{}H".format(y, x))
    # sys.stdout.write("\033[K")
    dictToSend = {'message':text, "y":y, "x":x}
    res = requests.post(f'http://localhost:5000/line{ProcessID.id}', json=dictToSend)
    #print(res)
    # sys.stdout.write(f"{x} {y} {text}{end}\n")
    # sys.stdout.flush()
    pass


def print_part_status(id, text):
    #_print(colors.blue(f"[Part {id}]") + f"\t{text}", y=(id + const.CLI_STATUS_STARTLINE))
    pass


def print_captcha_status(text, parts):
    _print(colors.yellow("[Link solve]") +
           f"\t{text}", y=(parts + 0 + const.CLI_STATUS_STARTLINE))


def print_tor_status(text, parts):
    _print(colors.yellow("[Tor  start]") +
           f"\t{text}", y=(parts + 0 + const.CLI_STATUS_STARTLINE))


def print_saved_status(text, parts):
    _print(colors.yellow(f"[Progress]\t {text}"),
           y=(parts + 1 + const.CLI_STATUS_STARTLINE))

def report_saved_status(size, percent, averageSpeed, currentSpeed, remainingTime, numParts):
    print_saved_status(
        f"{size:.2f} MB"
        f" ({percent:.2f}) %"
        f"\tavg. speed: {averageSpeed:.2f} MB/s"
        f"\tcurr. speed: {currentSpeed:.2f} MB/s"
        f"\tremaining: {remainingTime}",
        numParts
    )
    dictToSend = {'totalSize':size, 'percent': percent, 'avgSpeed': averageSpeed,
                    'currSpeed': currentSpeed, 'remainingTime': remainingTime}
    res = requests.post(f'http://localhost:5000/status{ProcessID.id}', json=dictToSend)


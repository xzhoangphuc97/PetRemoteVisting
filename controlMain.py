from controlVolume import volume
from controlBrightness import setbrightness
from screenSaver import setTimeOff,onScreen
from mouseClick import clickRight

def controlMain(topic, value):
    if(topic == "devc_control_vol"):
        volume(value)
    if(topic == "devc_control_bright"):
        setbrightness(value)
    if topic == "meeting_yyyy":
        if value == "Start":
            clickRight()
            onScreen()
        if value == "End":
            setTimeOff()

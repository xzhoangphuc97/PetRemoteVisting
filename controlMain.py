from controlVolume import volume
from controlBrightness import setbrightness
from screenSaver import setTimeOff,onScreen
from mouseClick import clickRight,clickLeft
import parameter

Topic1 = parameter.TOPIC1
Topic2 = parameter.TOPIC2
Topic3 = parameter.TOPIC3

def controlMain(topic, value):
    if(topic == Topic1):
        volume(int(value))
    if(topic == Topic2):
        setbrightness(int(value))
    if topic == Topic3:
        if value == "Start":
            clickLeft()
            onScreen()
        if value == "End":
            setTimeOff()

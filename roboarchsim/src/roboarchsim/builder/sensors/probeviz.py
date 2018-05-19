from morse.builder.creator import SensorCreator

class Probeviz(SensorCreator):
    _classpath = "roboarchsim.sensors.probeviz.Probeviz"
    _blendname = "probeviz"

    def __init__(self, name=None):
        SensorCreator.__init__(self, name)


import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.sensor
import math
from roboarchsim.builder.sensors import perlin
# import perlin

from morse.core.services import service, async_service
from morse.core import status
from morse.helpers.components import add_data, add_property

class Probeviz(morse.core.sensor.Sensor):
    """Write here the general documentation of your sensor.
    It will appear in the generated online documentation.
    """
    _name = "Probeviz"
    _short_desc = "visualiseses probe vector"

    # define here the data fields exported by your sensor
    # format is: field name, default initial value, type, description
    add_data('probevalue', 0.0, 'int', 'random testdata')
    add_data('distance', 0.0, 'float', 'Distance from origin in meters')
    add_data('x', 0.0, 'float', 'xpos')
    add_data('y', 0.0, 'float', 'ypos')
    add_data('z', 0.0, 'float', 'zpos')
    add_data('color', 'none', 'str', 'A dummy colorimeter, for testing purposes. Default to \'none\'.')
    
    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        morse.core.sensor.Sensor.__init__(self, obj, parent)

        # Do here sensor specific initializations

        self._distance = 0 # dummy internal variable, for testing purposes

        logger.info('probeviz component initialized')
        self._step = 0
        self._pnf = perlin.PerlinNoiseFactory(1,2)
        self._pnf2 = perlin.PerlinNoiseFactory(2,2)

    @service
    def get_current_distance(self):
        """ This is a sample (blocking) service (use 'async_service' decorator
        for non-blocking ones).

        Simply returns the value of the internal counter.

        You can access it as a RPC service from clients.
        """
        logger.info("%s is %sm away" % (self.name, self.local_data['distance']))

        return self.local_data['distance']

    def default_action(self):
        """ Main loop of the sensor.

        Implements the component behaviour
        """
        self._step = self._step + 1
        import random
        # implement here the behaviour of your sensor

        # self.local_data['probevalue'] = random.randint(0, 1024)
        # self.local_data['probevalue'] = 512 + 512*self._pnf(self._step/1000)
        self.local_data['probevalue'] = 450 + 512*self._pnf2(self.position_3d.x/3, self.position_3d.y/2)

        # self.local_data['probevalue'] = self._pnf(self._step/1000)
        self.local_data['distance'] = math.sqrt(pow(self.position_3d.x, 2) + pow(self.position_3d.y, 2) + pow(self.position_3d.z, 2))
        self.local_data['x'] = self.position_3d.x 
        self.local_data['y'] = self.position_3d.y
        self.local_data['z'] = self.position_3d.z
        # our test sensor sees a random color
        self.local_data['color'] = random.choice(["blue", "red", "green", "yellow"])

    def reset_step(self):
        self._step = 0;

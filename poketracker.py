import sys
import os
import logging

# add directory of the pgoapi to PATH so it will be found
sys.path.append(os.path.normpath(os.path.join(os.path.realpath(__file__), '..', '.\\pgoapi')))
from pgoapi.utilities import f2i

class PokeTracker:
    def __init__(self):
        self.log = logging.getLogger(__name__)

        self._pb_api_key = ''

        self._position_lat = 0
        self._position_lng = 0
        self._position_alt = 0

    def set_pos(self, lat, lng, alt):
        self._position_lat = f2i(lat)
        self._position_lng = f2i(lng)
        self._position_alt = f2i(alt)

    def get_pos(self):
        return (self._position_lat, self._position_lng, self._position_alt)

    def main_loop(self):
        # Get map 
        # Check map for pokemon
        # Drop pokemon we don't care about
        # Notify
        # Check for incoming info

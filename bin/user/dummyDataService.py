import weewx
from weewx.engine import StdService
import logging

log = logging.getLogger(__name__)

class PrintPacket(StdService):

    def __init__(self, engine, config_dict):

      # Initialize my superclass first:
      super(PrintPacket, self).__init__(engine, config_dict)

      # Bind to any new archive record events:
      self.bind(weewx.NEW_ARCHIVE_RECORD, self.new_archive_record)

    def new_archive_record(self, event):

        wspacket = {'batteryStatus1': 0}
        log.debug("ws3000 data:" + str(wspacket))
        for key in wspacket.keys():
            event.record[key] = wspacket[key]

        log.debug("Dummy data service - printing archive record")
        log.debug(event.record)

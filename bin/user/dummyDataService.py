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

        log.debug(event.record)
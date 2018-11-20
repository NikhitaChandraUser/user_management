import logging

class CommunityLogging:
    def __init__(self, cmd, lvl):

        if lvl == 'WARN':
            self.level = logging.WARNING
        elif lvl == 'DEBUG':
            self.level = logging.DEBUG
        else:
            self.level = logging.INFO

        print (self.level)

        logging.basicConfig(filename=cmd+'.log', level = self.level)

    def logMessage(self,msg):
        if self.level == 10:
            logging.debug(msg)
        elif self.level == 20:
            logging.info(msg)
        else:
            logging.warning(msg)

import logging


class VideoMixControllerCls(object):
    def __init__(self):
        self.log = logging.getLogger('VideoMixController')

        self.composite_mode = None
        self.video_a = None
        self.video_b = None

        self.clear_handler = []

    def apply(self):
        self.log.info("apply %s %s %s", self.composite_mode, self.video_a, self.video_b)
        self.clear()
        pass

    def clear(self):
        self.log.info("clear")

        self.composite_mode = None
        self.video_b = None
        self.video_b = None

        for handler in self.clear_handler:
            handler()

    def register_clear_handler(self, cb):
        self.clear_handler.append(cb)

    def set_source_for_channel(self, channel, source):
        if channel == 'a':
            self.video_a = source
        elif channel == 'b':
            self.video_b = source
        else:
            raise RuntimeError('Unexpected Channel ' + channel)


VideoMixController = VideoMixControllerCls()

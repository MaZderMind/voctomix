import logging


class VideoMixControllerCls(object):
    def __init__(self):
        self.log = logging.getLogger('VideoMixController')

        self.composite_mode = None
        self._video_a = None
        self.video_b = None

        self.clear_handler = []
        self.preliminary_b_handler = []

    @property
    def video_a(self):
        return self._video_a

    @video_a.setter
    def video_a(self, video_a):
        self._video_a = video_a
        self.select_preliminary_b()

    def apply(self):
        self.log.info("apply %s %s %s", self.composite_mode, self.video_a, self.video_b)
        self.clear()

    def clear(self):
        self.log.info("clear")

        self.composite_mode = None
        self.video_b = None
        self.video_b = None
        self.call_clear_handler()

    def register_clear_handler(self, cb):
        self.clear_handler.append(cb)

    def call_clear_handler(self):
        for handler in self.clear_handler:
            handler()

    def register_preliminary_b_handler(self, cb):
        self.preliminary_b_handler.append(cb)

    def call_preliminary_b_handler(self, preliminary_b):
        for handler in self.preliminary_b_handler:
            handler(preliminary_b)

    def set_source_for_channel(self, channel, source):
        if channel == 'a':
            self.video_a = source
        elif channel == 'b':
            self.video_b = source
        else:
            raise RuntimeError('Unexpected Channel ' + channel)

    def select_preliminary_b(self):
        pass


VideoMixController = VideoMixControllerCls()

import tornado.web  # pragma: no cover
import tornado.escape  # pragma: no cover


class HomeHandler(tornado.web.RequestHandler):  # pragma: no cover
    def get(self):
        self.write("Hello World!")

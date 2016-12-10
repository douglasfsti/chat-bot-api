import tornado.ioloop
import tornado.web

from routes import urls

if __name__ == "__main__":
    try:
        print("Iniciando servidor http://localhost:8080/")
        application = tornado.web.Application(urls,
                                              autoreload=True,
                                              debug=True,
                                              compress_response=True)
        application.listen(8080)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("Parando servidor")

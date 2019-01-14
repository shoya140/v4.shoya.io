---
layout: post
title: Tornadoのデバッグモードを有効にする
categories: ['blog']
tags: ['engineering']
keywords: Tornado, debug, デバッグ, リロード
---

Tornadoには多くのWebアプリフレームワーク同様にデバックモードがある。これを有効にすることで、pythonコードの更新をサーバの再起動なしに反映させたり、ファイルのキャッシュを無効にしたり、tracebackをブラウザ上に表示したりといった機能を利用することができる。

デバッグモードを有効にするには、tornado.web.Applicationのインスタンス作成時にhandlersと一緒にdebug=Trueを付加すれば良い。

{{< highlight python >}}
app = tornado.web.Application(handlers = [(r"/",  IndexHandler)], debug = True)
{{< /highlight >}}

Applicationクラスを作る場合はsettingsにディクショナリで指定する。

{{< highlight python >}}
class Application(tornado.web.Application):
    def __init__(self):
        self.board = Board()
        handlers = [
            (r"/", IndexHander),
            (r"/socket", SocketHandler)
        ]
        settings = {"debug":options.debug}
        tornado.web.Application.__init__(self, handlers, **settings)
{{< /highlight >}}

自分は下記のようにtornado.optionsを使ってport, debugの２つをコマンドラインから入力できるようにしておき、本番環境と開発環境を簡単に切り替えられるようにしている。

{{< highlight python >}}
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)
define("debug", default=False, help="run the server in debug mode", type=bool)
.
.
.
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers = [(r"/",  IndexHandler)], debug = options.debug)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
{{< /highlight >}}

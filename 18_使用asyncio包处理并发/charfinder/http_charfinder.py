import sys
import asyncio
from aiohttp import web

from charfinder import UnicodeNameIndex

TEMPLATE_NAME = 'http_charfinder.html'
CONTENT_TYPE = 'text/html; charset=UTF-8'
SAMPLE_WORDS = ('bismillah chess cat circled Malayalam digit'
                ' Roman face Ethiopic black mark symbol dot'
                ' operator Braille hexagram').split()

ROW_TPL = '<tr><td>{code_str}</td><th>{char}</th><td>{name}</td></tr>'
LINK_TPL = '<a href="/?query={0}" title="find &quot;{0}&quot;">{0}</a>'
LINKS_HTML = ', '.join(LINK_TPL.format(word) for word in
                       sorted(SAMPLE_WORDS, key=str.upper))

index = UnicodeNameIndex()
with open(TEMPLATE_NAME) as tpl:
    template = tpl.read()
template = template.replace('{links}', LINKS_HTML)


def home(request):  # <1>一个路由处理函数，参数是一个 aiohttp.web.Request 实例。
    query = request.GET.get('query', '').strip()  # <2>获取查询字符串，去掉首尾空白。
    print('Query: {!r}'.format(query))  # <3>在服务器的控制台中记录查询。
    # <4>如果有查询字符串，从索引（index）中找到结果，使用 HTML 表格中的行渲染结果，
    # 把结果赋值给 res 变量，再把状态消息赋值给 msg 变量。
    if query:
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(**descr._asdict())
                        for descr in descriptions)
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'

    html = template.format(query=query, result=res,  # <5>渲染 HTML 页面。
                           message=msg)
    print('Sending {} results'.format(len(descriptions)))  # <6>在服务器的控制台中记录响应。
    return web.Response(content_type=CONTENT_TYPE, text=html)  # <7>构建 Response 对象，将其返回。


async def init(loop, address, port):  # <1>init 协程产出一个服务器，交给事件循环驱动。
    app = web.Application(loop=loop)  # <2>aiohttp.web.Application 类表示 Web 应用 ……
    app.router.add_route('GET', '/', home)  # <3>……通过路由器把 URL 模式映射到处理函数上；这里，把 GET /路由映射到home函数上。
    # <4>app.make_handler 方法返回一个 aiohttp.web.RequestHandler 实例，
    # 根据 app 对象设置的路由处理 HTTP 请求。
    handler = app.make_handler()
    # <5>create_server 方法创建服务器，以 handler 为协议处理程序，并把服务器绑定在指定的地址（address）和端口（port）上。
    server = await loop.create_server(handler, address, port)
    return server.sockets[0].getsockname()  # <6>返回第一个服务器套接字的地址和端口。


def main(address="127.0.0.1", port=8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port))  # <7>运行 init 函数，启动服务器，获取服务器的地址和端口。
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever()  # <8>运行事件循环；控制权在事件循环手上时，main 函数会在这里阻塞。
    except KeyboardInterrupt:  # 按CTRL-C键
        pass
    print('Server shutting down.')
    loop.close()


if __name__ == '__main__':
    main(*sys.argv[1:])

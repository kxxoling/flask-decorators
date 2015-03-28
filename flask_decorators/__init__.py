from functools import wraps
from flask import request, current_app, make_response, Response


def json_or_jsonp(func):
    """Wrap response in JSON or JSONP style"""
    @wraps(func)
    def _(*args, **kwargs):
        mimetype = 'application/javascript'
        callback = request.args.get('callback', None)
        if callback is None:
            content = func(*args, **kwargs)

        else:
            content = "%s(%s)" % (callback, func(*args, **kwargs))
        return current_app.response_class(content, mimetype=mimetype)
    return _


def add_response_headers(headers):
    """Add headers passed in to the response

    Usage:

    .. code::py

        @app.route('/')
        @add_response_headers({'X-Robots-Tag': 'noindex'})
        def not_indexed():
            # This will set ``X-Robots-Tag: noindex`` in the response headers
            return "Check my headers!"
    """

    def decorator(func):
        @wraps(func)
        def _(*args, **kwargs):
            rsp = make_response(func(*args, **kwargs))
            rsp_headers = rsp.headers
            for header, value in headers.items():
                rsp_headers[header] = value
            return rsp
        return _
    return decorator


def gen(mimetype):
    """``gen`` is a decorator factory function, you just need to set
    a mimetype before using::

        @app.route('/')
        @gen('')
        def index():
            pass

    A full demo for creating a image stream is available on
    `GitHub <https://github.com/kxxoling/flask-video-streaming>`__ .
    """
    def streaming(func, *args, **kwargs):
        @wraps(func)
        def _():
            return Response(func(*args, **kwargs),
                            mimetype=mimetype)
        return _
    return streaming

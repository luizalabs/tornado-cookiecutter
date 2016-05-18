from tornado.web import URLSpec


def unpack(first, *rest):
    return first, rest


def include(prefix, module_path):
    """ autoregister apps
        Method responsible to register apps via urls.py

        >>> urls += include(r'/foods', 'apps.foods.urls')
    """
    module = __import__(module_path, globals(), locals(), fromlist=["*"])
    urls = getattr(module, 'urls')
    final_urls = list()
    for url in urls:
        pattern = url.regex.pattern
        if pattern.startswith("/"):
            pattern = r"%s%s" % (prefix, pattern[1:])
        else:
            pattern = r"%s%s" % (prefix, pattern)
        final_urls.append(URLSpec(
            pattern, url.handler_class, kwargs=url.kwargs, name=url.name)
        )
    return final_urls

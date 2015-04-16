import json


def render(msg, fmt=u'html'):
    if fmt == u'html':
        return u"<html><head></head><body>%s</body></html>" % msg
    elif fmt == u'json':
        json.dumps({u'data': msg})

    # Do the same for other formats...
    else:
        return msg

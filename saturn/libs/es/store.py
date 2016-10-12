# -*- coding: utf-8 -*-

from saturn.settings.version import APP

SERVERS = '10.154.255.131:9200,10.154.255.242:9200,10.154.255.90:9200'


def _get_es():
    if not getattr(_get_es, '_es', None):
        from mimas.es.context import init_context
        from mimas.es import ElasticsearchEngine
        context = init_context(APP, SERVERS)
        es = ElasticsearchEngine.init_by_context(context)
        _get_es._es = es
    return _get_es._es

es = _get_es()

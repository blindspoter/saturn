# -*- coding: utf-8 -*-


def _get_es():
    try:
        if not getattr(_get_es, '_es', None):
            from mimas.es.engine import SearchEngine
            engine = SearchEngine()
            _get_es._es = engine
        return _get_es._es
    except:
        return None

es = _get_es()

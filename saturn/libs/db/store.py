# -*- coding: utf-8 -*-

from saturn.settings.version import APP


def _get_pool_store():
    if not getattr(_get_pool_store, '_store', None):
        from solar.db.store.context import init_context
        from solar.db.store import SqlStorePool
        context = init_context(APP)
        db = SqlStorePool(context, total=2)
        _get_pool_store._store = db
    return _get_pool_store._store

db = _get_pool_store()

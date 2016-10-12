# -*- coding: utf-8 -*-

from datetime import datetime

from saturn.libs.es.es import es

from .framework import BaseTestCase


class LibEsTest(BaseTestCase):
    def test_es(self):
        doc = {
            'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.now(),
        }

        result = es.add("test_index", "tweet", doc)
        self.assertEqual(True, result.get('created'))

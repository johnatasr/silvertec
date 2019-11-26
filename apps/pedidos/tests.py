from pydoc import resolve
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.pedidos.views import *


class ComputadoresUrlsTestCase(TestCase):

    def test_resolves_list_url(self):
        resolver = self.resolve_by_name('computadores')

        self.assertEqual(resolver.func.cls, computadores_viewsets)

    def test_resolves_retrieve_url(self):
        resolver = self.resolve_by_name('computadores', id=1)

        self.assertEqual(resolver.func.cls, computadores_viewsets)

    def test_resolves_url_to_list_action(self):
        resolver = self.resolve_by_name('computadores')

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])

    def test_resolves_url_to_retrieve_action(self):
        resolver = self.resolve_by_name('computadores', id=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('retrieve', resolver.func.actions['get'])

    def resolve_by_name(self, name, **kwargs):
        url = reverse(name, kwargs=kwargs)
        return resolve(url)


    def test_list_url_only_allows_get_and_post(self):
        resolver = self.resolve_by_name('computadores')

        self.assert_has_actions(['get', 'post'], resolver.func.actions)

    def test_single_url_allows_all_methods_except_post(self):

        resolver = self.resolve_by_name('computadores', id=1)

        self.assert_has_actions(['get', 'put', 'patch', 'delete'], resolver.func.actions)

    def assert_has_actions(self, allowed, actions):
        self.assertEqual(len(allowed), len(actions))

        for allows in allowed:
            self.assertIn(allows, actions)
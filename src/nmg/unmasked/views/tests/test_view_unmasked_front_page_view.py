# -*- coding: utf-8 -*-
from nmg.unmasked.views.testing import NMG_UNMASKED_VIEWS_FUNCTIONAL_TESTING
from nmg.unmasked.views.testing import NMG_UNMASKED_VIEWS_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = NMG_UNMASKED_VIEWS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_unmasked_front_page_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='unmasked-front-page-view'
        )
        self.assertTrue(view.__name__ == 'unmasked-front-page-view')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in unmasked-front-page-view'
        # )

    def test_unmasked_front_page_view_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='unmasked-front-page-view'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = NMG_UNMASKED_VIEWS_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

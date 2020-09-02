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

    def test_nmg_person_listing_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='nmg-person-listing'
        )
        self.assertTrue(view.__name__ == 'nmg-person-listing')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in nmg-person-listing'
        # )

    def test_nmg_person_listing_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='nmg-person-listing'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = NMG_UNMASKED_VIEWS_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

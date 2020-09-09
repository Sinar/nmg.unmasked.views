# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.interfaces import IVocabularyFactory

from operator import methodcaller

from nmg.unmasked.views import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NMGIssueView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('nmg_issue_view.pt')

    def contracts(self):
        """
        Return back references from source object where

        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_names = ['buyer',
                           'procuringEntity',
                           'administrativeEntity',
                           'suppliers',
                           'tenderers',
                           'funders',
                           'reviewBody',
                           'interestedParties',
                           ]

        result = []

        for attribute_name in attribute_names:

            for rel in catalog.findRelations(
                dict(to_id=intids.getId(aq_inner(source_object)),
                     from_attribute=attribute_name)
                  ):

                obj = intids.queryObject(rel.from_id)

                if obj is not None and checkPermission('zope2.View', obj):
                    result.append(obj)

        unique = list(dict.fromkeys(result))

        return unique

    def stories(self):
        """
        Return back references from issue source to issue

        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_names = ['issue']

        result = []

        for attribute_name in attribute_names:

            for rel in catalog.findRelations(
                dict(to_id=intids.getId(aq_inner(source_object)),
                     from_attribute=attribute_name)
                  ):

                obj = intids.queryObject(rel.from_id)

                if obj is not None and checkPermission('zope2.View', obj):
                    if obj.portal_type == 'Issue Source':
                        result.append(obj)

        unique = list(dict.fromkeys(result))

        sorted_effective = sorted(unique,
                                  key=methodcaller('effective'),
                                  reverse=True)
        if sorted_effective:
            return sorted_effective
        else:
            return None

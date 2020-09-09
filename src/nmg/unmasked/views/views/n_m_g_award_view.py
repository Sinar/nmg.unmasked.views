# -*- coding: utf-8 -*-

from nmg.unmasked.views import _
from Products.Five.browser import BrowserView

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.interfaces import IVocabularyFactory


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NMGAwardView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('nmg_award-view.pt')

    def stories(self):
        """
        Return back references from source object where

        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_names = ['related_awards']

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

        return unique


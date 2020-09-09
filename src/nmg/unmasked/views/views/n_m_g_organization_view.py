# -*- coding: utf-8 -*-

import popolo.contenttypes.utils as utils

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory


from nmg.unmasked.views import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NMGOrganizationView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('nmg_organization_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    def members(self):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_name = 'organization'

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                 from_attribute=attribute_name)
              ):

            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'Membership' and obj.post is None:
                    # check if person has membership
                    if obj.person:
                        result.append(obj)

        return result

    def employees(self):
        # Get relationships where person is employee of organization

        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context

        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                 from_attribute='relationship_subject')
              ):

            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                result.append(obj)

        return result



    def stories(self):
        """
        Return back references from source object where

        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_names = ['implicated', 'directly_implicated',
                           'circumstantial_implicated']

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

    def procurements(self):
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
                    if obj.portal_type == 'OCDS Release':
                        result.append(obj)

        unique = list(dict.fromkeys(result))

        return unique

    def awards(self):
        """
        Return back references from source object where

        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_names = ['suppliers',]

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

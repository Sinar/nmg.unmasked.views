# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from operator import methodcaller

from nmg.unmasked.views import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NMGProcurementView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('nmg_procurement_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    def awards(self):
        brains = self.context.getFolderContents(contentFilter={
            'portal_type': ['Award']})

        objs = []
        for obj in brains:
            objs.append(obj.getObject())

        return objs

    def directors(self, folder):

        memberships = folder.listFolderContents(contentFilter={
            'portal_type': ['Membership']})

        directors = []
        for membership in memberships:
            directors.append(membership.person.to_object)

        return directors

    def stories(self):
        """
        Return back references from stories

        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        attribute_names = ['related_releases']

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

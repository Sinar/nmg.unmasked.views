# -*- coding: utf-8 -*-

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

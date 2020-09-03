# -*- coding: utf-8 -*-

from nmg.unmasked.views import _
from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NMGPersonListing(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('nmg_person_listing.pt')

    def __call__(self):
        # Implement your own actions:
        return super(NMGPersonListing, self).__call__()

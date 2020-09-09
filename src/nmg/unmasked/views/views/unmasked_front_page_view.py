# -*- coding: utf-8 -*-

from nmg.unmasked.views import _
from Products.Five.browser import BrowserView

from operator import methodcaller

from plone import api

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class UnmaskedFrontPageView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('unmasked_front_page_view.pt')

    def stories(self):
        # 5 latest published stories
        stories = api.content.find(portal_type='Issue Source',
                                   sort_on='effective',
                                   sort_order='descending',
                                   )[:5]

        return stories

    def first_story(self):
        # 5 latest published stories
        stories = api.content.find(portal_type='Issue Source',
                                   sort_on='effective',
                                   sort_order='descending',
                                   )

        return stories[0]

    def issues(self):
        # 5 latest published stories
        issues = api.content.find(portal_type='Issue',
                                  sort_on='effective',
                                  sort_order='descending')[:3]

        return issues

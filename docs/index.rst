==================
nmg.unmasked.views
==================

Developer Documentation
=======================

This package provides custom views for Politikus data types for NMG
Unmasked site. This is documentaiton on how to modify existing views in
code and through the web.

Custom views in Plone are loaded up as page templates in this package,
and separated into two files.

- Page Template
- Python Class

The Page Template with .pt file extension provides zope page template
functionality.  Additional details on customizing page templates here:
https://training.plone.org/5/mastering-plone/zpt.html

Corresponding Python Class file with .py file extension provides
optional helper classes in python to generate content for a view in page
template.

For example:

- nmg_issue_view.pt is the page template file for an Issue
- n_m_g_issue_view.py is the python class for this view with additional
  helper code.

These are saved in:

https://github.com/Sinar/nmg.unmasked.views/tree/master/src/nmg/unmasked/views/views

Page Template
=============

*Changes to page template do not require a restart of the Zope
application server*

Page template are HTML file and can display fields and data contained in
the content or python view using TAL markup.

For example:

.. code-block:: html

    <p tal:content="context/Title>Will replace Title here with content Title</p>

For a list of fields that a content provides eg. Issue an easy way to
get this data is via API call.

https://unmasked.nation.africa/people/johnah-manjari?fullobjects=1

Via a REST API call either programmatically or via a tool such as
Advanced REST CLIENT https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo

Additional info on accessing API here https://github.com/plone/plone.restapi

For this example, we can see the field for name:

.. code-block:: javascript

    "layout": "nmg-person-view", 
    "modified": "2020-09-09T16:18:06+00:00", 
    "name": "Johnah Manjari", 

.. code-block:: html

    <h1 tal:content="context/name">Name</h1>

Will replace Name within h1 tags with Johnah Manjari


For detailed documentation on Page Templates see
https://training.plone.org/5/mastering-plone/zpt.html

Python View Class
=================

*Changes to Python code requires a restart of the application server*

The corresponding python class file can be used to provide additional
logic or queries that would not be possible within simple construct of a
page template.

For example for Persons, date of birth is stored, but not the age,
because this is something that needs to be calculated based on the
current date.

.. code-block:: python

        def calc_age(self, birthdate):
        today = date.today()
        age = today.year - birthdate.year - \
            ((today.month, today.day) < (birthdate.month, birthdate.day))

        return age

This can then be accessed in NMG Person View Template as

.. code-block:: html

    </small><span tal:on-error="nothing" tal:content="python:view.calc_age(context.birth_date)">45</span>


Additional reference here
https://training.plone.org/5/mastering-plone/dexterity_3.htmlser documentation

Jmbo Content Blocks
=========
**Jmbo Content Blocks. A content block represents part of a page, and is meant to be used together with Jmbo Composer to build up pages.**

.. figure:: https://travis-ci.org/praekelt/jmbo-contentblocks.svg?branch=develop
   :align: center
   :alt: Travis

.. contents:: Contents
    :depth: 5

Content types
-------------

ContentBlock
****

A Content Block has:

  * A rich text field (Markdown) 

  * A layout field, to enable the user to choose a template

  * An extra_classes field, to attach extra CSS classes to the containing div of the rendered item

Extra layouts
-------------

ContentBlocks are Jmbo Modelbase objects, so the normal view template is in ``templates/contentblocks/inclusion_tags/contentblock_detail.html``. It is preferable to NOT override this template, as it contains logic to delegate to different view templates.

The ContentBlock ``layout`` field provides options to render extra templates. The default is the normal ``detail`` view.

The standard detail view provides a wrapping div with the class ``contentblock-{{ object.layout }}`` and any other CSS classes that was provided in the extra_css field.

It will then render the object if the object has its layout set to ``detail``, or delegate to a different template. Example below.

Example
-------

In this example, we want to render only the title of the object as a h2 tag, nothing else.

In your project folder, create a template: ``templates/contentblocks/inclusion_tags/contentblock_title.html``: ::

    <h2>{{ object.title }}</h2>

To make this template show up as an option in the layouts, add the following to your settings.py: ::

    CONTENTBLOCKS = {
        "LAYOUTS": [
            ("title", "Title only, rendered as a H2 tag"),
        ]
    }

Following this pattern, you can create any amount of different layout templates to render in pages.

Notes
-----

Since markdown allows inline html, the options for layout can be extended to include all kinds of content.

The wrapping div will be included in all the extra templates created this way. If you want to avoid this, you can customise the contentblock_detail.html template.

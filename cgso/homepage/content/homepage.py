from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText
from plone.app.collection.interfaces import ICollection
from Products.ATContentTypes.interfaces.topic import IATTopic

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective.sliderfields.interfaces import ISliderFieldsEnabled

from cgso.homepage import MessageFactory as _


# Interface class; used to define content-type schema.

class Ihomepage(form.Schema, IImageScaleTraversable):
    """
    """
    width = schema.Int(title=_(u'Width'), default=1049)
    height = schema.Int(title=_(u'Height'), default=350)


    languageindependent('slider_items')
    slider_items = RelationList(
        title=u'Slider items',
        value_type=RelationChoice(
        source=ObjPathSourceBinder(
            object_provides=[ISliderFieldsEnabled.__identifier__]
        )
            ),
            required=True
        )

    languageindependent('news_source')
    news_source = RelationChoice(
        title=u'Source collection for news listing',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                             ICollection.__identifier__]
        ),
        required=False
    )


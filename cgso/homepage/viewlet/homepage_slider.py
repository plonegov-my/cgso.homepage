from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from cgso.homepage.content.homepage import Ihomepage
from plone.app.layout.viewlets import interfaces as manager
from cgso.homepage.interfaces import IProductSpecific

grok.templatedir('templates')


class homepage_slider(grok.Viewlet):
    grok.context(Ihomepage)
    grok.viewletmanager(manager.IBelowContentTitle)
    grok.template('homepage_slider')
    grok.layer(IProductSpecific)

    def _get_objects(self):
        if not self.context.slider_items:
            return []
        return [i.to_object for i in self.context.slider_items]

    def contents(self):
        data = []
        for obj in self._get_objects():
            if obj is None:
                continue
            title = getattr(obj, 'slider_title', None)
            if not title:
                title = obj.Title()
            description = getattr(obj, 'slider_description', None)
            if not description:
                description = obj.Description()
            scales = obj.restrictedTraverse('@@images')
            image = scales.scale('slider_image', width=self.context.width,
                                    height=self.context.height,
                                    direction='down')

            if image:
                image_url = image.url
            else:
                image_url = 'http://placehold.it/%sx%s' % (
                        self.context.width, self.context.height)

            data.append({
                'title': title,
                'description': description,
                'image_url': image_url,
                'url': obj.absolute_url(),
                'slide_css':
                    """
                height: %spx;
                width: %spx;
                background-image:url('%s');
                """ % (
                        self.context.height, self.context.width, image_url
                        )
                })
        return data

    def style(self):
        return 'height:%spx;width:%spx;' % (
            self.context.height, self.context.width)

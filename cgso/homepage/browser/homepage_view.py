from five import grok
from plone.directives import dexterity, form
from cgso.homepage.content.homepage import Ihomepage

grok.templatedir('templates')


class Index(dexterity.DisplayForm):
    grok.context(Ihomepage)
    grok.require('zope2.View')
    grok.template('homepage_view')
    grok.name('view')

    def news_items(self):
        rel = self.context.news_source
        if not rel:
            return []
        source = rel.to_object
        results = source.queryCatalog(batch=False) or []
        return [i.getObject() for i in results[:5]]

from collective.grok import gs
from cgso.homepage import MessageFactory as _

@gs.importstep(
    name=u'cgso.homepage', 
    title=_('cgso.homepage import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('cgso.homepage.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here

# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from uvc.plonedokumentation import _


class IDokumentation(model.Schema):
    """
    Artikeltyp zur Erfassung von Dokumentationen im Bereich Praevention der BG ETEM.
    """

#    model.fieldset(
#            'doku_details',
#            label=_(u'gut zu wissen'),
#            fields=('details',),
#    )

#    model.fieldset('doku_zusatzinfos',
#            label=_(u'weiss nicht jeder'),
#            fields=('zusatzinfos',),
#            )

#    model.fieldset(
#            'doku_bilder',
#            label=_(u'Bilder'),
#            fields=('titelbilder', 'bilder','nachrichtenbild','bildtitel'),
#            )

#    model.fieldset(
#            'doku_dateien_links',
#            label=_(u'Dateien/Links'),
#            fields=('dateien','links'),
#            )

    ueberschrift = schema.TextLine(title=_(u"Überschrift"),
                   description=_(u"Hier können Sie dem Dokument eine Überschrift geben und damit den Title überschrieben."),
                   required = False,)

    haupttext = RichText(
                title=_(u"wichtig zu wissen"),
                description=_(u"(grundlegende Informationen zum Thema - Haupttext)"),
                required = True,
                )

    details = RichText(
              title=_(u"gut zu wissen"),
              description=_(u"(detaillierte Informationen ergänzend zu den Grundlagen)"),
              required = False,
              )

    zusatzinfos = RichText(
              title=_(u"weiss nicht jeder"),
              description=_(u"(Interessantes und Wissenswertes, ergänzend zu den Grundlagen und Details)"),
              required = False,
              )

#    titelbilder = RelationList(title=_(u"Titelbilder"),
#                           description=_(u"(Anzeige im Kopf der Seite)"),
#                           default=[],
#                           value_type=RelationChoice(title=_(u"Titelbilder"),
#                                                     source=ObjPathSourceBinder()),
#                           required=False,)

#    bilder = RelationList(
#              title=_(u"Illustration"),
#              description=_(u"(Bilder zur Anzeige unterhalb der Inhaltstexte)"),
#              value_type=RelationChoice(title=_(u"Bilder"), 
#                                        source=ObjPathSourceBinder()),
#              required=False,
#              )

#    webcode = schema.TextLine(
#              title=_(u"Webcode"),
#              description=_(u"Der Webcode für diesen Artikel wird automatisch errechnet und angezeigt. Sie\
#                          können diesen Webcode bei Bedarf jedoch jederzeit überschreiben."),
#              required = True,
#              defaultFactory = genWebcode,
#              )

    vorgaenger = schema.TextLine(
              title=_(u"Vorgänger"),
              description=_(u"Bitte tragen Sie den Webcode des Vorgängerdokuments ein."),
              required = False,
              )

    nachfolger = schema.TextLine(
              title=_(u"Nachfolger"),
              description=_(u"Bitte tragen Sie den Webcode des Nachfolgerdokuments ein."),
              required = False,
              )

#    weiterlesen = RelationList(title=_(u"Dokumente zum Weiterlesen"),
#                           description=_(u"Bitte wählen Sie hier Dokumente aus, die Sie dem Benutzer zum\
#                                   Weiterlesen empfehlen."),
#                           default=[],
#                           value_type=RelationChoice(title=_(u"Weiterlesen"),
#                                                     source=ObjPathSourceBinder()),
#                           required=False,)

#    nachrichtenbild = RelationChoice(
#        title=_(u"Vorschaubild"),
#        description=_(u"(Anzeige in Verweisboxen oder Ordneransichten)"),
#        source=ObjPathSourceBinder(),
#        required=False,
#        )

    bildtitel = schema.TextLine(
              title=_(u"Titel des Vorschaubildes"),
              required = False,
              )

#    directivesform.widget(dateien=MultiFileFieldWidget)
#    dateien = schema.List(title=_(u'Ihre Dateien für dieses Dokument'),
#                             value_type=NamedBlobFile(),
#                             required = False,)

#    form.widget(links=DataGridFieldFactory)
#    links = schema.List(title=_(u'Ihre Links für dieses Dokument'),
#                        value_type=DictRow(title=_(u"Link"), schema=ILink),
#                        required = False,)

@implementer(IDokumentation)
class Dokumentation(Container):
    """
    """

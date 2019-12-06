# -*- coding: utf-8 -*-
from uvc.plonedokumentation.content.dokumentation import IDokumentation  # NOQA E501
from uvc.plonedokumentation.testing import UVC_PLONEDOKUMENTATION_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class DokumentationIntegrationTest(unittest.TestCase):

    layer = UVC_PLONEDOKUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_dokumentation_schema(self):
        fti = queryUtility(IDexterityFTI, name='Dokumentation')
        schema = fti.lookupSchema()
        self.assertEqual(IDokumentation, schema)

    def test_ct_dokumentation_fti(self):
        fti = queryUtility(IDexterityFTI, name='Dokumentation')
        self.assertTrue(fti)

    def test_ct_dokumentation_factory(self):
        fti = queryUtility(IDexterityFTI, name='Dokumentation')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IDokumentation.providedBy(obj),
            u'IDokumentation not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_dokumentation_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Dokumentation',
            id='dokumentation',
        )

        self.assertTrue(
            IDokumentation.providedBy(obj),
            u'IDokumentation not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('dokumentation', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('dokumentation', parent.objectIds())

    def test_ct_dokumentation_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Dokumentation')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_dokumentation_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Dokumentation')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'dokumentation_id',
            title='Dokumentation container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )

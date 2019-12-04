# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import uvc.plonedokumentation


class UvcPlonedokumentationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=uvc.plonedokumentation)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'uvc.plonedokumentation:default')


UVC_PLONEDOKUMENTATION_FIXTURE = UvcPlonedokumentationLayer()


UVC_PLONEDOKUMENTATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UVC_PLONEDOKUMENTATION_FIXTURE,),
    name='UvcPlonedokumentationLayer:IntegrationTesting',
)


UVC_PLONEDOKUMENTATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UVC_PLONEDOKUMENTATION_FIXTURE,),
    name='UvcPlonedokumentationLayer:FunctionalTesting',
)


UVC_PLONEDOKUMENTATION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UVC_PLONEDOKUMENTATION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='UvcPlonedokumentationLayer:AcceptanceTesting',
)

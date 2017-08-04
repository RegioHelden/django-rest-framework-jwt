`REST framework JWT Auth (FORK)`_
=================================

Added a possibility to use custom `User` model. So that it is possible have several `User` models at the same project and keep authentication flow separately from each other.

Recipe
------

1. Extend ```rest_framework_jwt.authentication.JSONWebTokenAuthentication``` and define which user model it should use.

   .. code:: python

      from rest_framework_jwt import authentication

      class MyJWTAuthentication(authentication.JSONWebTokenAuthentication):
          user_model = 'some_app.SomeUserModel'


2. Define views that manipulate the token and tell them which user model to use. e.g.:

   .. code:: python

       from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

       obtain_jwt_token = ObtainJSONWebToken.as_view(user_model='some_app.SomeUserModel')

       urlpatterns = router.urls + [
           url(r'^api-token-auth/', obtain_jwt_token, name='auth-jwt-get'),
       ]

3. Use your authentication class in your views.

   .. code:: python

       class TestView(ViewSet):
           authentication_classes = (MyJWTAuthentication, )


If you don't want to use default ```django.contrib.auth.authenticate``` which is using backends defined at ```settings.AUTHENTICATION_BACKENDS``` for all users, you need to write your own authentication handler and tell ```JSONWebTokenSerializer``` to use it by overriding ```JSONWebTokenSerializer.authenticate``` method.

  .. code:: python

    class MyJWTSerializer(serializers_jwt.JSONWebTokenSerializer):

        def authenticate(self, **credentials):
            return my_authenticate(**credentials)

    # your obtain token view then will look like this
    obtain_jwt_token = ObtainJSONWebToken.as_view(
        user_model='some_app.SomeUserModel',
        serializer_class=MyJWTSerializer
    )
    urlpatterns = router.urls + [
       url(r'^api-token-auth/', obtain_jwt_token, name='auth-jwt-get'),
    ]


REST framework JWT Auth
=======================

|build-status-image| |pypi-version|

**JSON Web Token Authentication support for Django REST Framework**

Full documentation for the project is available at `docs`_.

Overview
--------

This package provides `JSON Web Token Authentication`_ support for
`Django REST framework`_.

If you want to know more about JWT, check out the following resources:

-  DjangoCon 2014 - JSON Web Tokens `Video`_ \| `Slides`_
-  `Auth with JSON Web Tokens`_
-  `JWT.io`_

Requirements
------------

-  Python (2.7, 3.3, 3.4, 3.5)
-  Django (1.8, 1.9, 1.10, 1.11)
-  Django REST Framework (3.1, 3.2, 3.3, 3.4, 3.5, 3.6)

Installation
------------

Install using ``pip``\ ...

.. code:: bash

    $ pip install djangorestframework-jwt

Documentation & Support
-----------------------

Full documentation for the project is available at `docs`_.

You may also want to follow the `author`_ on Twitter.

.. _REST framework JWT Auth (FORK): https://github.com/GetBlimp/django-rest-framework-jwt
.. _docs: http://getblimp.github.io/django-rest-framework-jwt
.. _JSON Web Token Authentication: http://tools.ietf.org/html/draft-ietf-oauth-json-web-token
.. _Django REST framework: http://django-rest-framework.org/
.. _Video: https://www.youtube.com/watch?v=825hodQ61bg
.. _Slides: https://speakerdeck.com/jpadilla/djangocon-json-web-tokens
.. _Auth with JSON Web Tokens: http://jpadilla.com/post/73791304724/auth-with-json-web-tokens
.. _JWT.io: http://jwt.io/
.. _author: https://twitter.com/blimp

.. |build-status-image| image:: https://secure.travis-ci.org/GetBlimp/django-rest-framework-jwt.svg?branch=master
   :target: http://travis-ci.org/GetBlimp/django-rest-framework-jwt?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/djangorestframework-jwt.svg
   :target: https://pypi.python.org/pypi/djangorestframework-jwt

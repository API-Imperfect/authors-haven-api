import pytest
from pytest_factoryboy import register
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware

from core_apps.users.tests.factories import UserFactory

register(UserFactory)


@pytest.fixture
def normal_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_superuser=True, is_staff=True)
    return new_user


@pytest.fixture
def mock_request():
    factory = RequestFactory()
    request = factory.get("/")
    middleware = SessionMiddleware(lambda req: None)
    middleware.process_request(request)
    request.session.save()

    auth_middleware = AuthenticationMiddleware(lambda req: None)
    auth_middleware.process_request(request)

    return request

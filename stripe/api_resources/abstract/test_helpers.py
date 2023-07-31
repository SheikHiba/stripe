from __future__ import absolute_import, division, print_function

from stripe import error, util
from urllib.parse import quote_plus

from typing import Any, ClassVar, TypeVar
from typing_extensions import Protocol

from stripe.api_resources.abstract.api_resource import APIResource

T = TypeVar("T", bound=APIResource)


class APIResourceTestHelpers(Protocol[T]):
    """
    The base type for the TestHelper nested classes.
    Handles request URL generation for test_helper custom methods.
    Should be used in combination with the @test_helpers decorator.

    @test_helpers
    class Foo(APIResource):
      class TestHelpers(APIResourceTestHelpers):
    """

    _resource_cls: ClassVar[Any] = None
    resource: T

    def __init__(self, resource):
        self.resource = resource

    @classmethod
    def _static_request(cls, *args, **kwargs):
        return cls._resource_cls._static_request(*args, **kwargs)

    @classmethod
    def _static_request_stream(cls, *args, **kwargs):
        return cls._resource_cls._static_request_stream(*args, **kwargs)

    @classmethod
    def class_url(cls):
        if cls == APIResourceTestHelpers:
            raise NotImplementedError(
                "APIResourceTestHelpers is an abstract class.  You should perform "
                "actions on its subclasses (e.g. Charge, Customer)"
            )
        # Namespaces are separated in object names with periods (.) and in URLs
        # with forward slashes (/), so replace the former with the latter.
        base = cls._resource_cls.OBJECT_NAME.replace(".", "/")  # type: ignore
        return "/v1/test_helpers/%ss" % (base,)

    def instance_url(self):
        id = getattr(self.resource, "id", None)

        if not isinstance(id, str):
            raise error.InvalidRequestError(
                "Could not determine which URL to request: %s instance "
                "has invalid ID: %r, %s. ID should be of type `str` (or"
                " `unicode`)" % (type(self).__name__, id, type(id)),
                "id",
            )

        id = util.utf8(id)
        base = self.class_url()
        extn = quote_plus(id)
        return "%s/%s" % (base, extn)


# TODO (next major)
def test_helpers(cls):
    """
    The test_helpers decorator is deprecated and will be removed in a future version
    of the library.
    """

    def test_helpers_getter(self):
        return self.TestHelpers(self)

    if not issubclass(cls, APIResource):
        raise ValueError(
            "Could not apply @test_helpers decorator to %r."
            " The class should a subclass of APIResource." % cls
        )

    cls.TestHelpers._resource_cls = cls  # type: ignore
    cls.TestHelpers._static_request = cls._static_request  # type: ignore
    cls.TestHelpers._static_request_stream = cls._static_request_stream  # type: ignore

    cls.test_helpers = property(test_helpers_getter)  # type: ignore
    return cls

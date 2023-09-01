# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from typing import Any
from typing import Dict
from typing import Optional
from typing_extensions import Literal


class FileLink(
    CreateableAPIResource["FileLink"],
    ListableAPIResource["FileLink"],
    UpdateableAPIResource["FileLink"],
):
    """
    To share the contents of a `File` object with non-Stripe users, you can
    create a `FileLink`. `FileLink`s contain a URL that can be used to
    retrieve the contents of the file without authentication.
    """

    OBJECT_NAME = "file_link"
    created: str
    expired: bool
    expires_at: Optional[str]
    file: Any
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["file_link"]
    url: Optional[str]

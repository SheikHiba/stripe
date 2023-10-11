# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.billing_portal.configuration import Configuration


class Session(CreateableAPIResource["Session"]):
    """
    The Billing customer portal is a Stripe-hosted UI for subscription and
    billing management.

    A portal configuration describes the functionality and features that you
    want to provide to your customers through the portal.

    A portal session describes the instantiation of the customer portal for
    a particular customer. By visiting the session's URL, the customer
    can manage their subscriptions and billing details. For security reasons,
    sessions are short-lived and will expire if the customer does not visit the URL.
    Create sessions on-demand when customers intend to manage their subscriptions
    and billing details.

    Learn more in the [integration guide](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal).
    """

    OBJECT_NAME = "billing_portal.session"

    class CreateParams(RequestOptions):
        configuration: NotRequired[Optional[str]]
        customer: str
        expand: NotRequired[Optional[List[str]]]
        flow_data: NotRequired[Optional["Session.CreateParamsFlowData"]]
        locale: NotRequired[
            Optional[
                Literal[
                    "auto",
                    "bg",
                    "cs",
                    "da",
                    "de",
                    "el",
                    "en",
                    "en-AU",
                    "en-CA",
                    "en-GB",
                    "en-IE",
                    "en-IN",
                    "en-NZ",
                    "en-SG",
                    "es",
                    "es-419",
                    "et",
                    "fi",
                    "fil",
                    "fr",
                    "fr-CA",
                    "hr",
                    "hu",
                    "id",
                    "it",
                    "ja",
                    "ko",
                    "lt",
                    "lv",
                    "ms",
                    "mt",
                    "nb",
                    "nl",
                    "pl",
                    "pt",
                    "pt-BR",
                    "ro",
                    "ru",
                    "sk",
                    "sl",
                    "sv",
                    "th",
                    "tr",
                    "vi",
                    "zh",
                    "zh-HK",
                    "zh-TW",
                ]
            ]
        ]
        on_behalf_of: NotRequired[Optional[str]]
        return_url: NotRequired[Optional[str]]

    class CreateParamsFlowData(TypedDict):
        after_completion: NotRequired[
            Optional["Session.CreateParamsFlowDataAfterCompletion"]
        ]
        subscription_cancel: NotRequired[
            Optional["Session.CreateParamsFlowDataSubscriptionCancel"]
        ]
        subscription_update: NotRequired[
            Optional["Session.CreateParamsFlowDataSubscriptionUpdate"]
        ]
        subscription_update_confirm: NotRequired[
            Optional["Session.CreateParamsFlowDataSubscriptionUpdateConfirm"]
        ]
        type: Literal[
            "payment_method_update",
            "subscription_cancel",
            "subscription_update",
            "subscription_update_confirm",
        ]

    class CreateParamsFlowDataSubscriptionUpdateConfirm(TypedDict):
        discounts: NotRequired[
            Optional[
                List[
                    "Session.CreateParamsFlowDataSubscriptionUpdateConfirmDiscount"
                ]
            ]
        ]
        items: List[
            "Session.CreateParamsFlowDataSubscriptionUpdateConfirmItem"
        ]
        subscription: str

    class CreateParamsFlowDataSubscriptionUpdateConfirmItem(TypedDict):
        id: str
        price: NotRequired[Optional[str]]
        quantity: NotRequired[Optional[int]]

    class CreateParamsFlowDataSubscriptionUpdateConfirmDiscount(TypedDict):
        coupon: NotRequired[Optional[str]]
        promotion_code: NotRequired[Optional[str]]

    class CreateParamsFlowDataSubscriptionUpdate(TypedDict):
        subscription: str

    class CreateParamsFlowDataSubscriptionCancel(TypedDict):
        retention: NotRequired[
            Optional["Session.CreateParamsFlowDataSubscriptionCancelRetention"]
        ]
        subscription: str

    class CreateParamsFlowDataSubscriptionCancelRetention(TypedDict):
        coupon_offer: "Session.CreateParamsFlowDataSubscriptionCancelRetentionCouponOffer"
        type: Literal["coupon_offer"]

    class CreateParamsFlowDataSubscriptionCancelRetentionCouponOffer(
        TypedDict
    ):
        coupon: str

    class CreateParamsFlowDataAfterCompletion(TypedDict):
        hosted_confirmation: NotRequired[
            Optional[
                "Session.CreateParamsFlowDataAfterCompletionHostedConfirmation"
            ]
        ]
        redirect: NotRequired[
            Optional["Session.CreateParamsFlowDataAfterCompletionRedirect"]
        ]
        type: Literal["hosted_confirmation", "portal_homepage", "redirect"]

    class CreateParamsFlowDataAfterCompletionRedirect(TypedDict):
        return_url: str

    class CreateParamsFlowDataAfterCompletionHostedConfirmation(TypedDict):
        custom_message: NotRequired[Optional[str]]

    configuration: ExpandableField["Configuration"]
    created: int
    customer: str
    flow: Optional[StripeObject]
    id: str
    livemode: bool
    locale: Optional[
        Literal[
            "auto",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "en-AU",
            "en-CA",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-SG",
            "es",
            "es-419",
            "et",
            "fi",
            "fil",
            "fr",
            "fr-CA",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "lv",
            "ms",
            "mt",
            "nb",
            "nl",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "vi",
            "zh",
            "zh-HK",
            "zh-TW",
        ]
    ]
    object: Literal["billing_portal.session"]
    on_behalf_of: Optional[str]
    return_url: Optional[str]
    url: str

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Session.CreateParams"]
    ) -> "Session":
        return cast(
            "Session",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, Type, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.cash_balance import CashBalance
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_id import TaxId
    from stripe.api_resources.test_helpers.test_clock import TestClock


@nested_resource_class_methods("balance_transaction")
@nested_resource_class_methods("cash_balance_transaction")
@nested_resource_class_methods("source")
@nested_resource_class_methods("tax_id")
class Customer(
    CreateableAPIResource["Customer"],
    DeletableAPIResource["Customer"],
    ListableAPIResource["Customer"],
    SearchableAPIResource["Customer"],
    UpdateableAPIResource["Customer"],
):
    """
    This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.

    Related guide: [Save a card during payment](https://stripe.com/docs/payments/save-during-payment)
    """

    OBJECT_NAME = "customer"

    class CreateParams(RequestOptions):
        address: NotRequired[
            Optional[
                Union[Literal[""], "Customer.CreateParamsShippingAddress"]
            ]
        ]
        balance: NotRequired[Optional[int]]
        cash_balance: NotRequired[Optional["Customer.CreateParamsCashBalance"]]
        coupon: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        email: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        invoice_prefix: NotRequired[Optional[str]]
        invoice_settings: NotRequired[
            Optional["Customer.CreateParamsInvoiceSettings"]
        ]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        name: NotRequired[Optional[str]]
        next_invoice_sequence: NotRequired[Optional[int]]
        payment_method: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]
        preferred_locales: NotRequired[Optional[List[str]]]
        promotion_code: NotRequired[Optional[str]]
        shipping: NotRequired[
            Optional[Union[Literal[""], "Customer.CreateParamsShipping"]]
        ]
        source: NotRequired[Optional[str]]
        tax: NotRequired[Optional["Customer.CreateParamsTax"]]
        tax_exempt: NotRequired[
            Optional[Union[Literal[""], Literal["exempt", "none", "reverse"]]]
        ]
        tax_id_data: NotRequired[
            Optional[List["Customer.CreateParamsTaxIdDatum"]]
        ]
        test_clock: NotRequired[Optional[str]]
        validate: NotRequired[Optional[bool]]

    class CreateParamsTaxIdDatum(TypedDict):
        type: Literal[
            "ad_nrt",
            "ae_trn",
            "ar_cuit",
            "au_abn",
            "au_arn",
            "bg_uic",
            "bo_tin",
            "br_cnpj",
            "br_cpf",
            "ca_bn",
            "ca_gst_hst",
            "ca_pst_bc",
            "ca_pst_mb",
            "ca_pst_sk",
            "ca_qst",
            "ch_vat",
            "cl_tin",
            "cn_tin",
            "co_nit",
            "cr_tin",
            "do_rcn",
            "ec_ruc",
            "eg_tin",
            "es_cif",
            "eu_oss_vat",
            "eu_vat",
            "gb_vat",
            "ge_vat",
            "hk_br",
            "hu_tin",
            "id_npwp",
            "il_vat",
            "in_gst",
            "is_vat",
            "jp_cn",
            "jp_rn",
            "jp_trn",
            "ke_pin",
            "kr_brn",
            "li_uid",
            "mx_rfc",
            "my_frp",
            "my_itn",
            "my_sst",
            "no_vat",
            "nz_gst",
            "pe_ruc",
            "ph_tin",
            "ro_tin",
            "rs_pib",
            "ru_inn",
            "ru_kpp",
            "sa_vat",
            "sg_gst",
            "sg_uen",
            "si_tin",
            "sv_nit",
            "th_vat",
            "tr_tin",
            "tw_vat",
            "ua_vat",
            "us_ein",
            "uy_ruc",
            "ve_rif",
            "vn_tin",
            "za_vat",
        ]
        value: str

    class CreateParamsTax(TypedDict):
        ip_address: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateParamsShipping(TypedDict):
        address: "Customer.CreateParamsShippingAddress"
        name: str
        phone: NotRequired[Optional[str]]

    class CreateParamsShippingAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsInvoiceSettings(TypedDict):
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List["Customer.CreateParamsInvoiceSettingsCustomField"],
                ]
            ]
        ]
        default_payment_method: NotRequired[Optional[str]]
        footer: NotRequired[Optional[str]]
        rendering_options: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Customer.CreateParamsInvoiceSettingsRenderingOptions",
                ]
            ]
        ]

    class CreateParamsInvoiceSettingsRenderingOptions(TypedDict):
        amount_tax_display: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]

    class CreateParamsInvoiceSettingsCustomField(TypedDict):
        name: str
        value: str

    class CreateParamsCashBalance(TypedDict):
        settings: NotRequired[
            Optional["Customer.CreateParamsCashBalanceSettings"]
        ]

    class CreateParamsCashBalanceSettings(TypedDict):
        reconciliation_mode: NotRequired[
            Optional[Literal["automatic", "manual", "merchant_default"]]
        ]

    class CreateParamsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateFundingInstructionsParams(RequestOptions):
        bank_transfer: "Customer.CreateFundingInstructionsParamsBankTransfer"
        currency: str
        expand: NotRequired[Optional[List[str]]]
        funding_type: Literal["bank_transfer"]

    class CreateFundingInstructionsParamsBankTransfer(TypedDict):
        eu_bank_transfer: NotRequired[
            Optional[
                "Customer.CreateFundingInstructionsParamsBankTransferEuBankTransfer"
            ]
        ]
        requested_address_types: NotRequired[
            Optional[List[Literal["iban", "sort_code", "spei", "zengin"]]]
        ]
        type: Literal[
            "eu_bank_transfer",
            "gb_bank_transfer",
            "jp_bank_transfer",
            "mx_bank_transfer",
            "us_bank_transfer",
        ]

    class CreateFundingInstructionsParamsBankTransferEuBankTransfer(TypedDict):
        country: str

    class DeleteParams(RequestOptions):
        pass

    class DeleteDiscountParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["Customer.ListParamsCreated", int]]
        ]
        email: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        test_clock: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListPaymentMethodsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        type: NotRequired[
            Optional[
                Literal[
                    "acss_debit",
                    "affirm",
                    "afterpay_clearpay",
                    "alipay",
                    "au_becs_debit",
                    "bacs_debit",
                    "bancontact",
                    "blik",
                    "boleto",
                    "card",
                    "cashapp",
                    "customer_balance",
                    "eps",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "klarna",
                    "konbini",
                    "link",
                    "oxxo",
                    "p24",
                    "paynow",
                    "paypal",
                    "pix",
                    "promptpay",
                    "sepa_debit",
                    "sofort",
                    "us_bank_account",
                    "wechat_pay",
                    "zip",
                ]
            ]
        ]

    class ModifyParams(RequestOptions):
        address: NotRequired[
            Optional[
                Union[Literal[""], "Customer.ModifyParamsShippingAddress"]
            ]
        ]
        balance: NotRequired[Optional[int]]
        cash_balance: NotRequired[Optional["Customer.ModifyParamsCashBalance"]]
        coupon: NotRequired[Optional[str]]
        default_source: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        email: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        invoice_prefix: NotRequired[Optional[str]]
        invoice_settings: NotRequired[
            Optional["Customer.ModifyParamsInvoiceSettings"]
        ]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        name: NotRequired[Optional[str]]
        next_invoice_sequence: NotRequired[Optional[int]]
        phone: NotRequired[Optional[str]]
        preferred_locales: NotRequired[Optional[List[str]]]
        promotion_code: NotRequired[Optional[str]]
        shipping: NotRequired[
            Optional[Union[Literal[""], "Customer.ModifyParamsShipping"]]
        ]
        source: NotRequired[Optional[str]]
        tax: NotRequired[Optional["Customer.ModifyParamsTax"]]
        tax_exempt: NotRequired[
            Optional[Union[Literal[""], Literal["exempt", "none", "reverse"]]]
        ]
        validate: NotRequired[Optional[bool]]

    class ModifyParamsTax(TypedDict):
        ip_address: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyParamsShipping(TypedDict):
        address: "Customer.ModifyParamsShippingAddress"
        name: str
        phone: NotRequired[Optional[str]]

    class ModifyParamsShippingAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyParamsInvoiceSettings(TypedDict):
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List["Customer.ModifyParamsInvoiceSettingsCustomField"],
                ]
            ]
        ]
        default_payment_method: NotRequired[Optional[str]]
        footer: NotRequired[Optional[str]]
        rendering_options: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Customer.ModifyParamsInvoiceSettingsRenderingOptions",
                ]
            ]
        ]

    class ModifyParamsInvoiceSettingsRenderingOptions(TypedDict):
        amount_tax_display: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]

    class ModifyParamsInvoiceSettingsCustomField(TypedDict):
        name: str
        value: str

    class ModifyParamsCashBalance(TypedDict):
        settings: NotRequired[
            Optional["Customer.ModifyParamsCashBalanceSettings"]
        ]

    class ModifyParamsCashBalanceSettings(TypedDict):
        reconciliation_mode: NotRequired[
            Optional[Literal["automatic", "manual", "merchant_default"]]
        ]

    class ModifyParamsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class RetrievePaymentMethodParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SearchParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        page: NotRequired[Optional[str]]
        query: str

    class ModifyCashBalanceParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        settings: NotRequired[
            Optional["Customer.ModifyCashBalanceParamsSettings"]
        ]

    class ModifyCashBalanceParamsSettings(TypedDict):
        reconciliation_mode: NotRequired[
            Optional[Literal["automatic", "manual", "merchant_default"]]
        ]

    class RetrieveCashBalanceParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class FundCashBalanceParams(RequestOptions):
        amount: int
        currency: str
        expand: NotRequired[Optional[List[str]]]
        reference: NotRequired[Optional[str]]

    class CreateBalanceTransactionParams(RequestOptions):
        amount: int
        currency: str
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class RetrieveBalanceTransactionParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ModifyBalanceTransactionParams(RequestOptions):
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class ListBalanceTransactionsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class RetrieveCashBalanceTransactionParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ListCashBalanceTransactionsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class CreateSourceParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        source: str
        validate: NotRequired[Optional[bool]]

    class RetrieveSourceParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ModifySourceParams(RequestOptions):
        account_holder_name: NotRequired[Optional[str]]
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        address_city: NotRequired[Optional[str]]
        address_country: NotRequired[Optional[str]]
        address_line1: NotRequired[Optional[str]]
        address_line2: NotRequired[Optional[str]]
        address_state: NotRequired[Optional[str]]
        address_zip: NotRequired[Optional[str]]
        exp_month: NotRequired[Optional[str]]
        exp_year: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        name: NotRequired[Optional[str]]
        owner: NotRequired[Optional["Customer.ModifySourceParamsOwner"]]

    class ModifySourceParamsOwner(TypedDict):
        address: NotRequired[
            Optional["Customer.ModifySourceParamsOwnerAddress"]
        ]
        email: NotRequired[Optional[str]]
        name: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]

    class ModifySourceParamsOwnerAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class DeleteSourceParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ListSourcesParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        object: NotRequired[Optional[str]]
        starting_after: NotRequired[Optional[str]]

    class CreateTaxIdParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        type: Literal[
            "ad_nrt",
            "ae_trn",
            "ar_cuit",
            "au_abn",
            "au_arn",
            "bg_uic",
            "bo_tin",
            "br_cnpj",
            "br_cpf",
            "ca_bn",
            "ca_gst_hst",
            "ca_pst_bc",
            "ca_pst_mb",
            "ca_pst_sk",
            "ca_qst",
            "ch_vat",
            "cl_tin",
            "cn_tin",
            "co_nit",
            "cr_tin",
            "do_rcn",
            "ec_ruc",
            "eg_tin",
            "es_cif",
            "eu_oss_vat",
            "eu_vat",
            "gb_vat",
            "ge_vat",
            "hk_br",
            "hu_tin",
            "id_npwp",
            "il_vat",
            "in_gst",
            "is_vat",
            "jp_cn",
            "jp_rn",
            "jp_trn",
            "ke_pin",
            "kr_brn",
            "li_uid",
            "mx_rfc",
            "my_frp",
            "my_itn",
            "my_sst",
            "no_vat",
            "nz_gst",
            "pe_ruc",
            "ph_tin",
            "ro_tin",
            "rs_pib",
            "ru_inn",
            "ru_kpp",
            "sa_vat",
            "sg_gst",
            "sg_uen",
            "si_tin",
            "sv_nit",
            "th_vat",
            "tr_tin",
            "tw_vat",
            "ua_vat",
            "us_ein",
            "uy_ruc",
            "ve_rif",
            "vn_tin",
            "za_vat",
        ]
        value: str

    class RetrieveTaxIdParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class DeleteTaxIdParams(RequestOptions):
        pass

    class ListTaxIdsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    address: Optional[StripeObject]
    balance: Optional[int]
    cash_balance: Optional["CashBalance"]
    created: int
    currency: Optional[str]
    default_source: Optional[ExpandableField[Any]]
    delinquent: Optional[bool]
    description: Optional[str]
    discount: Optional["Discount"]
    email: Optional[str]
    id: str
    invoice_credit_balance: Optional[Dict[str, int]]
    invoice_prefix: Optional[str]
    invoice_settings: Optional[StripeObject]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    name: Optional[str]
    next_invoice_sequence: Optional[int]
    object: Literal["customer"]
    phone: Optional[str]
    preferred_locales: Optional[List[str]]
    shipping: Optional[StripeObject]
    sources: Optional[ListObject[Any]]
    subscriptions: Optional[ListObject["Subscription"]]
    tax: Optional[StripeObject]
    tax_exempt: Optional[Literal["exempt", "none", "reverse"]]
    tax_ids: Optional[ListObject["TaxId"]]
    test_clock: Optional[ExpandableField["TestClock"]]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateParams"]
    ) -> "Customer":
        return cast(
            "Customer",
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

    @classmethod
    def _cls_create_funding_instructions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateFundingInstructionsParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/funding_instructions".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_create_funding_instructions")
    def create_funding_instructions(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.CreateFundingInstructionsParams"]
    ):
        return self._request(
            "post",
            "/v1/customers/{customer}/funding_instructions".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["Customer.DeleteParams"]
    ) -> "Customer":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Customer",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Customer.DeleteParams"]) -> "Customer":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def _cls_delete_discount(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.DeleteDiscountParams"]
    ):
        return cls._static_request(
            "delete",
            "/v1/customers/{customer}/discount".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_delete_discount")
    def delete_discount(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.DeleteDiscountParams"]
    ):
        return self._request(
            "delete",
            "/v1/customers/{customer}/discount".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListParams"]
    ) -> ListObject["Customer"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_payment_methods(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListPaymentMethodsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/payment_methods".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_payment_methods")
    def list_payment_methods(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.ListPaymentMethodsParams"]
    ):
        return self._request(
            "get",
            "/v1/customers/{customer}/payment_methods".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(
        cls, id, **params: Unpack["Customer.ModifyParams"]
    ) -> "Customer":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Customer",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Customer.RetrieveParams"]
    ) -> "Customer":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_retrieve_payment_method(
        cls,
        customer: str,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrievePaymentMethodParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/payment_methods/{payment_method}".format(
                customer=util.sanitize_id(customer),
                payment_method=util.sanitize_id(payment_method),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_retrieve_payment_method")
    def retrieve_payment_method(
        self,
        payment_method: str,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.RetrievePaymentMethodParams"]
    ):
        return self._request(
            "get",
            "/v1/customers/{customer}/payment_methods/{payment_method}".format(
                customer=util.sanitize_id(self.get("id")),
                payment_method=util.sanitize_id(payment_method),
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Customer.SearchParams"]
    ) -> SearchResultObject["Customer"]:
        return cls._search(search_url="/v1/customers/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    @classmethod
    def create_balance_transaction(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateBalanceTransactionParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/balance_transactions".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveBalanceTransactionParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/balance_transactions/{transaction}".format(
                customer=util.sanitize_id(customer),
                transaction=util.sanitize_id(transaction),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ModifyBalanceTransactionParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/balance_transactions/{transaction}".format(
                customer=util.sanitize_id(customer),
                transaction=util.sanitize_id(transaction),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_balance_transactions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListBalanceTransactionsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/balance_transactions".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_cash_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveCashBalanceTransactionParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/cash_balance_transactions/{transaction}".format(
                customer=util.sanitize_id(customer),
                transaction=util.sanitize_id(transaction),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_cash_balance_transactions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListCashBalanceTransactionsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/cash_balance_transactions".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_source(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateSourceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/sources".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveSourceParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/sources/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ModifySourceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/sources/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def delete_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.DeleteSourceParams"]
    ):
        return cls._static_request(
            "delete",
            "/v1/customers/{customer}/sources/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_sources(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListSourcesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/sources".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_tax_id(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateTaxIdParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/tax_ids".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_tax_id(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveTaxIdParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/tax_ids/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def delete_tax_id(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.DeleteTaxIdParams"]
    ):
        return cls._static_request(
            "delete",
            "/v1/customers/{customer}/tax_ids/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_tax_ids(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListTaxIdsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/tax_ids".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_cash_balance(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ModifyCashBalanceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/cash_balance".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_cash_balance(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveCashBalanceParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/cash_balance".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    class TestHelpers(APIResourceTestHelpers["Customer"]):
        _resource_cls: Type["Customer"]

        @classmethod
        def _cls_fund_cash_balance(
            cls,
            customer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Customer.FundCashBalanceParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_fund_cash_balance")
        def fund_cash_balance(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Customer.FundCashBalanceParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
                    customer=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


Customer.TestHelpers._resource_cls = Customer

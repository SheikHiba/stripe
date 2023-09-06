# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice_line_item import InvoiceLineItem


class QuotePreviewInvoice(ListableAPIResource["QuotePreviewInvoice"]):
    """
    Invoices are statements of amounts owed by a customer, and are either
    generated one-off, or generated periodically from a subscription.

    They contain [invoice items](https://stripe.com/docs/api#invoiceitems), and proration adjustments
    that may be caused by subscription upgrades/downgrades (if necessary).

    If your invoice is configured to be billed through automatic charges,
    Stripe automatically finalizes your invoice and attempts payment. Note
    that finalizing the invoice,
    [when automatic](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection), does
    not happen immediately as the invoice is created. Stripe waits
    until one hour after the last webhook was successfully sent (or the last
    webhook timed out after failing). If you (and the platforms you may have
    connected to) have no webhooks configured, Stripe waits one hour after
    creation to finalize the invoice.

    If your invoice is configured to be billed by sending an email, then based on your
    [email settings](https://dashboard.stripe.com/account/billing/automatic),
    Stripe will email the invoice to your customer and await payment. These
    emails can contain a link to a hosted page to pay the invoice.

    Stripe applies any customer credit on the account before determining the
    amount due for the invoice (i.e., the amount that will be actually
    charged). If the amount due for the invoice is less than Stripe's [minimum allowed charge
    per currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts), the
    invoice is automatically marked paid, and we add the amount due to the
    customer's credit balance which is applied to the next invoice.

    More details on the customer's credit balance are
    [here](https://stripe.com/docs/billing/customer/balance).

    Related guide: [Send invoices to customers](https://stripe.com/docs/billing/invoices/sending)
    """

    OBJECT_NAME = "quote_preview_invoice"
    account_country: Optional[str]
    account_name: Optional[str]
    account_tax_ids: Optional[List[Any]]
    amount_due: int
    amount_paid: int
    amount_remaining: int
    amount_shipping: int
    application: Optional[Any]
    application_fee_amount: Optional[int]
    applies_to: StripeObject
    attempt_count: int
    attempted: bool
    automatic_tax: StripeObject
    billing_reason: Optional[str]
    collection_method: str
    created: str
    currency: str
    custom_fields: Optional[List[StripeObject]]
    customer_address: Optional[StripeObject]
    customer_email: Optional[str]
    customer_name: Optional[str]
    customer_phone: Optional[str]
    customer_shipping: Optional[StripeObject]
    customer_tax_exempt: Optional[str]
    customer_tax_ids: Optional[List[StripeObject]]
    default_payment_method: Optional[Any]
    default_source: Optional[Any]
    default_tax_rates: List["TaxRate"]
    description: Optional[str]
    discount: Optional["Discount"]
    discounts: Optional[List[Any]]
    due_date: Optional[str]
    effective_at: Optional[str]
    ending_balance: Optional[int]
    footer: Optional[str]
    from_invoice: Optional[StripeObject]
    id: str
    last_finalization_error: Optional[StripeObject]
    latest_revision: Optional[Any]
    lines: ListObject["InvoiceLineItem"]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    next_payment_attempt: Optional[str]
    number: Optional[str]
    object: Literal["quote_preview_invoice"]
    on_behalf_of: Optional[Any]
    paid: bool
    paid_out_of_band: bool
    payment_intent: Optional[Any]
    payment_settings: StripeObject
    period_end: str
    period_start: str
    post_payment_credit_notes_amount: int
    pre_payment_credit_notes_amount: int
    quote: Optional[Any]
    receipt_number: Optional[str]
    rendering_options: Optional[StripeObject]
    shipping_cost: Optional[StripeObject]
    shipping_details: Optional[StripeObject]
    starting_balance: int
    statement_descriptor: Optional[str]
    status: Optional[str]
    status_transitions: StripeObject
    subscription: Optional[Any]
    subscription_details: Optional[StripeObject]
    subscription_proration_date: int
    subtotal: int
    subtotal_excluding_tax: Optional[int]
    tax: Optional[int]
    test_clock: Optional[Any]
    threshold_reason: StripeObject
    total: int
    total_discount_amounts: Optional[List[StripeObject]]
    total_excluding_tax: Optional[int]
    total_tax_amounts: List[StripeObject]
    transfer_data: Optional[StripeObject]
    webhooks_delivered_at: Optional[str]

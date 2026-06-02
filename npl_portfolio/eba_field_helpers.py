# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions, and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

"""
EBA field help-text helpers.

Usage in model field definitions:

    from npl_portfolio.eba_field_helpers import eba_help, deprecated_help

    # In Force field — links to the exact point in EUR-Lex via Text Fragment
    counterparty_identifier = models.TextField(
        blank=True, null=True,
        help_text=eba_help('1.02', 'Unique internal identifier for each counterparty.'),
    )

    # Deprecated field — no EBA ITS reference, openNPL-specific addition
    borrower_type = models.IntegerField(
        blank=True, null=True,
        help_text=deprecated_help(
            'Classification of the borrower as Private Individual or Corporate.',
            reason='No direct EBA ITS 2023/2083 field. Borrower type is derived from '
                   'Legal Type of Counterparty (field 1.06).',
        ),
    )
"""

_EURLEX_BASE = (
    'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/'
    '?uri=CELEX:32023R2083'
)


def eba_help(ref: str, description: str) -> str:
    """
    Generate help_text for an In Force EBA ITS 2023/2083 field.

    Renders a § reference that deep-links to the exact field in EUR-Lex
    using a Text Fragment (supported by Chrome, Edge, Safari 16.4+).

    Args:
        ref:         EBA field reference, dot-notation (e.g. '1.02', '4.43').
        description: Plain-text field description shown below the input.
    """
    fragment = ref.replace('.', '%2C')
    url = f'{_EURLEX_BASE}#:~:text={fragment}'
    badge = (
        f'<a href="{url}" target="_blank" rel="noopener noreferrer" '
        f'title="EU 2023/2083 — EBA NPL ITS field {ref}" '
        f'style="color:#1a5276; font-weight:600; margin-left:6px; '
        f'text-decoration:none; font-size:12px;">§ {ref}</a>'
    )
    return f'{description}{badge}'


def legacy_help(description: str, prior_ref: str = '') -> str:
    """
    Generate help_text for a Legacy field.

    Legacy fields existed in a pre-2023 EBA NPL draft template but were
    not included in the adopted Commission Implementing Regulation (EU) 2023/2083.
    They are retained in openNPL for historical data compatibility.

    Args:
        description: Original field description.
        prior_ref:   Optional reference to the prior EBA draft (e.g. 'EBA draft 2018 T1.xx').
    """
    note = f' Prior ref: {prior_ref}.' if prior_ref else ''
    return (
        f'<span style="color:#a0a000;">'
        f'📦 <strong>LEGACY</strong> — Not in EU 2023/2083.{note}'
        f'</span>'
        f'<br><span style="color:#888;">{description}</span>'
    )


def deprecated_help(description: str, reason: str) -> str:
    """
    Generate help_text for a Deprecated field.

    Deprecated fields exist in the openNPL model but have no EBA origin —
    they were added by openNPL for implementation convenience and have no
    counterpart in any version of the EBA NPL ITS.

    Args:
        description: Original field description.
        reason:      Why the field is deprecated (e.g. no EBA ref, superseded by).
    """
    return (
        f'<span style="color:#e07b39;">'
        f'🚫 <strong>DEPRECATED</strong> — {reason}'
        f'</span>'
        f'<br><span style="color:#888;">{description}</span>'
    )

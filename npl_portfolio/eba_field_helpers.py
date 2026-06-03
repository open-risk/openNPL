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

Field classification (EU 2023/2083 — EBA NPL ITS):

    MANDATORY    (~76 fields)  — EBA ITS mandatory fields. Red label.
    RECOMMENDED  (~64 fields)  — EBA ITS recommended fields. Orange label.
    LEGACY       (remaining)   — Pre-2023 EBA draft fields, not in final ITS.
                                 Kept for internal portfolio management. Green label.

Usage:

    from npl_portfolio.eba_field_helpers import mandatory_help, recommended_help, legacy_help

    counterparty_identifier = models.TextField(
        blank=True, null=True,
        help_text=mandatory_help('1.02', 'Unique internal identifier for each counterparty.'),
    )

    some_field = models.TextField(
        blank=True, null=True,
        help_text=recommended_help('1.05', 'Description of the field.'),
    )

    old_field = models.TextField(
        blank=True, null=True,
        help_text=legacy_help('Description of the legacy field.'),
    )
"""

_EURLEX_BASE = (
    'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/'
    '?uri=CELEX:32023R2083'
)


def mandatory_help(ref: str, description: str) -> str:
    """
    Help text for a Mandatory EBA ITS 2023/2083 field (~76 fields).
    Renders a red § badge linking to EUR-Lex. Admin label → red.

    Args:
        ref:         EBA field reference, dot-notation (e.g. '1.02').
        description: Plain-text field description.
    """
    fragment = ref.replace('.', '%2C')
    url = f'{_EURLEX_BASE}#:~:text={fragment}'
    badge = (
        f'<a href="{url}" target="_blank" rel="noopener noreferrer" '
        f'title="EU 2023/2083 — EBA NPL ITS mandatory field {ref}" '
        f'style="color:#b03000; font-weight:700; margin-left:6px; '
        f'text-decoration:none; font-size:12px;">MANDATORY § {ref}</a>'
    )
    return f'{description}{badge}'


def recommended_help(ref: str, description: str) -> str:
    """
    Help text for a Recommended EBA ITS 2023/2083 field (~64 fields).
    Renders an orange § badge linking to EUR-Lex. Admin label → orange.

    Args:
        ref:         EBA field reference, dot-notation (e.g. '1.05').
        description: Plain-text field description.
    """
    fragment = ref.replace('.', '%2C')
    url = f'{_EURLEX_BASE}#:~:text={fragment}'
    badge = (
        f'<a href="{url}" target="_blank" rel="noopener noreferrer" '
        f'title="EU 2023/2083 — EBA NPL ITS recommended field {ref}" '
        f'style="color:#a05000; font-weight:600; margin-left:6px; '
        f'text-decoration:none; font-size:12px;">RECOMMENDED § {ref}</a>'
    )
    return f'{description}{badge}'


def legacy_help(description: str, prior_ref: str = '') -> str:
    """
    Help text for a Legacy field (pre-2023 EBA draft, not in EU 2023/2083).
    Kept for internal portfolio management. Admin label → green.

    Args:
        description: Original field description.
        prior_ref:   Optional reference to the prior EBA draft.
    """
    note = f' Prior ref: {prior_ref}.' if prior_ref else ''
    return (
        f'<span style="color:#1a7a4a; font-weight:600;">'
        f'LEGACY — Not in EU 2023/2083.{note}'
        f'</span>'
        f'<br><span style="color:#888;">{description}</span>'
    )


# backward-compat alias — migrate to mandatory_help() or recommended_help()
def eba_help(ref: str, description: str) -> str:
    return recommended_help(ref, description)


def deprecated_help(description: str, reason: str) -> str:
    """
    Help text for openNPL-specific fields with no EBA origin.
    Admin label → grey.
    """
    return (
        f'<span style="color:#888; font-weight:600;">'
        f'DEPRECATED — {reason}'
        f'</span>'
        f'<br><span style="color:#aaa;">{description}</span>'
    )

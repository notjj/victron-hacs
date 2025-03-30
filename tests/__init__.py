"""Tests for the victron_ble integration."""

from unittest.mock import patch

DOMAIN = "victron_ble"


def patch_async_setup_entry(return_value=True):
    """Patch async setup entry to return True."""
    return patch(
        "custom_components.victron_ble.async_setup_entry",
        return_value=return_value,
    )

"""Test the victron_ble config flow."""

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType

from custom_components.victron_ble.const import DOMAIN

from . import patch_async_setup_entry


async def test_form(hass: HomeAssistant) -> None:
    """Test we get the form."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == FlowResultType.FORM
    assert result["errors"] is None

    with patch_async_setup_entry() as mock_setup_entry:
        result = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {
                "name": "test_device",
                "address": "test-address",
                "key": "test-key",
            },
        )
        await hass.async_block_till_done()

    assert result["type"] == FlowResultType.CREATE_ENTRY
    assert result["title"] == "test_device"
    assert result["data"] == {
        "name": "test_device",
        "address": "test-address",
        "key": "test-key",
    }
    assert len(mock_setup_entry.mock_calls) == 1

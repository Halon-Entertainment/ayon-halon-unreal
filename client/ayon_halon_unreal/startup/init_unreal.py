from ayon_core.pipeline import get_current_project_name, install_host
from ayon_core.pipeline.context_tools import get_current_host_name
from ayon_core.settings import get_project_settings
from ayon_core.settings.lib import get_current_project_settings
from ayon_core.lib.log import Logger
from version_control.api.perforce import handle_login

from ayon_halon_unreal.api import menu
from ayon_halon_unreal.api.create_data_asset import AyonMetaData
from ayon_halon_unreal.api.pipeline import UnrealHost

project_settings = get_project_settings(get_current_project_name())
host_name = get_current_host_name()
version_control = project_settings.get("version_control")

log = Logger.get_logger(__name__)


def submit_metadata_asset_to_perforce(file_path: str) -> None:
    print(f"Version Control {version_control}")
    if version_control and version_control["enabled"]:
        from version_control.api.perforce import get_current_host_connection
        from version_control.rest.perforce.rest_stub import PerforceRestStub

        connection_info = get_current_host_connection()
        handle_login(connection_info)

        comment = "Ayon Metadata Parent Added"
        log.debug(f"Asset Data File Path: {file_path}")
        PerforceRestStub.add(file_path, comment)
        PerforceRestStub.submit_change_list(comment)


def create_assetdata() -> None:
    data = get_current_project_settings()
    meta_data_asset_location = data.get("ayon_halon_unreal", {}).get(
        "meta_data_asset_location", None
    )
    meta_data = AyonMetaData()
    if meta_data_asset_location:
        meta_data.set_base_path(meta_data_asset_location)

    if not meta_data.first_or_create():
        if not meta_data.file_path:
            raise ValueError(f"Unable to get file path from {str(meta_data)}")
        submit_metadata_asset_to_perforce(meta_data.file_path)

def main():
    ayon_host = UnrealHost()
    install_host(ayon_host)
    menu.init_ayon_menu()
    create_assetdata()

main()

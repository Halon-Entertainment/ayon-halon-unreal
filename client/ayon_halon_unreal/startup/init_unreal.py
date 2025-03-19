import unreal
from ayon_core.pipeline import install_host
from ayon_core.pipeline.context_tools import get_current_host_name
from ayon_halon_unreal.api import menu
from ayon_halon_unreal.api.pipeline import UnrealHost
from ayon_core.settings import get_project_settings
from ayon_core.pipeline import get_current_project_name
from version_control.api.perforce import handle_login

project_settings = get_project_settings(get_current_project_name())
host_name = get_current_host_name()
version_control = project_settings.get('version_control')

def submit_metadata_asset_to_perforce(file_path: str):
    if version_control and version_control['enabled']:
        from version_control.rest.perforce.rest_stub import PerforceRestStub
        from version_control.api.perforce import get_current_host_connection

        connection_info = get_current_host_connection()
        handle_login(connection_info)

    
        comment = "Ayon Metadata Parent Added"
        PerforceRestStub.add(file_path, comment) 
        PerforceRestStub.submit_change_list(comment)

def main():
    ayon_host = UnrealHost()
    install_host(ayon_host)
    menu.init_ayon_menu()
    metadata_asset_path = "" 
    submit_metadata_asset_to_perforce(metadata_asset_path)


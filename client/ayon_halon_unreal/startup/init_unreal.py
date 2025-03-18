import unreal
from ayon_core.pipeline import install_host
from ayon_halon_unreal.api import menu
from ayon_halon_unreal.api.pipeline import UnrealHost

from client.ayon_halon_unreal.api.create_data_asset import AyonMetaData
from ayon_core.settings import get_current_project_settings


ayon_host = UnrealHost()
install_host(ayon_host)
menu.init_ayon_menu()

data = get_current_project_settings()
meta_data_asset_location = data.get("ayon_halon_unreal", {}).get("meta_data_asset_location", None)

meta_data = AyonMetaData()
if meta_data_asset_location:
    meta_data.set_base_path(meta_data_asset_location)

meta_data.create()

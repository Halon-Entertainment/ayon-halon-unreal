import unreal
from ayon_core.pipeline import install_host
from ayon_halon_unreal.api import menu, create_data_asset
from ayon_halon_unreal.api.pipeline import UnrealHost


ayon_host = UnrealHost()
install_host(ayon_host)
menu.init_ayon_menu()
create_data_asset.create_the_bp()

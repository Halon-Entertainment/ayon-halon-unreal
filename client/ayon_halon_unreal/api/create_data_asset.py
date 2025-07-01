import typing

import unreal
from ayon_core.lib.log import Logger

log = Logger.get_logger(__name__)


class AyonMetaData:
    base_path = "/Game/"
    asset_name = "DefaultDataAsset"
    file_path: typing.Optional[str] = None

    def set_base_path(self, base_path):
        if base_path[0] != "/":
            base_path = "/" + base_path

        if base_path[-1] != "/":
            base_path = base_path + "/"

        self.base_path = base_path
        return self

    def first_or_create(self) -> bool:
        asset_path = f"{self.base_path}{self.asset_name}"
        asset_exists = unreal.EditorAssetLibrary.does_asset_exist(asset_path)

        log.debug(f"Asset Path: {asset_path}")
        log.debug(f"Asset Exists: {asset_exists}")

        if asset_exists:
            return True

        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

        blue_print_factory = unreal.BlueprintFactory()
        blue_print_factory.set_editor_property(
            "ParentClass", unreal.PrimaryDataAsset
        )

        new_blueprint = asset_tools.create_asset(
            self.asset_name,
            self.base_path,
            None,
            blue_print_factory,
        )

        unreal.EditorAssetLibrary.save_loaded_asset(new_blueprint)
        self.file_path = unreal.SystemLibrary.get_system_path(new_blueprint)
        return False

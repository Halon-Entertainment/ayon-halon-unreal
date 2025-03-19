import unreal

from ayon_halon_unreal.api import menu, paths
from dataclasses import dataclass
from importlib import reload
from ayon_halon_unreal.api import create_data_asset

class AyonMetaData:

    base_path = '/Game/'
    parent_meta_data_asset_name = "DefaultDataAsset"

    def set_base_path(self, base_path):
        if base_path[1] == '/':
            base_path = base_path[1:]

        if base_path[-1] != '/':
            base_path = base_path + '/'

        self.base_path = base_path
        return self

    def create(self):
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

        blue_print_factory = unreal.BlueprintFactory()
        blue_print_factory.set_editor_property("ParentClass", unreal.PrimaryDataAsset)

        new_blueprint = asset_tools.create_asset(
            self.parent_meta_data_asset_name, self.base_path, None, blue_print_factory
        )

        unreal.EditorAssetLibrary.save_loaded_asset(new_blueprint)

        return new_blueprint

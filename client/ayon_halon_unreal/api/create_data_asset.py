import unreal

from ayon_halon_unreal.api import menu, paths
from dataclasses import dataclass

@dataclass
class AyonMetaDataInfo:

    dataclass_parent: str = "DefaultDataAsset"
    base_path: str = f"/Game/{dataclass_parent}"
    import_dir: str = "/Game/ImportedData"
    custom_dataclass: str = "CustomDataAsset"
    custom_dataclass_dir: str = f"{base_path}.{custom_dataclass}_C"

## Create a child data asset from the vanilla one
## Basic AF
def create_child_data(new_asset_name="Donut"):
    # Load the primary data asset class
    # primary_data_asset = unreal.EditorAssetLibrary.load_asset(AyonMetaDataInfo.base_path)

    print(f"{AyonMetaDataInfo.base_path}")
    # object_class = unreal.load_object(None, AyonMetaDataInfo.base_path)
    # asset_class = unreal.EditorAssetLibrary.load_asset(AyonMetaDataInfo.base_path)
    data_asset_class = unreal.load_class(
        None,
        f"{AyonMetaDataInfo.base_path}.{AyonMetaDataInfo.dataclass_parent}_C",
    )

    if not data_asset_class:
        print(
            f"Failed to load Blueprint class: {AyonMetaDataInfo.base_path}"
        )
        return

    new_asset_path = f"{AyonMetaDataInfo.import_dir}/{new_asset_name}"
    # Create the new data asset
    new_asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=new_asset_name,
        package_path=AyonMetaDataInfo.import_dir,
        asset_class=data_asset_class,
        factory=unreal.DataAssetFactory(),
    )

    if new_asset:
        print(f"Created child data asset: {new_asset_path}")
        unreal.EditorAssetLibrary.save_asset(new_asset_path)
        return new_asset
    else:
        print(f"Failed to create child data asset: {new_asset_path}")
        return


def write_to_the_data(path="/Game/ImportedData/Some_Asset"):
    return


"""
from importlib import reload
from assets import create_data_asset
reload(create_data_asset)
create_data_asset.create_child_data("Some_Asset")
"""


def create_the_bp():
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    asset = menu.CustomDataAsset()
    # Define Blueprint path and name
    blueprint_name = "DataAssetClassThingy"
    package_path = "/Game/ImportedData"
    asset_class = unreal.Actor
    blueprint_factory = unreal.BlueprintFactory()
    new_blueprint = asset_tools.create_asset(
        blueprint_name, package_path, asset_class, blueprint_factory
    )
    return


"""
from importlib import reload
from assets import create_data_asset
reload(create_data_asset)
create_data_asset.create_the_bp()
"""


# Make the top-end data thingy
def create_primary_data_asset(child_asset_name="Derp"):
    asset = menu.CustomDataAsset()

    print(f"Custom Class: {asset}, saving it in: {AyonMetaDataInfo.custom_dataclass}")

    data_asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        AyonMetaDataInfo.custom_dataclass,  # Asset name
        '/Game',  # Folder path
        unreal.PrimaryDataAsset,  # Class type
        unreal.DataAssetFactory(),  # Generic factory (use a specific one if needed)
    )
    return

    data_asset_class = unreal.load_class(
        None, f"{AyonMetaDataInfo.custom_dataclass_dir}.{AyonMetaDataInfo.custom_dataclass}"
    )
    return


from importlib import reload
from ayon_halon_unreal.api import create_data_asset

reload(create_data_asset)
# create_data_asset.create_the_bp()
create_child_data()
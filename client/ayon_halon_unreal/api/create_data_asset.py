import unreal

from ayon_halon_unreal.api import menu, paths


## Create a child data asset from the vanilla one
## Basic AF
def create_child_data(child_asset_name="Derp"):
    # Load the primary data asset class
    # primary_data_asset = unreal.EditorAssetLibrary.load_asset(paths.path_to_vanilla_data_class())

    print(f"{paths.path_to_vanilla_data_class()}")
    # object_class = unreal.load_object(None, paths.path_to_vanilla_data_class())
    # asset_class = unreal.EditorAssetLibrary.load_asset(paths.path_to_vanilla_data_class())
    data_asset_class = unreal.load_class(
        None,
        f"{paths.path_to_vanilla_data_class()}.{paths.vanilla_data_name()}_C",
    )

    if not data_asset_class:
        print(
            f"Failed to load Blueprint class: {paths.path_to_vanilla_data_class()}"
        )
        return

    new_asset_name = f"{child_asset_name}"
    new_asset_path = f"{paths.data_import_dir()}/{new_asset_name}"
    # Create the new data asset
    new_asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        asset_name=new_asset_name,
        package_path=paths.data_import_dir(),
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
    package_path = paths.path_to_custom_data_class()
    print(f"Custom Class: {asset}, saving it in: {package_path}")

    data_asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        paths.custom_data_name(),  # Asset name
        paths.path_to_plugin(),  # Folder path
        unreal.PrimaryDataAsset,  # Class type
        unreal.DataAssetFactory(),  # Generic factory (use a specific one if needed)
    )
    return

    data_asset_class = unreal.load_class(
        None, f"{paths.path_to_custom_data_class()}.{paths.custom_data_name()}"
    )
    return

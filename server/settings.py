from ayon_server.settings import BaseSettingsModel, SettingsField
from .import_settings import UnrealImportModel, UnrealInterchangeModel


class UnrealSettings(BaseSettingsModel):
    enabled: bool = SettingsField(
        True,
        title="Enabled",
        scope=['studio', 'project']
    )
    uproject_file_path: str = SettingsField(
        "{root[work]}/unreal/{project[name].uproject",
        scope=['studio', 'project'],
        title="UProject File Path",
        description="Templated file path to find the uproject file at launch."
    )
    data_asset_name: str = SettingsField(
        "DefaultDataAsset",
        title="Data Asset Class Name",
        description="AYON Container name"
    )
    content_storage_root: str = SettingsField(
        "/Game",
        title="AYON Content Root Path",
        description="Root to prepend onto storage name to build the asset paths, typically /Game"
    )
    content_storage_path: str = SettingsField(
        "Halon",
        title="AYON Content Folder",
        description="Folder name or path within storage where we store all assets, Ayon folder"
    )
    import_settings: UnrealImportModel = SettingsField(
        default_factory=UnrealImportModel,
        title="Import settings"
    )
    meta_data_asset_location: str = SettingsField(
        "Game",
        scope=['studio', 'project'],
        title="Meta Data Asset Location",
        description="Location to store the meta data asset"
    )


DEFAULT_VALUES = {
    "plugin_name": "NewAyon",
    "data_asset_name": "DefaultDataAsset",
    "content_storage_root": "/Game",
    "content_storage_path": "FnBrCine_CommonAssets",
}

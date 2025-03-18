from ayon_server.settings import BaseSettingsModel, SettingsField
from .import_settings import UnrealImportModel, UnrealInterchangeModel


class UnrealSettings(BaseSettingsModel):
    enabled: bool = SettingsField(
        True,
        title="Enabled",
        scope=['studio', 'project']
    )
    plugin_name: str = SettingsField(
        "NewAyon",
        title="AYON Plugin Name",
        description="Root of the Directory where primary data asset is stored, Plugin or Game"
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
        "FnBrCine_CommonAssets",
        title="AYON Content Folder",
        description="Folder name or path within storage where we store all assets, Ayon folder"
    )

    import_settings: UnrealImportModel = SettingsField(
        default_factory=UnrealImportModel,
        title="Import settings"
    )


DEFAULT_VALUES = {
    "plugin_name": "NewAyon",
    "data_asset_name": "DefaultDataAsset",
    "content_storage_root": "/Game",
    "content_storage_path": "FnBrCine_CommonAssets",
}

from ayon_server.settings import BaseSettingsModel, SettingsField


class UnrealSettings(BaseSettingsModel):
    enabled: bool = SettingsField(
        True,
        title="Enabled",
        scope=['studio', 'project']
    )
    plugin_folder: str = SettingsField(
        "/Plugins/GameFeatures/Cine/FNBR",
        title="Base Plugin Directory",
        description="Unreal Plugin Directory that all other paths will be searched within"
    )

    ayon_storage_paths: str = SettingsField(
        "/FnBrCine_CommonAssets",
        title="AYON Content Path",
        description="Directory within the Plugin where we will search for AYON content"
    )


DEFAULT_VALUES = {
    "plugin_folder": "/Plugins/GameFeatures/Cine/FNBR",
    "ayon_storage_paths": "/FnBrCine_CommonAssets",
}

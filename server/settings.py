from ayon_server.settings import BaseSettingsModel, SettingsField


class UnrealSettings(BaseSettingsModel):
    enabled: bool = SettingsField(
        True,
        title="Enabled",
        scope=['studio', 'project']
    )
    plugin_folder: str = SettingsField(
        "/Plugins/Cinematics",
        title="Base Plugin Directory",
        description="Unreal Plugin Directory that all other paths will be searched within"
    )

    ayon_storage_paths: list[str] = SettingsField(
        default_factory = list[str],
        title="AYON Content Paths",
        description="Directories within the Plugin where we will search for AYON content"
    )


DEFAULT_VALUES = {
    "plugin_folder": "/Plugins/Cinematics",
    "ayon_storage_paths": [],
}

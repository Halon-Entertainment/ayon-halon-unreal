import os
from ayon_core.addon import AYONAddon, IHostAddon
import time
from .version import __version__

UNREAL_ADDON_ROOT = os.path.dirname(os.path.abspath(__file__))

class AyonHalonUnreal(AYONAddon, IHostAddon):
    name = "unreal"
    version = __version__
    host_name = "unreal"

    @property
    def name(self):
        return "ayon-halon-unreal"

    @property
    def version(self):
        return __version__

    def initialize(self, settings):
        print(f"Initializing Ayon Halon Unreal Addon...")
        return super().initialize(settings)

    def get_global_environments(self):
        return {
            "AYON_UNREAL_ROOT": UNREAL_ADDON_ROOT,
        }

    def get_global_environments(self):
        return {
            "UNREAL_ADDON_ROOT": UNREAL_ADDON_ROOT,
        }

    def get_launch_hook_paths(self, app):
        return [
            os.path.join(UNREAL_ADDON_ROOT, "hooks")
        ]
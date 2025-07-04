import os
import pathlib
import time

from ayon_core.addon import AYONAddon, IHostAddon

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
        env = os.environ
        env.update(
            {
                "UE_PYTHONPATH": os.environ.get("PYTHONPATH", "")
                + os.pathsep
                + (pathlib.Path(UNREAL_ADDON_ROOT) / "startup").as_posix(),
                "AYON_LOG_NO_COLORS": "1",
            }
        )
        env["ENV_SET"] = "True"
        os.environ.update(env)

    def get_global_environments(self):
        return {
            "AYON_UNREAL_ROOT": UNREAL_ADDON_ROOT,
        }

    def get_launch_hook_paths(self, app):
        return [os.path.join(UNREAL_ADDON_ROOT, "launch_hooks")]

    def add_implementation_envs(self, env, app):
        env = {
            "UE_PYTHONPATH": os.environ.get("PYTHONPATH", ""),
            "AYON_LOG_NO_COLORS": "1",
        }
        env["ENV_SET"] = "True"

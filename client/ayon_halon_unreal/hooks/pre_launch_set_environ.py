import os
import pathlib

from ayon_applications import LaunchTypes, PreLaunchHook

from ayon_halon_unreal.addon import UNREAL_ADDON_ROOT


class UnrealPrelaunchEnvironmentHook(PreLaunchHook):
    """Hook to handle launching Unreal.

    This hook will check if current workfile path has Unreal
    project inside. IF not, it initializes it, and finally it pass
    path to the project by environment variable to Unreal launcher
    shell script.

    """

    app_groups = {"unreal"}
    launch_types = {LaunchTypes.local}
    order = 200

    def execute(self):
        """Hook entry method."""

        # self.log.debug("Running Pre Env Hook")
        #
        # env = os.environ
        # env['UE_PYTHONPATH'] = env["PYTHONPATH"]
        # env["UE_PYTHONPATH"] = (
        #     env.get("UE_PYTHONPATH", "")
        #     + os.pathsep
        #     + (pathlib.Path(UNREAL_ADDON_ROOT) / "startup").as_posix()
        # )
        # os.environ.update(env)
        pass

import os
import pathlib
from shutil import rmtree
import subprocess

from ayon_applications.defs import Application

from ayon_core.addon.base import AddonsManager
from ayon_core.lib.log import Logger

log = Logger.get_logger(__name__)


class RequirementManager(object):
    def __init__(self, addons_manager: AddonsManager, application: Application):
        app_data = os.getenv("LOCALAPPDATA")
        self.application = application
        self.addons_manager = addons_manager
        if not app_data:
            raise RuntimeError("No appdata found on system.")

        self.addon_resourses_dir = pathlib.Path(app_data, "halon", "halon-ayon-unreal")
        self.application_version_dir = self.addon_resourses_dir / f"{application.name}"
        self.application_site_packages = (
            self.application_version_dir / "site-packages"
        )
        ue_python_path = os.getenv("UE_PYTHONPATH", "")
        ue_python_path = (
            ue_python_path + f";{self.application_site_packages.as_posix()}"
        )


    def addon_updated(self):
        self.application_site_packages.mkdir(exist_ok=True, parents=True)
        addons_by_name = self.addons_manager.addons_by_name
        unreal_addon = addons_by_name['ayon-halon-unreal']
        unreal_addon_version = unreal_addon.version
        addon_tracker_file = self.application_version_dir / "addon-version.txt"
        if not addon_tracker_file.exists():
            with open(addon_tracker_file, 'w') as tracker_handle:
                tracker_handle.write(unreal_addon_version)
            return True
        
        with open(addon_tracker_file, 'r') as tracker_handle:
            tracker_version = tracker_handle.read()

        if tracker_version == unreal_addon_version:
            return False
        else:
            with open(addon_tracker_file, 'w') as tracker_handle:
                tracker_handle.write(unreal_addon_version)
            return True

    def install_requirements(self):
        if self.addon_updated():
            rmtree(self.application_site_packages)
            self.application_site_packages.mkdir(exist_ok=True, parents=True)

            pip_requirements = ["PySide6"]
            args = ["-m", "pip", "install"]
            args += pip_requirements
            args += [f"--target={self.application_site_packages.as_posix()}"]

            unreal_executable = pathlib.Path(
                self.application.executables[0].executable_path
            )
            binaries_folder = list(unreal_executable.parents)[1]
            log.debug(binaries_folder)
            python_executable = (
                binaries_folder / "ThirdParty/Python3/Win64/python.exe"
            )
            log.debug(f"Python Executable: {python_executable.as_posix()}")

            cmd = [python_executable] + args
            result = subprocess.run(cmd)
            if result.returncode != 0:
                raise RuntimeError("Failed to install pip_requirements")

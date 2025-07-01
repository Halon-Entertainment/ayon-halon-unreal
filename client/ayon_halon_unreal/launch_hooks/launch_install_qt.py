from ayon_core.pipeline.context_tools import _get_addons_manager
from ayon_halon_unreal.reload import main
main()

from ayon_applications import LaunchTypes, PreLaunchHook
from ayon_halon_unreal.startup.requirements import RequirementManager


class LaunchInstallQt(PreLaunchHook):
    order = -8
    app_groups = ["unreal"]
    launch_types = {LaunchTypes.local}

    def execute(self):
        application = self.launch_context.application
        addons_manager = _get_addons_manager()
        requirement_manager = RequirementManager(addons_manager, application)
        self.log.debug(f"Installing Python Requirements for {application.full_name}")
        requirement_manager.install_requirements()
        
        ue_python_path = self.launch_context.env.get("UE_PYTHONPATH", "")
        ue_python_path = ue_python_path + f";{requirement_manager.application_site_packages.as_posix()}"

        self.launch_context.env["UE_PYTHONPATH"] = ue_python_path


from ayon_applications import (
    PreLaunchHook,
    ApplicationLaunchFailed,
    LaunchTypes,
)
from ayon_core.settings import get_project_settings
from ayon_core.pipeline.workfile import get_workfile_template_key


class UnrealPrelaunchHook(PreLaunchHook):
    """Hook to handle launching Unreal.

    This hook will check if current workfile path has Unreal
    project inside. IF not, it initializes it, and finally it pass
    path to the project by environment variable to Unreal launcher
    shell script.

    """
    app_groups = {"unreal"}
    launch_types = {LaunchTypes.local}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.signature = f"( {self.__class__.__name__} )"

    def _get_work_filename(self):
        # Use last workfile if was found
        if self.data.get("last_workfile_path"):
            last_workfile = Path(self.data.get("last_workfile_path"))
            if last_workfile and last_workfile.exists():
                return last_workfile.name

        # Prepare data for fill data and for getting workfile template key
        anatomy = self.data["anatomy"]
        project_entity = self.data["project_entity"]


    def execute(self):
        """Hook entry method."""
        project_settings = self.data["project_settings"]
        unreal_settings = project_settings["ayon_halon_unreal"]
        if not unreal_settings['enabled']:
            return

        workdir = self.launch_context.env["AYON_WORKDIR"]
        executable = str(self.launch_context.executable)
        self.log.debug(f"Launching Unreal, Workdir: {workdir}, Exec: {executable}")

        project_file_path = 'D:/p4/Test_Project/unreal/testproject.uproject'

        self.launch_context.launch_args.append(
            f"\"{project_file_path}\""
        )
        self.log.debug(f"{self.launch_context.executable} {self.launch_context.launch_args[0]}")

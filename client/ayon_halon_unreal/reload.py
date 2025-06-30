import sys
import os
from ayon_core.lib.log import Logger

log = Logger.get_logger(__name__)

def main():
    if os.getenv("AYON_USE_DEV", False):
        log.debug('Reloading Halon Unreal')

        import importlib

        modules_to_reload = []
        for module_name, module in sys.modules.items():
            if module_name in [
                "ayon_halon_unreal.startup",
                "ayon_halon_unreal.api",
            ]:
                modules_to_reload.append(module)

        for module in modules_to_reload:

            importlib.reload(module)

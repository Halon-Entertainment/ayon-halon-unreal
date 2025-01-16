from ayon_core.addon import AYONAddon

from .version import __version__



class AyonHalonUnreal(AYONAddon):
    @property
    def name(self):
        return "ayon-halon-unreal"

    @property
    def version(self):
        return __version__

    def initialize(self, settings):
        return super().initialize(settings)
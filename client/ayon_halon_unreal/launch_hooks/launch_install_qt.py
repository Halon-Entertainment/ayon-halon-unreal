import os
import pathlib
import zipfile
import pip._internal as pip

from ayon_applications import LaunchTypes, PreLaunchHook
import requests


class LaunchInstallQt(PreLaunchHook):
    order = -8
    app_groups = ["unreal"]
    launch_types = {LaunchTypes.local}

    def execute(self):
        application = self.launch_context.application
        application_name = application.name

        addons_resources_dir = pathlib.Path(
            os.getenv("LOCALAPPDATA"), 'halon'
        )

        self.sitepackages_location = (
            addons_resources_dir / f"halon-ayon-unreal/{application_name}/site-packages"  
        )
        python_path = os.environ.get('UE_PYTHONPATH', "")
        python_path = python_path + f";{self.sitepackages_location.as_posix()}"
        self.downloads_location = (
            addons_resources_dir / f"halon-ayon-unreal/{application_name}/downloads"
        )

        qt_versions = {
            "5-3": ["https://files.pythonhosted.org/packages/d1/ef/0aa5e910fa4e9770db6b45c23e360a52313922e0ca71fc060a57db613de1/PySide6-6.9.1-cp39-abi3-win_arm64.whl",
                    "https://files.pythonhosted.org/packages/26/bd/a1b31f49eb35888eae318c27327732b1036f0d921e5c8ec2e7a4276e7445/shiboken2-5.15.2.1-5.15.2-cp35.cp36.cp37.cp38.cp39.cp310-none-win_amd64.whl"]
        }

        self.urls = qt_versions[application_name]
        self.install_qt()

    def install_qt(self):
        qt_packages = self.download_qt()
        self.sitepackages_location.mkdir(parents=True, exist_ok=True)
        for package in qt_packages:
            with zipfile.ZipFile(package, 'r') as whl_file:
                whl_file.extractall(path=self.sitepackages_location)

    def download_qt(self):
        packages = []
        for url in self.urls:
            reponse = requests.get(url)
            package_name = url.split('/')[-1]
            package = self.downloads_location / package_name
            packages.append(package)
            if reponse.status_code == 200:
                self.downloads_location.mkdir(parents=True, exist_ok=True)

                if not package.exists():
                    with open(package, 'wb') as file:
                        file.write(reponse.content)
            else:
                raise RuntimeError('Unable to download Qt')

        return packages

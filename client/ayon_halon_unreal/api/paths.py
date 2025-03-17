import unreal

def path_to_plugin():
    return "/NewAyon"

def vanilla_data_name():
    return "DefaultDataAsset"

def path_to_vanilla_data_class():
    return f"{path_to_plugin()}/{vanilla_data_name()}"

def data_import_dir():
    return f"/Game/ImportedData"

def custom_data_name():
    return "CustomDataAsset"

def path_to_custom_data_class():
    return f"{path_to_plugin()}/{custom_data_name()}"





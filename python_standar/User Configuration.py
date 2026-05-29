test_settings = {
    "theme": "dark",
    "language": "es"
}
def add_setting(config_dict, setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()

    if key in config_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        config_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    
    for key in config_dict:
        if key.lower() == key.lower():
            return f"Setting 'theme' already exists! Cannot add a new setting with this name."
def update_setting(config_dict, update_tuple):
    key, value = update_tuple
    key = key.lower()
    value = value.lower()

    if key in config_dict:
        config_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
def delete_setting(config_dict, key):
    key = key.lower()

    if key in config_dict:
        del config_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(config_dict):
    if not config_dict:
        return f"No settings available."
    result = f"Current User Settings:\n"
    for key, value in config_dict.items():
        result += f"{key.capitalize()}: {value}\n"
    
    return result

print(add_setting({'theme': 'light'}, ('THEME', 'dark')))

print(add_setting({'theme': 'light'}, ('volume', 'high')))

print(delete_setting({'theme': 'light'}, 'theme'))

print(view_settings(test_settings))
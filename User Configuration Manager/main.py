#settings
test_settings = {
    'theme': 'light',
    'language': 'English',
    'notifications': 'allow',
}
def add_setting(settings, new_settings):
    key = new_settings[0].lower()
    value = new_settings[1].lower()
    if key in settings:
        return f"Setting {key} already exists! Cannot add a new setting with this name."
    else:
        return f"Settings {key} added with value {value} successfully!"

def update_settings(settings, new_settings):
    key = new_settings[0].lower()
    value = new_settings[1].lower()
    if key in settings:
        settings[key] = value
        return f"Settings {key} updated to {value} successfully!"
    else:
        return f"Setting {key} does not exist! Cannot update a non-existing setting."
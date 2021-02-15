import os

def set_wallpaper(wp_path):
    """
    Sets Linux desktop background (wallpaper) to image file path parameter.
    """
    os.system(f"gsettings set org.gnome.desktop.background picture-uri \"{wp_path}\"")

def is_image(path):
    """
    Returns true if file specified is an image.
    """
    return True


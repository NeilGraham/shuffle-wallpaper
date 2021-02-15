import argparse, os, time, random
from shuffle import set_wallpaper, is_image

parser = argparse.ArgumentParser()
parser.add_argument(
    "-r", "--recursive", action="store_true",
    help="Recursively search for images to set wallpaper to."
)
parser.add_argument(
    "path", help="Path to wallpaper(s) file or directory."
)
parser.add_argument(
    "-t", "--time", type=float, default=10.0, 
    help="Time (in minutes) before shuffling to next wallpaper."
)
args = parser.parse_args()


wallpapers = []

if os.path.isfile(args.path) and is_image():
    wallpapers.append(args.path)
    
elif os.path.isdir(args.path):
    if args.recursive == False:
        raise ValueError("Specify argument '-r' to select all files recursively inside a folder.")
    for root, dirs, files in os.walk(args.path):
        for file in files:
            path = os.path.join(root,file)
            if is_image(path):
                wallpapers.append(path)

last:str = os.system("gsettings get org.gnome.desktop.background picture-uri")
while True:
    random.shuffle(wallpapers)
    while last == wallpapers[0]:
        random.shuffle(wallpapers)

    for wp_path in wallpapers:
        set_wallpaper(wp_path)
        time.sleep(60*args.time)
        last = wp_path

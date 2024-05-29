try:
    mkdir(path.join(root, "bin/womp"))
except FileExistsError:
    pass


for i in [
    "init.py",
    "hs.py",
    "load_fm.py",
    "load_kb.py",
    "load_lock.py",
    "load_settings.py" "unload_fm.py",
    "unload_kb.py",
    "unload_lock.py",
    "unload_settings.py" "womp.py",
]:
    shutil.copyfile(i, path.join(root, "bin/womp", i))

shutil.copyfile("womp.lja", path.join(root, "bin", "womp.lja"))

try:
    mkdir(path.join(root, "boot"))
except FileExistsError:
    pass

try:
    mkdir(path.join(root, "boot/boot.d"))
except FileExistsError:
    pass

shutil.copyfile("99-womp.lja", path.join(root, "boot/boot.d", "99-womp.lja"))

try:
    mkdir(path.join(root, "usr/share/applications"))
except FileExistsError:
    pass

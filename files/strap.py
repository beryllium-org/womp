try:
    mkdir(path.join(root, "bin/womp"))
except FileExistsError:
    pass

for i in [
    "womp.py",
    "init.py",
]:
    shutil.copy(i, path.join(root, "bin/womp", i))

shutil.copy("womp.lja", path.join(root, "bin", "womp.lja"))
shutil.copy("99-womp.lja", path.join(root, "boot", "99-womp.lja"))

try:
    mkdir(path.join(root, "usr/share/applications"))
except FileExistsError:
    pass

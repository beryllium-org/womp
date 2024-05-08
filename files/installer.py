be.based.run("mkdir /bin/womp")
for pv[get_pid()]["f"] in [
    "init.py",
    "hs.py",
    "load_fm.py",
    "load_kb.py",
    "load_lock.py",
    "load_settings.py"
    "unload_fm.py",
    "unload_kb.py",
    "unload_lock.py",
    "unload_settings.py"
    "womp.py",
]:
    be.based.run("cp " + vr("f") + " /bin/womp/" + vr("f"))
be.based.run("cp womp.lja /bin/womp.lja")
be.based.run("cp 99-womp.lja /boot/boot.d/99-womp.lja")
be.based.run("mkdir /usr/share/applications")

be.api.setvar("return", "0")

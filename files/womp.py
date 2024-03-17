rename_process("womp")
vr("opts", be.api.xarg())
if (not be.api.console_connected()) or "f" in vr("opts")["o"]:
    be.api.subscript("/bin/womp/init.py")
    be.api.subscript("/bin/womp/funcs1.py")
    be.api.subscript("/bin/womp/funcs2.py")
    vr("main")()
    vr("c").disable()
    be.devices["DISPLAY"][0].auto_refresh = True
else:
    term.write("Another console is already connected, rerun with -f to run anyways.")

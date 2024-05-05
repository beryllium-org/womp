rename_process("womp")
vr("opts", be.api.xarg())
if (not be.api.console_connected()) or "f" in vr("opts")["o"]:
    vr("ok", 0)
    be.api.subscript("/bin/womp/init.py")
    be.api.subscript("/bin/womp/funcs1.py")
    be.api.subscript("/bin/womp/funcs2.py")
    be.api.subscript("/bin/womp/funcs3.py")
    be.api.subscript("/bin/womp/funcs4.py")
    if vr("ok") == 5:
        vr("main")()
    else:
        term.write("Failed to init womp!")
    vr("c").disable()
    be.devices["DISPLAY"][0].auto_refresh = True
else:
    term.write("Another console is already connected, rerun with -f to run anyways.")

rename_process("womp")
vr("opts", be.api.xarg())
if (not be.api.console_connected()) or "f" in vr("opts")["o"]:
    vr("ok", 0)
    be.api.subscript("/bin/womp/init.py")
    be.api.subscript("/bin/womp/funcs1.py")
    be.api.subscript("/bin/womp/funcs2.py")
    be.api.subscript("/bin/womp/funcs3.py")
    be.api.subscript("/bin/womp/funcs4.py")
    gc.collect()
    gc.collect()
    vr("crashes", 0)
    if vr("ok") == 5:
        while vr("crashes") < 3:
            try:
                vr("main")()
                break
            except Exception as err:
                vrp("crashes")
                gc.collect()
                gc.collect()
                term.write("Womp crashed. Crash log:")
                term.nwrite(str(format_exception(err)[0]))
                del err
                if vr("crashes") != 3:
                    term.write("Reloading womp..")
                else:
                    term.write("Too many crashing, exiting womp!")
    else:
        term.write("Failed to init womp!")
    vr("c").disable()
    be.devices["DISPLAY"][0].auto_refresh = True
else:
    term.write("Another console is already connected, rerun with -f to run anyways.")

def ri() -> int:
    try:
        vr("d").focus = 0
        be.io.ledset(1)
        vr("d").buf[1] = ""
        vr("d").program()
        be.io.ledset(3)
    except KeyboardInterrupt:
        vr("d").buf[0] = 4
    return vr("d").buf[0]


vr("ri", ri)
del ri


def ctop(data: str) -> None:
    vr("d").clear()
    vr("d").write(data)


vr("ctop", ctop)
del ctop


def repeatk() -> None:
    if vr("p").in_waiting:
        ct = time.monotonic()
        while vr("p").in_waiting and time.monotonic() - ct < 0.15:
            pass


vr("repeatk", repeatk)
del repeatk


def waitc() -> None:
    while vr("p").in_waiting:
        time.sleep(0.02)


vr("waitc", waitc)
del waitc


def lc() -> None:
    vr("d").nwrite("\r\033[K")


vr("lc", lc)
del lc


def ditem(item: str, sel: bool) -> None:
    vr("lc")()
    ldat = " - "
    if sel:
        ldat += "[ "
    ldat += item
    if sel:
        ldat += " ]"
    vr("d").write(ldat)


vr("ditem", ditem)
del ditem


def refr() -> None:
    be.devices["DISPLAY"][0].refresh()


vr("refr", refr)
del refr


def dmenu(title: str, data: list, hint=None, preselect=0) -> int:
    vr("waitc")()
    vr("ctop")(title + "\n" + (vr("c").size[0] * "-"))
    if hint is not None:
        vr("d").move(y=vr("c").size[1])
        vr("d").nwrite(hint)
    sel = preselect
    scl = 0
    while sel - scl > vr("c").size[1] - 6:
        scl += 1
    while not vr("quit_womp"):
        vr("repeatk")()
        vr("d").move(y=3)
        big = len(data) > vr("c").size[1] - 6
        if not big:
            vr("d").write()
            for i in range(len(data)):
                vr("ditem")(data[i], sel == i)
        else:
            vr("lc")()
            vr("d").write("   [...]" if scl else None)
            for i in range(vr("c").size[1] - 5):
                vr("ditem")(data[i + scl], sel - scl == i)
            vr("lc")()
            vr("d").write(
                "   [...]" if (scl != len(data) - vr("c").size[1] + 5) else None
            )
        vr("refr")()
        v = vr("ri")()
        if v == 2:
            if sel < len(data) - 1:
                sel += 1
                if big and (sel - scl > vr("c").size[1] - 6):
                    scl += 1
        elif not v:
            if sel:
                sel -= 1
                if scl and (sel - scl < 0):
                    scl -= 1
        elif v == 7:
            return sel
        elif v == 4:
            return -1


vr("dmenu", dmenu)
del dmenu


def appm() -> None:
    apps_lst = be.api.fs.listdir("/usr/share/applications")
    apps_k = ["Main menu"]
    for i in range(len(apps_lst)):
        apps_k.append(apps_lst[i][0])
    while True:
        sel = vr("dmenu")(
            "Apps",
            apps_k,
            hint="Press top left to go back. Press Enter to select.",
        )
        if sel in [-1, 0]:
            break
        else:
            pass  # not yet implemented
            # be.based.command.fpexec("/usr/share/applications/")


vr("appm", appm)
del appm

def hs() -> None:
    while not vr("quit_womp"):
        sel = vr("dmenu")(
            "Home",
            ["Apps", "Files", "Settings"],
            hint="Press top left to quit. Press Enter to select.",
        )
        if sel == -1:
            break
        elif sel == 0:
            vr("appm")()
        elif sel == 1:
            be.api.subscript("/bin/womp/load_fm.py")
            vr("filem")()
            be.api.subscript("/bin/womp/unload_fm.py")
        else:
            be.api.subscript("/bin/womp/load_settings.py")
            vr("setm")()
            be.api.subscript("/bin/womp/unload_settings.py")


vr("hs", hs)
del hs


def lkb() -> None:
    be.api.subscript("/bin/womp/load_kb.py")


vr("lkb", lkb)
del lkb


def ukb() -> None:
    be.api.subscript("/bin/womp/unload_kb.py")


vr("ukb", ukb)
del ukb

vr("quit_womp", False)

def vmain() -> None:
    while not vr("quit_womp"):
        be.api.subscript("/bin/womp/load_lock.py")
        if vr("lm")():
            be.api.subscript("/bin/womp/unload_lock.py")
            vr("hs")()
        else:
            break


vr("main", vmain)
del vmain

vrp("ok")

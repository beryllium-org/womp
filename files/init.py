vr("opts", be.api.xarg())
vr("d", jcurses())
vr("c", pv[0]["consoles"]["ttyDISPLAY0"])
vr("d").console = vr("c")
vr("d").clear()
vr("p", be.devices["wiopad"][0])
be.devices["DISPLAY"][0].auto_refresh = False

vr("d").trigger_dict = {
    "w": 0,
    "a": 1,
    "s": 2,
    "d": 3,
    "x": 4,
    "ctrlC": -1,
    "c": 5,
    "v": 6,
    "enter": 7,
    "overflow": 8,
    "rest": "ignore",
    "rest_a": "common",
    "echo": "none",
    "prefix": "",
    "permit_pos": False,
}
vr("c").enable()


def ri() -> int:
    try:
        vr("d").focus = 0
        vr("d").buf[1] = ""
        vr("d").program()
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


def lm() -> bool:
    vr("d").clear()
    vr("ctop")(
        "Wio Operation Menu Program (W. O. M. P.)"
        + " " * 8
        + "v1.0"
        + (vr("c").size[0] * "-")
    )
    vr("d").move(y=vr("c").size[1])
    vr("d").nwrite("Hold top left to quit. To unlock, hold enter.")
    vr("d").move(y=3)
    vr("refr")()
    while True:
        v = vr("ri")()
        if v == -1:
            return False
        if v in [4, 7]:
            ct = time.monotonic()
            good = True
            while time.monotonic() - ct < 1.2:
                if not pv[0]["consoles"]["ttyDISPLAY0"].in_waiting:
                    good = False
                    break
            if good:
                vr("d").move(y=vr("c").size[1])
                vr("lc")()
                vr("d").nwrite("To continue, release.")
                vr("refr")()
                vr("waitc")()
                return v == 7


vr("lm", lm)
del lm


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
    while (sel - scl > vr("c").size[1] - 6):
        scl += 1
    while True:
        vr("repeatk")()
        vr("d").move(y=3)
        big = len(data) > vr("c").size[1] - 3
        if not big:
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
    while True:
        sel = vr("dmenu")(
            "Apps",
            [
                "No apps",
            ],
            hint="Press top left to go back. Press Enter to select.",
        )
        if sel == -1:
            break


vr("appm", appm)
del appm

def filem() -> None:
    while True:
        sel = vr("dmenu")(
            "File Manager",
            [
                "Not yet implemented",
            ],
            hint="Press top left to close. Press Enter to select.",
        )
        if sel == -1:
            break


vr("filem", filem)
del filem

def setm() -> None:
    while True:
        sel = vr("dmenu")(
            "Settings",
            [
                "Not yet implemented",
            ],
            hint="Press top left to close. Press Enter to select.",
        )
        if sel == -1:
            break


vr("setm", setm)
del setm


def about() -> None:
    vr("ctop")("About" + "\n" + (vr("c").size[0] * "-"))
    vr("d").write(
        "Beryllium OS Wio Operational Menu Program\n"
        + "Version 1.0\n\n"
        + "I'm eepy."
    )
    vr("refr")()
    vr("waitc")()
    vr("ri")()


vr("about", about)
del about


def hs() -> None:
    while True:
        sel = vr("dmenu")(
            "Home",
            ["Apps", "Files", "Settings", "About"],
            hint="Press top left to quit. Press Enter to select.",
        )
        if sel == -1:
            break
        elif sel == 0:
            vr("appm")()
        elif sel == 1:
            vr("filem")()
        elif sel == 2:
            vr("setm")()
        elif sel == 3:
            vr("about")()


vr("hs", hs)
del hs


def vmain() -> None:
    while True:
        if vr("lm")():
            vr("hs")()
        else:
            break


vr("main", vmain)
del vmain

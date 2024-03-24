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

vr("tix", 0)

def ticker() -> None:
    if not vr("tix"):
        vr("d").nwrite("[|||||||]")
    elif vr("tix") == 1:
        vr("d").nwrite("[ ||||| ]")
    elif vr("tix") == 2:
        vr("d").nwrite("[  |||  ]")
    elif vr("tix") == 3:
        vr("d").nwrite("[   |   ]")
    elif vr("tix") == 4:
        vr("d").nwrite("[  |||  ]")
    elif vr("tix") == 5:
        vr("d").nwrite("[ ||||| ]")
    vrp("tix")
    if vr("tix") == 6:
        vr("tix", 0)

vr("ticker", ticker)
del ticker

def drinfo() -> None:
    vr("d").move(x=23, y=6)
    vr("d").nwrite(str(len(pid_act)) + " Active processes   ")
    vr("d").move(x=23, y=7)
    vr("d").nwrite(str(len(be.scheduler)) + " Running in background   ")
    vr("d").move(x=23, y=8)
    gc.collect()
    gc.collect()
    vr("d").nwrite(str(gc.mem_free()) + " Bytes free     ")
    vr("d").move(x=37, y=9)
    vr("ticker")()
    vr("refr")()

vr("drinfo", drinfo)
del drinfo

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
    vr("d").move(y=4)
    sps = 4 * " "
    vr("d").write(sps + ".------------.")
    vr("d").write(sps + "| 4   9.0122 |")
    vr("d").write(sps + "|    _  _    |")
    vr("d").write(sps + "|   |_)|_    |")
    vr("d").write(sps + "|   |_)|_    |")
    vr("d").write(sps + "|            |    System active")
    vr("d").write(sps + "| Beryllium  |")
    vr("d").write(sps + "'------------'")
    del sps
    be.io.ledset(1)
    last_r = 0
    try:
        while True:
            if float(time.monotonic() - last_r) > 0.4:
                vr("drinfo")()
                last_r = time.monotonic()
            vr("d").focus = 0
            vr("d").buf[1] = ""
            vr("d").buf[0] = 9
            gc.collect()
            vr("d").program_non_blocking()
            v = vr("d").buf[0]
            if v == -1:
                return False
            elif v in [4, 7]:
                be.io.ledset(3)
                ct = time.monotonic()
                good = True
                while time.monotonic() - ct < 0.5:
                    if not pv[0]["consoles"]["ttyDISPLAY0"].in_waiting:
                        good = False
                        be.io.ledset(1)
                        break
                if good:
                    vr("d").move(y=vr("c").size[1])
                    vr("lc")()
                    vr("d").nwrite("To continue, release.")
                    vr("refr")()
                    vr("waitc")()
                    return v == 7
            elif v == 9:
                be.api.tasks.run()
    except KeyboardInterrupt:
        return False


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
    while sel - scl > vr("c").size[1] - 6:
        scl += 1
    while True:
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

vr(
    "mdict",
    {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    },
)


def filem() -> None:
    old = getcwd()
    sel = 0
    while True:
        listing = be.api.fs.listdir()
        notr = getcwd() != "/"
        fl = ["d | .."] if notr else []
        for i in range(len(listing)):
            fl.append(listing[i][1] + " | " + listing[i][0])
        sel = vr("dmenu")(
            "File Manager | In: " + be.api.fs.resolve(),
            fl,
            hint="Press top left to close. Press Enter to select.",
            preselect=sel,
        )
        if sel == -1:
            break
        elif notr:
            if not sel:
                chdir("..")
                sel = 0
            else:
                if be.api.fs.isdir(listing[sel - 1][0]) == 1:
                    chdir(listing[sel - 1][0])
                    sel = 0
                else:
                    vr("fselm")(listing[sel - (1 if notr else 0)])
        else:
            if be.api.fs.isdir(listing[sel][0]) == 1:
                chdir(listing[sel][0])
                sel = 0
            else:
                vr("fselm")(listing[sel])
    chdir(old)


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
        "Beryllium OS Wio Operational Menu Program\n" + "Version 1.0\n\n" + "I'm eepy."
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
        else:
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

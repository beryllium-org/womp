def fselm(filen) -> None:
    while True:
        sel = vr("dmenu")(
            "File selected | " + filen[0],
            [
                "File info",
                "View as text",
                "Send over ducky",
                "Execute as a program",
                "Execute as a ducky script",
            ],
            hint="Press top left to close. Press Enter to select.",
        )
        if sel == -1:
            break
        elif not sel:
            sz = filen[3]
            if sz < 1024:
                sz = f"{int(sz)}B"
            elif sz < 1048576:
                sz = f"{int(sz/1024)}K"
            elif sz < 1073741824:
                sz = f"{int(sz/1048576)}M"
            else:
                sz = f"{int(sz/1073741824)}G"
            modtime = filen[4]
            modtime = (
                vr("mdict")[modtime.tm_mon]
                + " "
                + str(modtime[2])
                + " "
                + ("0" if modtime.tm_hour < 10 else "")
                + str(modtime[3])
                + ":"
                + ("0" if modtime.tm_min < 10 else "")
                + str(modtime[4])
            )
            vr("ctop")(
                "File Info: "
                + filen[0]
                + "\n"
                + (vr("c").size[0] * "-")
                + "\nFull path: \n"
                + str(be.api.fs.base())
                + "/"
                + filen[0]
                + "\n\nSize: "
                + sz
                + "\nModified: "
                + modtime
            )

            vr("waitc")()
            vr("refr")()
            v = vr("ri")()
        elif sel == 1:
            vr("d").clear()
            with be.api.fs.open(filen[0]) as f:
                lines = f.readlines()
                for i in lines[:-1]:
                    vr("d").nwrite(i)
                vr("d").nwrite(lines[-1][: -(1 if lines[-1][-1] == "\n" else 0)])
                vr("waitc")()
                vr("refr")()
                v = vr("ri")()
        elif sel == 2:
            if be.api.fs.isdir("/bin/duckycat.lja") == 0:
                vr("waitc")()
                vr("d").clear()
                vr("d").nwrite("Caternating to host.. ")
                vr("refr")()
                be.based.run("duckycat " + filen[0])
                if int(be.api.getvar("return")):
                    vr("d").nwrite("FAIL")
                else:
                    vr("d").nwrite("OK")
                vr("refr")()
                time.sleep(0.5)
                break
            else:
                vr("d").clear()
                vr("d").nwrite(
                    "Ducky not installed!\n"
                    + "Cannot continue.\n"
                    + "\nPress any key to go back."
                )
                vr("waitc")()
                vr("refr")()
                v = vr("ri")()
        elif sel == 3:
            if filen.endswith(".lja"):
                vr("waitc")()
                vr("d").clear()
                vr("d").nwrite("Running in based.. ")
                vr("refr")()
                be.based.command.exec(filen[0])
                vr("d").nwrite("Done")
                vr("refr")()
                time.sleep(0.5)
                break
            elif filen.endswith(".py"):
                vr("waitc")()
                vr("d").clear()
                vr("d").nwrite("Running in python.. ")
                vr("refr")()
                be.based.command.fpexec(filen[0])
                vr("d").nwrite("Done")
                vr("refr")()
                time.sleep(0.5)
                break
            else:
                vr("d").clear()
                vr("d").nwrite(
                    "Not an executable!\n"
                    + "Cannot continue.\n"
                    + "\nPress any key to go back."
                )
                vr("waitc")()
                vr("refr")()
                v = vr("ri")()
        else:
            if be.api.fs.isdir("/bin/ducky.lja") == 0:
                vr("waitc")()
                vr("d").clear()
                vr("d").nwrite("Running with ducky.. ")
                vr("refr")()
                be.based.run("ducky " + filen[0])
                if int(be.api.getvar("return")):
                    vr("d").nwrite("FAIL")
                else:
                    vr("d").nwrite("OK")
                vr("refr")()
                time.sleep(0.5)
                break
            else:
                vr("d").clear()
                vr("d").nwrite(
                    "Ducky not installed!\n"
                    + "Cannot continue.\n"
                    + "\nPress any key to go back."
                )
                vr("waitc")()
                vr("refr")()
                v = vr("ri")()


vr("fselm", fselm)
del fselm
vrp("ok")

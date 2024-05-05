def vsel(kid: int, chrl="[", chrt="]") -> None:
    ckl = vr("vkloc")[kid]
    vr("d").move(y=ckl[0] + 16, x=ckl[1])
    vr("d").nwrite(chrl)
    vr("d").move(y=ckl[0] + 16, x=ckl[2])
    vr("d").nwrite(chrt)


vr("vsel", vsel)
del vsel


def usel(kid: int) -> None:
    vr("vsel")(kid, " ", " ")


vr("usel", usel)
del usel


def kb(title: str = "Input text", prompt: str = "", start: str = None) -> bytes:
    sel = 21
    vr("caps", 0)
    vr("dr_keys")()
    vr("d").move(y=0, x=0)
    sps = int((52 - len(title)) / 2) - 2
    vr("d").nwrite(sps * " " + "| " + title + " |" + sps * " ")
    del sps
    vr("d").nwrite("-" * 52)
    vr("d").nwrite(prompt + "_")
    sty = 3
    stx = len(prompt)
    res = []
    if start is not None:
        res += list(bytes(start, "UTF-8"))
    repeat_mode = False
    last_key_time = 0
    while True:
        vr("vsel")(sel)
        vr("refr")()
        be.io.ledset(1)
        vr("d").buf[1] = ""
        vr("d").program()
        if repeat_mode:
            if time.monotonic() - last_key_time > 0.1:
                repeat_mode = False
            else:
                last_key_time = time.monotonic()
        be.io.ledset(3)
        k = vr("d").buf[0]
        if k in [-1, 4]:
            res.clear()
            break
        elif not k:
            vr("usel")(sel)
            if sel < 2:
                sel = 42
            elif sel < 12:
                sel = 41 + sel
            elif sel < 15:
                sel = 53
            elif sel == 15:
                sel = 0
            elif sel < 29:
                sel -= 14
            elif sel == 41:
                sel = 28
            elif sel < 42:
                sel -= 14
            elif sel < 53:
                sel -= 13
            else:
                sel = 41
            vr("vsel")(sel)
        elif k == 1:
            vr("usel")(sel)
            if not sel:
                sel = 14
            elif sel == 15:
                sel = 28
            elif sel == 29:
                sel = 41
            elif sel == 42:
                sel = 53
            else:
                sel -= 1
            vr("vsel")(sel)
        elif k == 2:
            vr("usel")(sel)
            if sel < 2:
                sel = 15
            elif sel < 28:
                sel += 14
            elif sel == 28:
                sel = 41
            elif sel < 41:
                sel += 13
            elif sel == 41:
                sel = 53
            elif sel == 42:
                sel = 0
            elif sel == 53:
                sel = 14
            else:
                sel -= 41
            vr("vsel")(sel)
        elif k == 3:
            vr("usel")(sel)
            if sel == 14:
                sel = 0
            elif sel == 28:
                sel = 15
            elif sel == 41:
                sel = 29
            elif sel == 53:
                sel = 42
            else:
                sel += 1
            vr("vsel")(sel)
        elif k == 7:
            usecaps = bool(vr("caps"))
            if vr("caps") == 2 and sel < 12 and sel != 1:
                usecaps = False
            keysel = vr("keys")[sel][usecaps]
            if vr("caps") == 1 and keysel != 401:
                vr("caps", 0)
                vr("dr_keys")()
            if keysel == 10:
                break
            elif keysel == -1:
                res.clear()
                break
            elif keysel == 401:
                vr("caps", int(not vr("caps")))
                vr("dr_keys")()
            elif keysel == 400:
                if vr("caps") != 2:
                    vr("caps", 2)
                else:
                    vr("caps", 0)
                vr("dr_keys")()
            elif keysel == 127:
                if res:
                    vr("d").move(y=sty, x=stx + len(res))
                    vr("d").nwrite("  \010\010 \010_")
                    res.pop()
                    vr("refr")()
            else:
                res.append(keysel)
                vr("d").move(y=sty, x=stx + len(res))
                vr("d").nwrite(chr(keysel) + "_")
                vr("refr")()
        mkeys = vr("c").in_waiting
        krep = time.monotonic()
        if not repeat_mode:
            if mkeys:
                repeat_mode = True
                while time.monotonic() - krep < 0.5:
                    if not vr("c").in_waiting:
                        repeat_mode = False
                        break
                last_key_time = time.monotonic()
        else:
            while (time.monotonic() - krep < 0.08) and vr("c").in_waiting:
                pass
            last_key_time = time.monotonic()
    return str(bytes(res), "UTF-8")


vr("kb", kb)
del kb
vrp("ok")

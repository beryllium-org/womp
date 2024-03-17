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

be.based.run(
    "rm /boot/boot.d/99-womp.lja /bin/womp/funcs1.py /bin/womp/funcs2.py /bin/womp/womp.py /bin/womp/init.lja /bin/womp.lja"
)
be.based.run("rmdir /bin/womp")

be.api.setvar("return", "0")

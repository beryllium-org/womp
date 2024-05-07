be.based.run(
    "rm /boot/boot.d/99-womp.lja /bin/womp/init.py /bin/womp/load_fm.py /bin/womp/load_kb.py /bin/womp/load_lock.py /bin/womp/unload_fm.py /bin/womp/unload_kb.py /bin/womp/unload_lock.py /bin/womp/womp.py /bin/womp.lja"
)
be.based.run("rmdir /bin/womp")

be.api.setvar("return", "0")

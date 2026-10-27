import socket, subprocess, platform
def log(*a): print("[WB-PROBE]", *a, flush=True)
log("start |", platform.platform())
targets = [("zloj5610.bohrium.tech",22,"C2-SSH"),("github.com",443,"github"),
           ("raw.githubusercontent.com",443,"githubraw"),("wispbyte.com",443,"panel")]
for h,p,name in targets:
    try:
        s=socket.create_connection((h,p),timeout=8)
        banner=b""
        if name=="C2-SSH":
            s.settimeout(3)
            try: banner=s.recv(80)
            except Exception: pass
        log(f"{name} {h}:{p} -> OK", banner[:60])
        s.close()
    except Exception as e:
        log(f"{name} {h}:{p} -> FAIL", repr(e)[:90])
for tool in ["ssh","curl","python3","bash","tar","git"]:
    r=subprocess.run(["which",tool],capture_output=True,text=True)
    log(tool,"=",r.stdout.strip() or "MISSING")
log("end")

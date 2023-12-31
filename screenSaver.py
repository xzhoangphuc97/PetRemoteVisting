import subprocess
def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)
    
def setTimeOff():
    run_win_cmd("powercfg -change -monitor-timeout-ac 1")
    run_win_cmd("powercfg -change -monitor-timeout-dc 1")

def onScreen():
    run_win_cmd("powercfg -change -monitor-timeout-ac 0")
    run_win_cmd("powercfg -change -monitor-timeout-dc 0")

import webbrowser
import time
icount =0
print("this program started on" +  time.ctime())
while (icount <3):
    time.sleep(10)
    webbrowser.open("http://www.youku.com")
    icount = icount +1

import time
import webbrowser

total_breaks = 3
break_count = 0
work_time = 10 #2 * 60 * 60

print "Program started at " + time.ctime()
while break_count < total_breaks:
    time.sleep(work_time)
    print "Break time #" + str(break_count + 1) + ": " + time.ctime()
    webbrowser.open("https://www.youtube.com/watch?v=1TphEh0Qgv0")
    break_count += 1
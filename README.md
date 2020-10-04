# SimpleCPUMonitor

This project is a simple python package for monitoring the CPU usage of Google Colab.
In order to make it run, you only need to first import and install the package using pip3:

```
!pip3 install git+https://github.com/k-timy/SimpleCPUMonitor.git
```
Then, you can simply import and call it:

```
from SimpleCPUMonitor import CPUMonitor
import time

monitor = CPUMonitor()

# run a time consuming thread...
for i in range(10):
    time.sleep(0.6)
# done with the process.    

# Calling stop function is necessary
monitor.stop()
```

When all your processes are finished, you need to stop the monitor by calling **stop()** function. Otherwise, the thread that it is running on keeps running for some reason that I don't know. In fact, since I have set that thread as **'Daemon'**, it is expected to be killed with force while the program's main thread is stopped for any reasons.
However, on Google Colab, that thread is not stopped automatically.

You can run this in [colab here](https://github.com/k-timy/SimpleCPUMonitor/blob/main/example.ipynb).

# Feedbacks

Feel free to provide me with your feedbacks on this or fork to extend this project on your own.

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

monitor.stop()
```

You can run this in [colab here](https://github.com/k-timy/SimpleCPUMonitor/blob/main/example.ipynb).

# Feedbacks

Feel free to provide me with your feedbacks on this or fork to extend this project on your own.

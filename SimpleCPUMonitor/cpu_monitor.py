import psutil
import threading
import time
import ipywidgets as widgets
from ipywidgets import Layout, Box
from IPython.display import display

class CPUMonitor:
    """ To display the CPU usage while running a code. Particularly, on Google Colab
    platform where we do not have access to its cpu usage in a live session"""
    def __init__(self, update_interval=0.5):
        self.update_interval = update_interval
        self.num_cpus = psutil.cpu_count()
        self.perf_thread = threading.Thread(target=self.update_data, daemon=True)
        self.keep_running = True
        self.perf_thread.start()
        
        self.bars = []        
        for i in range(self.num_cpus):
            widget = widgets.IntProgress(
                value=0,
                min=0,
                max=100,
                step=1,
                description='CPU #{}'.format(i),
                bar_style='success', # 'success', 'info', 'warning', 'danger' or ''
                orientation='vertical',
                readout=True,
                readout_format='d'
            )                 
            self.bars.append(widget)
        items_layout = Layout( width='auto')
        box_layout = Layout(display='flex',
                            flex_flow='row',
                            align_items='stretch',
                            border='solid',
                            width='auto')
        box = Box(children=self.bars, layout=box_layout)
        display(box)

    def update_data(self):
        while self.keep_running:
            time.sleep(self.update_interval)        
            cpu_percents = psutil.cpu_percent(percpu=True)
            for idx, bar in enumerate(self.bars):
                bar.value = cpu_percents[idx]
    def stop(self):
        """ Although the thread is executed as Daemon, it does not stop even
        after interrupting a cell's execution on Google Colab, for some reason.
        So, this function should be called in the end. To put an end to
        this thread manully."""
        self.keep_running = False

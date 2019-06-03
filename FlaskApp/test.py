from threading import Timer
import time
import psutil
from datetime import datetime
from forms import ProcessForm
from getPCmemory import one_process_memo


myform = ProcessForm()
myform.processName.choice = one_process_memo()

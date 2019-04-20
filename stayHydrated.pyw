from rx import Observable
from win10toast import ToastNotifier
import time

toastr = ToastNotifier()
toastr.show_toast("Stay Hydrated!", "Stay hydrated script is active", duration=60, icon_path="water.ico")
#RxPy timer in ms
Observable.timer(5400000, 5400000).subscribe(lambda v: toastr.show_toast("Stay Hydrated!","Time to drink!", icon_path="water.ico", duration=600))

#Time to sleep in seconds
time.sleep(86400)
toastr.show_toast("Stay Hydrated!", "WARNING: 7 day limit passed", duration=600, icon_path="water.ico")
time.sleep(600)
from win10toast import ToastNotifier

try:
    Noti = ToastNotifier()
    Noti.show_toast("Hello world!!", "holisss este es el mensaje", duration=10)
except Exception as e:
    print(f"error: {e}")
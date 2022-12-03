import time
from plyer import notification
while(True):
    if time.strftime('%H:%M')=="11:30":
        notification.notify(
            title="drink some water",
            message="it will keep you healthy you need 3.9 L",
            timeout=12
        )
        time.sleep(60*30)
    elif time.strftime('%H:%M')=="12:00":
        notification.notify(
            title="drink water now",
            message="it will keep you healthy you need 3.9 L",
            timeout=12
        )
        time.sleep(60*30)
    elif time.strftime('%H:%M')=="12:30":
        notification.notify(
            title="take a walk",
            message="it will make your mood fresh",
            timeout=12
        )
        time.sleep(60*30)
    elif time.strftime('%H:%M')=="13:23":
        notification.notify(
            title="drink some water",
            message="it will make your body and mind fresh and healthy",
            timeout=12
        )
        time.sleep(60*60)
    elif time.strftime('%H:%M') == "14:00":
        notification.notify(
            title="shut down the computer",
            message="time for the break",
            timeout=12
        )
        time.sleep(60 * 90)
    elif time.strftime('%H:%M') == "15:30":
        notification.notify(
            title="welcome sir how was the break",
            message="seven",
            timeout=12
        )
        time.sleep(60 * 60)
    elif time.strftime('%H:%M') == "16:30":
        notification.notify(
            title="drink some water",
            message="it will keep you healthy",
            timeout=12
        )
        time.sleep(60*30)
    elif time.strftime('%H:%M') == "17:00":
        notification.notify(
            title="take a walk",
            message="it will keep you healthy and fresh",
            timeout=12
        )
        time.sleep(60*60)
    elif time.strftime('%H:%M') == "18:00":
        notification.notify(
            title="take a walk and drink water",
            message="it will keep you healthy and fresh",
            timeout=12
        )
        time.sleep(60*60)
    elif time.strftime('%H:%M') == "19:00":
        notification.notify(
            title="shut down the computer",
            message="you need rest",
            timeout=12

        )
        exit()